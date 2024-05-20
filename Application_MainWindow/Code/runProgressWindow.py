import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.ProgressWindow import Ui_ProgresWindow


class ProgressWindow(QMainWindow, Ui_ProgresWindow):
    def __init__(self):
        super(ProgressWindow, self).__init__()
        self.setupUi(self)
        self.close()

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    selectProgress_window = ProgressWindow()
    selectProgress_window.show()
    sys.exit(app.exec())