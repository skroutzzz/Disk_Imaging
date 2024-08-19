import sys
import os
import re
import hashlib
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QThread, Signal, QProcess, Slot
import subprocess

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
    def __init__(self):
        super(ProgressWindow, self).__init__()
        self.setupUi(self)

        
        self.target_size_mb = None
        self.source_hashes = None
        self.pw_backButton.clicked.connect(self.run_dd_command)

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
        source_device = "/dev/sdb"  # Adjust this to the correct source disk
        output_file = "/home/skroutz/Documents/Case/disk_image.img"  # Adjust this to the correct destination path
        block_size = "4M"

        if not os.path.exists(source_device):
            QMessageBox.critical(self, "Error", f"The source device or file {source_device} does not exist")
            return

        size_bytes = self.get_device_size(source_device)
        #self.target_size_mb = self.get_device_size(source_device)
        if size_bytes is None:
            return
        
        

        #command = ['if=' + source_device, 'of=' + output_file, 'bs=' + block_size, 'status=progress']

        

        self.pw_progressBar.setValue(0)
        self.pw_progressBar.setVisible(True)
        self.statusBar().showMessage("Calculating source disk hashes...")

        self.hashing_worker = HashingWorker(source_device, ['md5', 'sha256'], size_bytes)
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
        source_device = "/dev/sdb"  # Adjust this to the correct source disk
        output_file = "/home/skroutz/Documents/Case/disk_image.img"  # Adjust this to the correct destination path
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

        self.hashing_worker = HashingWorker(output_file, ['md5', 'sha256'], size_bytes)
        self.hashing_worker.hash_calculated.connect(self.on_output_hashes_calculated)
        self.hashing_worker.progress_update.connect(self.pw_progressBar.setValue)
        self.hashing_worker.start()



                     

    @Slot()
    def on_output_hashes_calculated(self, hashes):
        
        if hashes is None:
            QMessageBox.critical(self, "Error", "Failed to calculated output file hashes.")
            return

        print(f"Image MD5: {hashes['md5']}")
        print(f"Image SHA256: {hashes['sha256']}")

        QMessageBox.information(self, "Imaging Complete", 
                                f"Imaging and hashing are complete.\n\n"
                                f"Source MD5: {self.source_hashes['md5']}\n"
                                f"Source SHA256: {self.source_hashes['sha256']}\n\n"
                                f"Image MD5: {hashes['md5']}\n"
                                f"Image SHA256: {hashes['sha256']}")

        QMessageBox.information(self, "Success", "dd command completed successfully!")
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    progress_window = ProgressWindow()
    progress_window.show()
    sys.exit(app.exec())
