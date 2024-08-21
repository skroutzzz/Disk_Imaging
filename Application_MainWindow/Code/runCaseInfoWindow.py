import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit, QMessageBox
from PySide6.QtCore import Slot
from case_info import CaseInfo

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.CaseInfoWindow import Ui_CaseInfoWindow
from runNewTypeWindow import NewTypeWindow

class CaseInfoWindow(QMainWindow, Ui_CaseInfoWindow):
    def __init__(self, case_info: CaseInfo):
        super(CaseInfoWindow, self).__init__()
        self.setupUi(self)
        self.case_info = case_info

        #Define attributes to store user input
        
        self.ciw_browseButton.clicked.connect(self.browse_base_directory)
        
        self.ciw_nextButton.clicked.connect(self.store_user_input_and_open_new_type_window)

       


    def browse_base_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Base Directory")
        if directory:
            self.ciw_baseEdit.setText(directory)

    def store_user_input_and_open_new_type_window(self):      
        self.case_info.case_name = self.ciw_caseNameEdit.text().strip(),
        self.case_info.base_directory = self.ciw_baseEdit.text().strip(),
        self.case_info.case_number = self.lineEdit_3.text().strip(),
        self.case_info.examiner_name = self.ciw_examinerNameEdit.text().strip(),
        self.case_info.examiner_phone = self.ciw_examinerPhoneEdit.text().strip(),
        self.case_info.examiner_email = self.ciw_examinerEmailEdit.text().strip(),
        self.case_info.notes = self.ciw_notesEdit.text().strip()

        print(f"Type of ciw_caseNameEdit: {type(self.ciw_caseNameEdit)}")
        print(f"Case Name after strip: '{self.case_info.case_name}'")
        print(f"Directory after strip: '{self.case_info.base_directory}'")

        try:
            print("Attempting to validate...")
            self.case_info.validate_case_info()
        except ValueError as e:
            print(f"Validation failed: {e}")
            QMessageBox.critical(self, "Validation Error", str(e))
            return
        print("Proceeding to the next window...")
        self.new_type_window = NewTypeWindow(self.case_info)
        self.new_type_window.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    case_info = CaseInfo()
    caseInfo_window = CaseInfoWindow(case_info)
    caseInfo_window.show()
    sys.exit(app.exec())