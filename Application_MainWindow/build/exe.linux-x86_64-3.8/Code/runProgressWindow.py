import sys
import os
import re
import hashlib
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QThread, Signal, QProcess, Slot
import subprocess
import datetime
from case_info import CaseInfo

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.ProgressWindow import Ui_ProgresWindow

class HashingWorker(QThread):
    hash_calculated = Signal(dict)
    progress_update = Signal(int)

    def __init__(self, filepath, hash_algorithms, size_bytes):
        super().__init__()
        self.filepath = filepath
        self.hash_algorithms = hash_algorithms
        self.size_bytes = size_bytes

    def run(self):
        try:
            if not os.path.exists(self.filepath):
                raise FileNotFoundError(f"File or device {self.filepath} does not exist.")
            
            #total_size = os.path.getsize(self.filepath)
            if self.size_bytes == 0:
                raise ValueError("The file or device size is zero, cannot calculate hashes on an empty source")
            
            hashers = {alg: hashlib.new(alg) for alg in self.hash_algorithms}
            #total_size = os.path.getsize(self.filepath)
            processed_size = 0

            with open(self.filepath, 'rb') as f:
                while True:
                    block = f.read(4096)
                    if not block:
                        break
                    for hasher in hashers.values():
                        hasher.update(block)
                    processed_size += len(block)
                    progress = int((processed_size / self.size_bytes) * 100)
                    self.progress_update.emit(progress)

            result_hashes = {alg: hasher.hexdigest() for alg, hasher in hashers.items()}
            self.hash_calculated.emit(result_hashes)
        except Exception as e:
            print(f"Error during hashing: {str(e)}")
            self.hash_calculated.emit(None)             



