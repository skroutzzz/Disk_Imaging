import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QComboBox, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Slot
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.SelectDataWindow import Ui_SelectDataWindow
from runProgressWindow import ProgressWindow


class SelectDataWindow(QMainWindow, Ui_SelectDataWindow):
    def __init__(self, case_info):
        super(SelectDataWindow, self).__init__()
        self.setupUi(self)
        self.case_info = case_info

        
        self.sdw_comboBox.addItems(self.get_available_devices())

        self.populate_devices()
        self.sdw_nextButton.clicked.connect(self.store_selection_and_open_progress_window)
        

    def populate_devices(self):
        devices = self.get_available_devices()
        for device in devices:
            device_name = device["name"]
            device_size = device["size"]
            self.sdw_comboBox.addItem(f"{device_name} - {device_size}", device_name)

    def get_available_devices(self):
        devices = []
        try:
            result = subprocess.run(['lsblk', '-ndo', 'NAME,SIZE,TYPE'], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            for line in output.splitlines():
                name, size, device_type = line.split()
                if device_type == 'disk':
                    devices.append({"name": f"/dev/{name}","size": size})
        except Exception as e:
            print(f"Error retrieving devices: {e}")
        return devices

  

    def store_selection_and_open_progress_window(self):
        selected_device = self.sdw_comboBox.currentData()
        self.case_info['source_disk'] = selected_device

        from runProgressWindow import ProgressWindow
        self.progress_window = ProgressWindow(self.case_info)
        self.progress_window.show()
        self.close()   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    case_info = {}
    selectData_window = SelectDataWindow({})
    selectData_window.show()
    sys.exit(app.exec())