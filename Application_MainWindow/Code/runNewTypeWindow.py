import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.NewTypeWindow import Ui_NewTypeWindow
from runIngestModuleWindow import IngestModuleWindow


class NewTypeWindow(QMainWindow, Ui_NewTypeWindow):
    def __init__(self):
        super(NewTypeWindow, self).__init__()
        self.setupUi(self)

        self.ntw_nextButton.clicked.connect(self.open_IngestModuleWindow)

        

    @Slot()
    def open_IngestModuleWindow(self):
        self.ingestModuleWindow = IngestModuleWindow()
        self.ingestModuleWindow.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    newType_window = NewTypeWindow()
    newType_window.show()
    sys.exit(app.exec())