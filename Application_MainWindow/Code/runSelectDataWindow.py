import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.SelectDataWindow import Ui_SelectDataWindow
from runProgressWindow import ProgressWindow


class SelectDataWindow(QMainWindow, Ui_SelectDataWindow):
    def __init__(self):
        super(SelectDataWindow, self).__init__()
        self.setupUi(self)

        self.sdw_nextButton.clicked.connect(self.open_ProgressWindow)


    @Slot()
    def open_ProgressWindow(self):
        self.progressWindow = ProgressWindow()
        self.progressWindow.show()
        self.close()



        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    selectData_window = SelectDataWindow()
    selectData_window.show()
    sys.exit(app.exec())