import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.CaseInfoWindow import Ui_CaseInfoWindow
from runNewHostWindow import NewHostWindow
from runNewTypeWindow import NewTypeWindow

class CaseInfoWindow(QMainWindow, Ui_CaseInfoWindow):
    def __init__(self):
        super(CaseInfoWindow, self).__init__()
        self.setupUi(self)

        #Define attributes to store user input
        self.ciw_caseNameEdit = QLineEdit()
        self.ciw_baseEdit = QLineEdit()
        self.ciw_browseButton.clicked.connect(self.browse_base_directory)
        self.lineEdit_3 = QLineEdit()
        self.ciw_examinerNameEdit = QLineEdit()
        self.ciw_examinerEmailEdit = QLineEdit()
        self.ciw_examinerPhoneEdit = QLineEdit()
        self.ciw_nextButton.clicked.connect(self.store_user_input_and_open_new_type_window)

        #self.ciw_nextButton.clicked.connect(self.open_newHostWindow)
        #self.ciw_nextButton.clicked.connect(self.open_NewTypeWindow)


    def browse_base_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Base Directory")
        if directory:
            self.ciw_baseEdit.setText(directory)

    def store_user_input_and_open_new_type_window(self):
        case_info = {
            "case_name": self.ciw_caseNameEdit.text(),
            "base_directory": self.ciw_baseEdit.text(),
            "case_number": self.lineEdit_3.text(),
            "examiner_name": self.ciw_examinerNameEdit.text(),
            "examiner_phone": self.ciw_examinerPhoneEdit.text(),
            "examiner_email": self.ciw_examinerEmailEdit.text(),
            "notes": self.ciw_notesEdit.text()
        }

        from runNewTypeWindow import NewTypeWindow
        self.new_type_window = NewTypeWindow(case_info)
        self.new_type_window.show()
        self.close()
    
    @Slot()
    def open_newHostWindow(self):
        self.newHostWindow = NewHostWindow()
        self.newHostWindow.show()
        self.close()

    @Slot()
    def open_NewTypeWindow(self):
        self.newTypeWindow = NewTypeWindow()
        self.newTypeWindow.show()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    caseInfo_window = CaseInfoWindow()
    caseInfo_window.show()
    sys.exit(app.exec())