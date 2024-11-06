# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CaseInfoWindow.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

class Ui_CaseInfoWindow(object):
    def setupUi(self, CaseInfoWindow):
        if not CaseInfoWindow.objectName():
            CaseInfoWindow.setObjectName(u"CaseInfoWindow")
        CaseInfoWindow.resize(800, 600)
        self.centralwidget = QWidget(CaseInfoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ciw_groupBox = QGroupBox(self.centralwidget)
        self.ciw_groupBox.setObjectName(u"ciw_groupBox")
        self.formLayout = QFormLayout(self.ciw_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.ciw_caseNameLabel = QLabel(self.ciw_groupBox)
        self.ciw_caseNameLabel.setObjectName(u"ciw_caseNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.ciw_caseNameLabel)

        self.ciw_caseNameEdit = QLineEdit(self.ciw_groupBox)
        self.ciw_caseNameEdit.setObjectName(u"ciw_caseNameEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ciw_caseNameEdit)

        self.ciw_baseLabel = QLabel(self.ciw_groupBox)
        self.ciw_baseLabel.setObjectName(u"ciw_baseLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.ciw_baseLabel)

        self.ciw_baseEdit = QLineEdit(self.ciw_groupBox)
        self.ciw_baseEdit.setObjectName(u"ciw_baseEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ciw_baseEdit)

        self.ciw_browseButton = QPushButton(self.ciw_groupBox)
        self.ciw_browseButton.setObjectName(u"ciw_browseButton")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ciw_browseButton)

        self.label_3 = QLabel(self.ciw_groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.ciw_groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_3)

        self.ciw_examinerNameLabel = QLabel(self.ciw_groupBox)
        self.ciw_examinerNameLabel.setObjectName(u"ciw_examinerNameLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.ciw_examinerNameLabel)

        self.ciw_examinerNameEdit = QLineEdit(self.ciw_groupBox)
        self.ciw_examinerNameEdit.setObjectName(u"ciw_examinerNameEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.ciw_examinerNameEdit)

        self.ciw_examinerPhoneLabel = QLabel(self.ciw_groupBox)
        self.ciw_examinerPhoneLabel.setObjectName(u"ciw_examinerPhoneLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.ciw_examinerPhoneLabel)

        self.ciw_examinerPhoneEdit = QLineEdit(self.ciw_groupBox)
        self.ciw_examinerPhoneEdit.setObjectName(u"ciw_examinerPhoneEdit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.ciw_examinerPhoneEdit)

        self.ciw_examinerEmailLabel = QLabel(self.ciw_groupBox)
        self.ciw_examinerEmailLabel.setObjectName(u"ciw_examinerEmailLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.ciw_examinerEmailLabel)

        self.ciw_examinerEmailEdit = QLineEdit(self.ciw_groupBox)
        self.ciw_examinerEmailEdit.setObjectName(u"ciw_examinerEmailEdit")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.ciw_examinerEmailEdit)

        self.ciw_notesLabel = QLabel(self.ciw_groupBox)
        self.ciw_notesLabel.setObjectName(u"ciw_notesLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.ciw_notesLabel)

        self.ciw_notesEdit = QLineEdit(self.ciw_groupBox)
        self.ciw_notesEdit.setObjectName(u"ciw_notesEdit")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.ciw_notesEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(9, QFormLayout.FieldRole, self.verticalSpacer_2)


        self.gridLayout.addWidget(self.ciw_groupBox, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ciw_backButton = QPushButton(self.centralwidget)
        self.ciw_backButton.setObjectName(u"ciw_backButton")

        self.horizontalLayout.addWidget(self.ciw_backButton)

        self.ciw_nextButton = QPushButton(self.centralwidget)
        self.ciw_nextButton.setObjectName(u"ciw_nextButton")

        self.horizontalLayout.addWidget(self.ciw_nextButton)

        self.ciw_finishButton = QPushButton(self.centralwidget)
        self.ciw_finishButton.setObjectName(u"ciw_finishButton")

        self.horizontalLayout.addWidget(self.ciw_finishButton)

        self.ciw_cancelButton = QPushButton(self.centralwidget)
        self.ciw_cancelButton.setObjectName(u"ciw_cancelButton")

        self.horizontalLayout.addWidget(self.ciw_cancelButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        CaseInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CaseInfoWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        CaseInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CaseInfoWindow)
        self.statusbar.setObjectName(u"statusbar")
        CaseInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CaseInfoWindow)

        QMetaObject.connectSlotsByName(CaseInfoWindow)
    # setupUi

    def retranslateUi(self, CaseInfoWindow):
        CaseInfoWindow.setWindowTitle(QCoreApplication.translate("CaseInfoWindow", u"Disk Imager", None))
        self.ciw_groupBox.setTitle(QCoreApplication.translate("CaseInfoWindow", u"GroupBox", None))
        self.ciw_caseNameLabel.setText(QCoreApplication.translate("CaseInfoWindow", u"Case Name:", None))
        self.ciw_baseLabel.setText(QCoreApplication.translate("CaseInfoWindow", u"Base Directory:", None))
        self.ciw_browseButton.setText(QCoreApplication.translate("CaseInfoWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("CaseInfoWindow", u"Case Number:", None))
        self.ciw_examinerNameLabel.setText(QCoreApplication.translate("CaseInfoWindow", u"Examiner Name:", None))
        self.ciw_examinerPhoneLabel.setText(QCoreApplication.translate("CaseInfoWindow", u"Examiner Phone:", None))
        self.ciw_examinerEmailLabel.setText(QCoreApplication.translate("CaseInfoWindow", u"Examiner Email:", None))
        self.ciw_notesLabel.setText(QCoreApplication.translate("CaseInfoWindow", u"Notes:", None))
        self.ciw_backButton.setText(QCoreApplication.translate("CaseInfoWindow", u"Back", None))
        self.ciw_nextButton.setText(QCoreApplication.translate("CaseInfoWindow", u"Next", None))
        self.ciw_finishButton.setText(QCoreApplication.translate("CaseInfoWindow", u"Finish", None))
        self.ciw_cancelButton.setText(QCoreApplication.translate("CaseInfoWindow", u"Cancel", None))
    # retranslateUi

