# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewTypeWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_NewTypeWindow(object):
    def setupUi(self, NewTypeWindow):
        if not NewTypeWindow.objectName():
            NewTypeWindow.setObjectName(u"NewTypeWindow")
        NewTypeWindow.resize(800, 600)
        self.centralwidget = QWidget(NewTypeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ntw_backButton = QPushButton(self.centralwidget)
        self.ntw_backButton.setObjectName(u"ntw_backButton")

        self.horizontalLayout.addWidget(self.ntw_backButton)

        self.ntw_nextButton = QPushButton(self.centralwidget)
        self.ntw_nextButton.setObjectName(u"ntw_nextButton")

        self.horizontalLayout.addWidget(self.ntw_nextButton)

        self.ntw_finishButton = QPushButton(self.centralwidget)
        self.ntw_finishButton.setObjectName(u"ntw_finishButton")

        self.horizontalLayout.addWidget(self.ntw_finishButton)

        self.ntw_cancelButton = QPushButton(self.centralwidget)
        self.ntw_cancelButton.setObjectName(u"ntw_cancelButton")

        self.horizontalLayout.addWidget(self.ntw_cancelButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.ntw_groupBox = QGroupBox(self.centralwidget)
        self.ntw_groupBox.setObjectName(u"ntw_groupBox")
        self.formLayout = QFormLayout(self.ntw_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.ntw_diskImageButton = QRadioButton(self.ntw_groupBox)
        self.ntw_diskImageButton.setObjectName(u"ntw_diskImageButton")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.ntw_diskImageButton)

        self.ntw_localDiskButton = QRadioButton(self.ntw_groupBox)
        self.ntw_localDiskButton.setObjectName(u"ntw_localDiskButton")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.ntw_localDiskButton)

        self.ntw_logicalFileButton = QRadioButton(self.ntw_groupBox)
        self.ntw_logicalFileButton.setObjectName(u"ntw_logicalFileButton")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ntw_logicalFileButton)

        self.ntw_unallocatedButton = QRadioButton(self.ntw_groupBox)
        self.ntw_unallocatedButton.setObjectName(u"ntw_unallocatedButton")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.ntw_unallocatedButton)


        self.gridLayout.addWidget(self.ntw_groupBox, 0, 0, 1, 2)

        NewTypeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(NewTypeWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        NewTypeWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(NewTypeWindow)
        self.statusbar.setObjectName(u"statusbar")
        NewTypeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewTypeWindow)

        QMetaObject.connectSlotsByName(NewTypeWindow)
    # setupUi

    def retranslateUi(self, NewTypeWindow):
        NewTypeWindow.setWindowTitle(QCoreApplication.translate("NewTypeWindow", u"Disk Imager", None))
        self.ntw_backButton.setText(QCoreApplication.translate("NewTypeWindow", u"Back", None))
        self.ntw_nextButton.setText(QCoreApplication.translate("NewTypeWindow", u"Next", None))
        self.ntw_finishButton.setText(QCoreApplication.translate("NewTypeWindow", u"Finish", None))
        self.ntw_cancelButton.setText(QCoreApplication.translate("NewTypeWindow", u"Cancel", None))
        self.ntw_groupBox.setTitle(QCoreApplication.translate("NewTypeWindow", u"Select Type of Data Source", None))
        self.ntw_diskImageButton.setText(QCoreApplication.translate("NewTypeWindow", u"Disk Image", None))
        self.ntw_localDiskButton.setText(QCoreApplication.translate("NewTypeWindow", u"Local Disk", None))
        self.ntw_logicalFileButton.setText(QCoreApplication.translate("NewTypeWindow", u"Logical Files", None))
        self.ntw_unallocatedButton.setText(QCoreApplication.translate("NewTypeWindow", u"Unallocated Space Image File", None))
    # retranslateUi

