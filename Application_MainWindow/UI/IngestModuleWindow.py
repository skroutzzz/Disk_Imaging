# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IngestModuleWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_IngestModuleWindow(object):
    def setupUi(self, IngestModuleWindow):
        if not IngestModuleWindow.objectName():
            IngestModuleWindow.setObjectName(u"IngestModuleWindow")
        IngestModuleWindow.resize(800, 600)
        self.centralwidget = QWidget(IngestModuleWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.imw_groupBox = QGroupBox(self.centralwidget)
        self.imw_groupBox.setObjectName(u"imw_groupBox")
        self.formLayout = QFormLayout(self.imw_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.imw_md5Checkbox = QCheckBox(self.imw_groupBox)
        self.imw_md5Checkbox.setObjectName(u"imw_md5Checkbox")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.imw_md5Checkbox)

        self.imw_shaCheckbox = QCheckBox(self.imw_groupBox)
        self.imw_shaCheckbox.setObjectName(u"imw_shaCheckbox")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.imw_shaCheckbox)

        self.imw_verificationCheckbox = QCheckBox(self.imw_groupBox)
        self.imw_verificationCheckbox.setObjectName(u"imw_verificationCheckbox")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.imw_verificationCheckbox)

        self.imw_keywordCheckbox = QCheckBox(self.imw_groupBox)
        self.imw_keywordCheckbox.setObjectName(u"imw_keywordCheckbox")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.imw_keywordCheckbox)

        self.imw_interestingCheckbox = QCheckBox(self.imw_groupBox)
        self.imw_interestingCheckbox.setObjectName(u"imw_interestingCheckbox")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.imw_interestingCheckbox)


        self.gridLayout.addWidget(self.imw_groupBox, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.imw_backButton = QPushButton(self.centralwidget)
        self.imw_backButton.setObjectName(u"imw_backButton")

        self.horizontalLayout.addWidget(self.imw_backButton)

        self.imw_nextButton = QPushButton(self.centralwidget)
        self.imw_nextButton.setObjectName(u"imw_nextButton")

        self.horizontalLayout.addWidget(self.imw_nextButton)

        self.imw_finishButton = QPushButton(self.centralwidget)
        self.imw_finishButton.setObjectName(u"imw_finishButton")

        self.horizontalLayout.addWidget(self.imw_finishButton)

        self.imw_cancelButton = QPushButton(self.centralwidget)
        self.imw_cancelButton.setObjectName(u"imw_cancelButton")

        self.horizontalLayout.addWidget(self.imw_cancelButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        IngestModuleWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(IngestModuleWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        IngestModuleWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(IngestModuleWindow)
        self.statusbar.setObjectName(u"statusbar")
        IngestModuleWindow.setStatusBar(self.statusbar)

        self.retranslateUi(IngestModuleWindow)

        QMetaObject.connectSlotsByName(IngestModuleWindow)
    # setupUi

    def retranslateUi(self, IngestModuleWindow):
        IngestModuleWindow.setWindowTitle(QCoreApplication.translate("IngestModuleWindow", u"Disk Imager", None))
        self.imw_groupBox.setTitle(QCoreApplication.translate("IngestModuleWindow", u"Select Modules", None))
        self.imw_md5Checkbox.setText(QCoreApplication.translate("IngestModuleWindow", u"Calculate MD5", None))
        self.imw_shaCheckbox.setText(QCoreApplication.translate("IngestModuleWindow", u"Calculate SHA-256", None))
        self.imw_verificationCheckbox.setText(QCoreApplication.translate("IngestModuleWindow", u"Verify image after acquisition for verification", None))
        self.imw_keywordCheckbox.setText(QCoreApplication.translate("IngestModuleWindow", u"Keyword Search", None))
        self.imw_interestingCheckbox.setText(QCoreApplication.translate("IngestModuleWindow", u"Interesting Files Identifier", None))
        self.imw_backButton.setText(QCoreApplication.translate("IngestModuleWindow", u"Back", None))
        self.imw_nextButton.setText(QCoreApplication.translate("IngestModuleWindow", u"Next", None))
        self.imw_finishButton.setText(QCoreApplication.translate("IngestModuleWindow", u"Finish", None))
        self.imw_cancelButton.setText(QCoreApplication.translate("IngestModuleWindow", u"Cancel", None))
    # retranslateUi

