# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectDataWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

class Ui_SelectDataWindow(object):
    def setupUi(self, SelectDataWindow):
        if not SelectDataWindow.objectName():
            SelectDataWindow.setObjectName(u"SelectDataWindow")
        SelectDataWindow.resize(800, 600)
        self.centralwidget = QWidget(SelectDataWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sdw_backButton = QPushButton(self.centralwidget)
        self.sdw_backButton.setObjectName(u"sdw_backButton")

        self.horizontalLayout.addWidget(self.sdw_backButton)

        self.sdw_nextButton = QPushButton(self.centralwidget)
        self.sdw_nextButton.setObjectName(u"sdw_nextButton")

        self.horizontalLayout.addWidget(self.sdw_nextButton)

        self.sdw_finishButton = QPushButton(self.centralwidget)
        self.sdw_finishButton.setObjectName(u"sdw_finishButton")

        self.horizontalLayout.addWidget(self.sdw_finishButton)

        self.sdw_cancelButton = QPushButton(self.centralwidget)
        self.sdw_cancelButton.setObjectName(u"sdw_cancelButton")

        self.horizontalLayout.addWidget(self.sdw_cancelButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.sdw_groupBox = QGroupBox(self.centralwidget)
        self.sdw_groupBox.setObjectName(u"sdw_groupBox")
        self.formLayout = QFormLayout(self.sdw_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.verticalSpacer)

        self.sdw_browseLabel = QLabel(self.sdw_groupBox)
        self.sdw_browseLabel.setObjectName(u"sdw_browseLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.sdw_browseLabel)

        self.sdw_comboBox = QComboBox(self.sdw_groupBox)
        self.sdw_comboBox.setObjectName(u"sdw_comboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sdw_comboBox)


        self.gridLayout.addWidget(self.sdw_groupBox, 0, 0, 1, 2)

        SelectDataWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SelectDataWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        SelectDataWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SelectDataWindow)
        self.statusbar.setObjectName(u"statusbar")
        SelectDataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SelectDataWindow)

        QMetaObject.connectSlotsByName(SelectDataWindow)
    # setupUi

    def retranslateUi(self, SelectDataWindow):
        SelectDataWindow.setWindowTitle(QCoreApplication.translate("SelectDataWindow", u"Disk Imager", None))
        self.sdw_backButton.setText(QCoreApplication.translate("SelectDataWindow", u"Back", None))
        self.sdw_nextButton.setText(QCoreApplication.translate("SelectDataWindow", u"Next", None))
        self.sdw_finishButton.setText(QCoreApplication.translate("SelectDataWindow", u"Finish", None))
        self.sdw_cancelButton.setText(QCoreApplication.translate("SelectDataWindow", u"Cancel", None))
        self.sdw_groupBox.setTitle(QCoreApplication.translate("SelectDataWindow", u"Select Data Source", None))
        self.sdw_browseLabel.setText(QCoreApplication.translate("SelectDataWindow", u"Browse for a device:", None))
    # retranslateUi

