import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from case_info import CaseInfo
from UI.NewTypeWindow import Ui_NewTypeWindow
from runIngestModuleWindow import IngestModuleWindow


class NewTypeWindow(QMainWindow, Ui_NewTypeWindow):
    def __init__(self, case_info: CaseInfo):
        super(NewTypeWindow, self).__init__()
        self.setupUi(self)
        self.case_info = case_info

        self.ntw_nextButton.clicked.connect(self.store_selection_and_open_ingest_module_window)

        
    def store_selection_and_open_ingest_module_window(self):
        if self.ntw_localDiskButton.isChecked():
            disk_type = 'local_disk'
        else:
            QMessageBox.warning(self, "Selection Error", "The system only supports local disk for now")

        print(f"Case Name after strip: '{self.case_info.case_name}'")
        self.case_info.set_disk_type(disk_type)

        print(f"Disk type '{self.case_info.disk_type}'")
        self.ingest_module_window = IngestModuleWindow(self.case_info)
        self.ingest_module_window.show()
        self.close()


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    case_info = CaseInfo()
    newType_window = NewTypeWindow(case_info)
    newType_window.show()
    sys.exit(app.exec())