class ProgressWindow(QMainWindow, Ui_ProgresWindow):
    def __init__(self, case_info: CaseInfo):
        super(ProgressWindow, self).__init__()
        self.setupUi(self)
        self.case_info = case_info
        

        print(f"Base Directory: {self.case_info.base_directory} (Type: {type(self.case_info.base_directory)})")
        self.target_size_mb = None
        self.source_hashes = None
        self.pw_beginButton.clicked.connect(self.run_dd_command)

    def check_permissions(self, device):
        if not os.access(device, os.R_OK):
            QMessageBox.critical(self, "Permission Denied", f"Permission denied to read {device}")
            sys.exit(1)


    def get_device_size(self,device):
        try:
            if os.path.exists(device) and not os.path.isdir(device):
                if os.path.isfile(device):
                    size_bytes = os.path.getsize(device)
                else:
                    self.check_permissions(device)
                    size_output = subprocess.check_output(['blockdev', '--getsize64', device]).decode('utf-8').strip()
                    size_bytes = int(size_output)

                size_mb = size_bytes / (1024 * 1024)
                return size_bytes
            else:
                raise ValueError(f"Device or file {device} is not valid")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to determine the size of the {device}.\nError: {str(e)}")
            return None
    
    def calculate_hashes(self, filepath, hash_algorithms):

        try:
            hashers = {alg: hashlib.new(alg) for alg in hash_algorithms}
            with open(filepath, 'rb') as f:
                for block in iter(lambda: f.read(4096), b""):
                    for hasher in hashers.values():
                        hasher.update(block)
            return {alg: hasher.hexdigest() for alg, hasher in hasher.items()}
        except Exception as e:
            print(f"Error during hashing of {filepath}: {str(e)}")
            return None
        
    Slot()
    def run_dd_command(self):
        source_device = self.case_info.source_disk  # Adjust this to the correct source disk
        #output_file = os.path.join(self.case_info.base_directory, "disk_image.img")  # Adjust this to the correct destination path
        #block_size = "4M"

        if not os.path.exists(source_device):
            QMessageBox.critical(self, "Error", f"The source device or file {source_device} does not exist")
            return

        size_bytes = self.get_device_size(source_device)
        #self.target_size_mb = self.get_device_size(source_device)
        if size_bytes is None:
            return
        
        hash_algorithms = []
        if self.case_info.hash_algorithms['md5']:
            hash_algorithms.append('md5')
        if self.case_info.hash_algorithms['sha256']:
            hash_algorithms.append('sha256')
        

        self.pw_progressBar.setValue(0)
        self.pw_progressBar.setVisible(True)
        self.statusBar().showMessage("Calculating source disk hashes...")

        self.hashing_worker = HashingWorker(source_device, hash_algorithms, size_bytes)
        self.hashing_worker.hash_calculated.connect(self.on_source_hashes_calculated)
        self.hashing_worker.progress_update.connect(self.pw_progressBar.setValue)
        self.hashing_worker.start()

        #self.process.start("/bin/dd", command)


    @Slot(dict)
    def on_source_hashes_calculated(self, hashes):
        if hashes is None:
            QMessageBox.critical(self, "Error", "Failed to calculate source disk hashes.")
            return
        
        self.source_hashes = hashes
        self.pw_progressBar.setVisible(False)
        self.statusBar().clearMessage()

        print(f"Source MD5: {self.source_hashes['md5']}")
        print(f"Source SHA256: {self.source_hashes['sha256']}")

        QMessageBox.information(self, "Hashing Complete", "Source hashing complete. Imaging willl now begin")

        self.start_imaging_process()

    def start_imaging_process(self):
        source_device = self.case_info.source_disk  # Adjust this to the correct source disk
        output_file = os.path.join(self.case_info.base_directory, "disk_image.img")  # Adjust this to the correct destination path
        block_size = "4M"

        command = ['if=' + source_device, 'of=' + output_file, 'bs=' + block_size, 'status=progress']

        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.update_progress)
        self.process.finished.connect(lambda: self.on_imaging_finished(output_file))

        self.pw_progressBar.setValue(0)
        self.pw_progressBar.setVisible(True)

        self.process.start("/bin/dd", command)


    @Slot()
    def update_progress(self):
        output = str(self.process.readAllStandardOutput(), 'utf-8')
        print(output)

        for line in output.splitlines():
            if 'bytes' in line:
                match = re.search(r'(\d+) bytes', line)
                if match:
                        copied_bytes = int(match.group(1))
                        copied_mb = copied_bytes / (1024 * 1024)

                        if self.target_size_mb:
                            progress_percentage = (copied_mb / self.target_size_mb) *100
                            self.pw_progressBar.setValue(int(progress_percentage))

    @Slot()
    def on_imaging_finished(self, output_file):
        self.pw_progressBar.setValue(100)
        self.pw_progressBar.setVisible(False)

        size_bytes = self.get_device_size(output_file)
        if size_bytes is None:
            QMessageBox.critical(self, "Error", "Failed to determine the size of the output file")
            return
        
        self.pw_progressBar.setValue(0)
        self.pw_progressBar.setVisible(True)
        self.statusBar().showMessage("Calculating output file hashes...")

        hash_algorithms = []
        if self.case_info.hash_algorithms['md5']:
            hash_algorithms.append('md5')
        if self.case_info.hash_algorithms['sha256']:
            hash_algorithms.append('sha256')

        self.hashing_worker = HashingWorker(output_file, hash_algorithms, size_bytes)
        self.hashing_worker.hash_calculated.connect(self.on_output_hashes_calculated)
        self.hashing_worker.progress_update.connect(self.pw_progressBar.setValue)
        self.hashing_worker.start()



                     

    @Slot()
    def on_output_hashes_calculated(self, hashes):
        
        if hashes is None:
            QMessageBox.critical(self, "Error", "Failed to calculated output file hashes.")
            return

        print(f"Image MD5: {hashes.get('md5', 'Not Calculated')}")
        print(f"Image SHA256: {hashes.get('sha256', 'Not Calculated')}")

        QMessageBox.information(self, "Imaging Complete", 
                                f"Imaging and hashing are complete.\n\n"
                                f"Source MD5: {self.source_hashes.get('md5', 'Not Calculated')}\n"
                                f"Source SHA256: {self.source_hashes.get('sha256', 'Not Calculated')}\n\n"
                                f"Image MD5: {hashes.get('md5', 'Not Calculated')}\n"
                                f"Image SHA256: {hashes.get('sha256', 'Not Calculated')}")

        

        self.save_case_info_with_hashes(hashes)

        QMessageBox.information(self, "Success", "dd command completed successfully!")

    def save_case_info_with_hashes(self, image_hashes):

        info_file_path = os.path.join(self.case_info.base_directory, "disk_image_info.txt")

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(info_file_path, 'w') as file:
                file.write("Case Information:\n")
                file.write(f"Case Name: {self.case_info.case_name}\n")
                file.write(f"Investigator: {self.case_info.examiner_name}\n")
                file.write(f"Source Disk: {self.case_info.source_disk}\n")
                file.write(f"Output Directory: {self.case_info.base_directory}\n")
                file.write(f"Creation Date: {current_time}\n")
                file.write("\nHashes:\n")
                file.write(f"Source MD5: {self.source_hashes.get('md5', 'Not Calculated')}\n")
                file.write(f"Source SHA256: {self.source_hashes.get('sha256', 'Not Calculated')}\n")
                file.write(f"Image MD5: {image_hashes.get('md5', 'Not Calculated')}\n")
                file.write(f"Image SHA256: {image_hashes.get('sha256', 'Not Calculated')}\n")

            os.chmod(info_file_path, 0o444)

            print(f"Case information saved to: {info_file_path}")

        except Exception as e:
            print(f"Failed to save case info: {str(e)}")
            QMessageBox.critical(self, "Error", f"Failed to save case information. \nError: {str(e)}")
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    case_info = CaseInfo()
    progress_window = ProgressWindow(case_info)
    progress_window.show()
    sys.exit(app.exec())
