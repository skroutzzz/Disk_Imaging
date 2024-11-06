# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgressWindow.ui'
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
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QWidget)

class Ui_ProgresWindow(object):
    def setupUi(self, ProgresWindow):
        if not ProgresWindow.objectName():
            ProgresWindow.setObjectName(u"ProgresWindow")
        ProgresWindow.resize(800, 600)
        self.centralwidget = QWidget(ProgresWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pw_groupBox = QGroupBox(self.centralwidget)
        self.pw_groupBox.setObjectName(u"pw_groupBox")
        self.formLayout = QFormLayout(self.pw_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.pw_label = QLabel(self.pw_groupBox)
        self.pw_label.setObjectName(u"pw_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pw_label)

        self.pw_progressBar = QProgressBar(self.pw_groupBox)
        self.pw_progressBar.setObjectName(u"pw_progressBar")
        self.pw_progressBar.setValue(24)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.pw_progressBar)

        self.pw_textEdit = QTextEdit(self.pw_groupBox)
        self.pw_textEdit.setObjectName(u"pw_textEdit")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.pw_textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer)

        self.pw_beginButton = QPushButton(self.pw_groupBox)
        self.pw_beginButton.setObjectName(u"pw_beginButton")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.pw_beginButton)


        self.gridLayout.addWidget(self.pw_groupBox, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pw_backButton = QPushButton(self.centralwidget)
        self.pw_backButton.setObjectName(u"pw_backButton")

        self.horizontalLayout.addWidget(self.pw_backButton)

        self.pw_nextButton = QPushButton(self.centralwidget)
        self.pw_nextButton.setObjectName(u"pw_nextButton")

        self.horizontalLayout.addWidget(self.pw_nextButton)

        self.pw_finishButton = QPushButton(self.centralwidget)
        self.pw_finishButton.setObjectName(u"pw_finishButton")

        self.horizontalLayout.addWidget(self.pw_finishButton)

        self.pw_cancelButton = QPushButton(self.centralwidget)
        self.pw_cancelButton.setObjectName(u"pw_cancelButton")

        self.horizontalLayout.addWidget(self.pw_cancelButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        ProgresWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ProgresWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        ProgresWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ProgresWindow)
        self.statusbar.setObjectName(u"statusbar")
        ProgresWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ProgresWindow)

        QMetaObject.connectSlotsByName(ProgresWindow)
    # setupUi

    def retranslateUi(self, ProgresWindow):
        ProgresWindow.setWindowTitle(QCoreApplication.translate("ProgresWindow", u"Disk Imager", None))
        self.pw_groupBox.setTitle(QCoreApplication.translate("ProgresWindow", u"GroupBox", None))
        self.pw_label.setText(QCoreApplication.translate("ProgresWindow", u"Processing data source and adding it to local database. This may take a while...", None))
        self.pw_beginButton.setText(QCoreApplication.translate("ProgresWindow", u"Begin", None))
        self.pw_backButton.setText(QCoreApplication.translate("ProgresWindow", u"Back", None))
        self.pw_nextButton.setText(QCoreApplication.translate("ProgresWindow", u"Next", None))
        self.pw_finishButton.setText(QCoreApplication.translate("ProgresWindow", u"Finish", None))
        self.pw_cancelButton.setText(QCoreApplication.translate("ProgresWindow", u"Cancel", None))
    # retranslateUi

