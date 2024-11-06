import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from case_info import CaseInfo
from UI.IngestModuleWindow import Ui_IngestModuleWindow
from runSelectDataWindow import SelectDataWindow


class IngestModuleWindow(QMainWindow, Ui_IngestModuleWindow):
    def __init__(self, case_info:CaseInfo):
        super(IngestModuleWindow, self).__init__()
        self.setupUi(self)
        self.case_info = case_info

        

        self.imw_nextButton.clicked.connect(self.store_selections_and_open_select_data_window)

    def store_selections_and_open_select_data_window(self):
        md5_selected = self.imw_md5Checkbox.isChecked()
        sha256_selected = self.imw_shaCheckbox.isChecked()
        verification_selected = self.imw_verificationCheckbox.isChecked()

        self.case_info.set_hash_algorithms(md5=md5_selected, sha256=sha256_selected, verification=verification_selected)

        print(f"MD5 Selected: {self.case_info.hash_algorithms['md5']}")
        print(f"SHA256 Selected: {self.case_info.hash_algorithms['sha256']}")
        print(f"Verification Selected: {self.case_info.hash_algorithms['verification']}")

        from runSelectDataWindow import SelectDataWindow
        self.select_data_window = SelectDataWindow(self.case_info)
        self.select_data_window.show()
        self.close()

 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    case_info = CaseInfo()
    ingestModule_window = IngestModuleWindow(case_info)
    ingestModule_window.show()
    sys.exit(app.exec())