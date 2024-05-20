import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.NewHostWindow import Ui_NewDataSourceWindow
from runNewTypeWindow import NewTypeWindow


class NewHostWindow(QMainWindow, Ui_NewDataSourceWindow):
    def __init__(self):
        super(NewHostWindow, self).__init__()
        self.setupUi(self)

        self.nhw_NextButton.clicked.connect(self.open_NewTypeWindow)

    @Slot()
    def open_NewTypeWindow(self):
        self.newTypeWindow = NewTypeWindow()
        self.newTypeWindow.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    newHost_window = NewHostWindow()
    newHost_window.show()
    sys.exit(app.exec())