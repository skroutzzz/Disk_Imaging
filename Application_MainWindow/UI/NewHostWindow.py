# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewHostWindow.ui'
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
    QHBoxLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_NewDataSourceWindow(object):
    def setupUi(self, NewDataSourceWindow):
        if not NewDataSourceWindow.objectName():
            NewDataSourceWindow.setObjectName(u"NewDataSourceWindow")
        NewDataSourceWindow.resize(800, 600)
        self.centralwidget = QWidget(NewDataSourceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.nhw_generateNewButton = QRadioButton(self.groupBox)
        self.nhw_generateNewButton.setObjectName(u"nhw_generateNewButton")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nhw_generateNewButton)

        self.nhw_specifyNewButton = QRadioButton(self.groupBox)
        self.nhw_specifyNewButton.setObjectName(u"nhw_specifyNewButton")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nhw_specifyNewButton)

        self.nhw_specifyNewLine = QLineEdit(self.groupBox)
        self.nhw_specifyNewLine.setObjectName(u"nhw_specifyNewLine")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nhw_specifyNewLine)

        self.nhw_useExistingButton = QRadioButton(self.groupBox)
        self.nhw_useExistingButton.setObjectName(u"nhw_useExistingButton")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.nhw_useExistingButton)

        self.nhw_useExistingText = QTextEdit(self.groupBox)
        self.nhw_useExistingText.setObjectName(u"nhw_useExistingText")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.nhw_useExistingText)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nhw_backButton = QPushButton(self.groupBox)
        self.nhw_backButton.setObjectName(u"nhw_backButton")

        self.horizontalLayout.addWidget(self.nhw_backButton)

        self.nhw_NextButton = QPushButton(self.groupBox)
        self.nhw_NextButton.setObjectName(u"nhw_NextButton")

        self.horizontalLayout.addWidget(self.nhw_NextButton)

        self.nhw_finishButton = QPushButton(self.groupBox)
        self.nhw_finishButton.setObjectName(u"nhw_finishButton")

        self.horizontalLayout.addWidget(self.nhw_finishButton)

        self.nhw_cancelButton = QPushButton(self.groupBox)
        self.nhw_cancelButton.setObjectName(u"nhw_cancelButton")

        self.horizontalLayout.addWidget(self.nhw_cancelButton)


        self.formLayout.setLayout(9, QFormLayout.FieldRole, self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        NewDataSourceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(NewDataSourceWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        NewDataSourceWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(NewDataSourceWindow)
        self.statusbar.setObjectName(u"statusbar")
        NewDataSourceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewDataSourceWindow)

        QMetaObject.connectSlotsByName(NewDataSourceWindow)
    # setupUi

    def retranslateUi(self, NewDataSourceWindow):
        NewDataSourceWindow.setWindowTitle(QCoreApplication.translate("NewDataSourceWindow", u"Disk Imager", None))
        self.groupBox.setTitle(QCoreApplication.translate("NewDataSourceWindow", u"Select Host", None))
        self.nhw_generateNewButton.setText(QCoreApplication.translate("NewDataSourceWindow", u"Generate new host name based on data source name", None))
        self.nhw_specifyNewButton.setText(QCoreApplication.translate("NewDataSourceWindow", u"Specify new host name", None))
        self.nhw_useExistingButton.setText(QCoreApplication.translate("NewDataSourceWindow", u"Use Existing Host", None))
        self.nhw_backButton.setText(QCoreApplication.translate("NewDataSourceWindow", u"Back", None))
        self.nhw_NextButton.setText(QCoreApplication.translate("NewDataSourceWindow", u"Next", None))
        self.nhw_finishButton.setText(QCoreApplication.translate("NewDataSourceWindow", u"Finish", None))
        self.nhw_cancelButton.setText(QCoreApplication.translate("NewDataSourceWindow", u"Cancel", None))
    # retranslateUi

