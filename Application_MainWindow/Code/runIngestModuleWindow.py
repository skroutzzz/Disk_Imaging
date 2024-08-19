import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.IngestModuleWindow import Ui_IngestModuleWindow
from runSelectDataWindow import SelectDataWindow


class IngestModuleWindow(QMainWindow, Ui_IngestModuleWindow):
    def __init__(self, case_info):
        super(IngestModuleWindow, self).__init__()
        self.setupUi(self)
        self.case_info = case_info

        

        self.imw_nextButton.clicked.connect(self.store_selections_and_open_select_data_window)

    def store_selections_and_open_select_data_window(self):
        self.case_info['md5'] = self.imw_md5Checkbox.isChecked()
        self.case_info['sha256'] = self.imw_shaCheckbox.isChecked()
        self.case_info['verification'] = self.imw_verificationCheckbox.isChecked()

        from runSelectDataWindow import SelectDataWindow
        self.select_data_window = SelectDataWindow(self.case_info)
        self.select_data_window.show()
        self.close()

    @Slot()
    def open_SelectDataWindow(self):
        self.selectDataWindow = SelectDataWindow()
        self.selectDataWindow.show()
        self.close()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    case_info = {}
    ingestModule_window = IngestModuleWindow({})
    ingestModule_window.show()
    sys.exit(app.exec())