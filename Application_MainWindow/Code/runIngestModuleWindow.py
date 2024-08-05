import sys 
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from UI.IngestModuleWindow import Ui_IngestModuleWindow
from runSelectDataWindow import SelectDataWindow


class IngestModuleWindow(QMainWindow, Ui_IngestModuleWindow):
    def __init__(self):
        super(IngestModuleWindow, self).__init__()
        self.setupUi(self)

        self.imw_nextButton.clicked.connect(self.open_SelectDataWindow)

    

    @Slot()
    def open_SelectDataWindow(self):
        self.selectDataWindow = SelectDataWindow()
        self.selectDataWindow.show()
        self.close()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ingestModule_window = IngestModuleWindow()
    ingestModule_window.show()
    sys.exit(app.exec())