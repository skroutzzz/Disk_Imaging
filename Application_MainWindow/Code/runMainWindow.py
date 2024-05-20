import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.MainWindow import Ui_MainWindow
from runCaseInfoWindow import CaseInfoWindow
from runNewHostWindow import NewHostWindow




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.mw_newCaseButton.clicked.connect(self.open_caseInfoWindow)
        self.mw_addDataSourceButton.clicked.connect(self.open_newHostWindow)
        
        

        
    @Slot()
    def open_caseInfoWindow(self):
        self.caseWindow = CaseInfoWindow()
        self.caseWindow.show()

    @Slot()
    def open_newHostWindow(self):
        self.newHostWindow = NewHostWindow()
        self.newHostWindow.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())