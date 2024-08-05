import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.CaseInfoWindow import Ui_CaseInfoWindow
from runNewHostWindow import NewHostWindow

class CaseInfoWindow(QMainWindow, Ui_CaseInfoWindow):
    def __init__(self):
        super(CaseInfoWindow, self).__init__()
        self.setupUi(self)

        self.ciw_nextButton.clicked.connect(self.open_newHostWindow)


    
    @Slot()
    def open_newHostWindow(self):
        self.newHostWindow = NewHostWindow()
        self.newHostWindow.show()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    caseInfo_window = CaseInfoWindow()
    caseInfo_window.show()
    sys.exit(app.exec())