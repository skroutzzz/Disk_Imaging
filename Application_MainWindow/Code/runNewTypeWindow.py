import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.NewTypeWindow import Ui_NewTypeWindow
from runIngestModuleWindow import IngestModuleWindow


class NewTypeWindow(QMainWindow, Ui_NewTypeWindow):
    def __init__(self, case_info):
        super(NewTypeWindow, self).__init__()
        self.setupUi(self)
        self.case_info = case_info

        self.ntw_nextButton.clicked.connect(self.store_selection_and_open_ingest_module_window)

        
    def store_selection_and_open_ingest_module_window(self):
        self.case_info['disk_type'] = 'local_disk' if self.ntw_localDiskButton.isChecked() else 'other'

        from runIngestModuleWindow import IngestModuleWindow
        self.ingest_module_window = IngestModuleWindow(self.case_info)
        self.ingest_module_window.show()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    case_info = {}
    newType_window = NewTypeWindow({})
    newType_window.show()
    sys.exit(app.exec())