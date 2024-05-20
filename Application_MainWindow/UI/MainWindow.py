# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QTextEdit, QTreeView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew_Case = QAction(MainWindow)
        self.actionNew_Case.setObjectName(u"actionNew_Case")
        self.actionOpen_Case = QAction(MainWindow)
        self.actionOpen_Case.setObjectName(u"actionOpen_Case")
        self.actionClose_Case = QAction(MainWindow)
        self.actionClose_Case.setObjectName(u"actionClose_Case")
        self.actionAdd_Data_Source = QAction(MainWindow)
        self.actionAdd_Data_Source.setObjectName(u"actionAdd_Data_Source")
        self.actionRemove_Data_Source = QAction(MainWindow)
        self.actionRemove_Data_Source.setObjectName(u"actionRemove_Data_Source")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.mw_groupBox = QGroupBox(self.centralwidget)
        self.mw_groupBox.setObjectName(u"mw_groupBox")
        self.gridLayout_2 = QGridLayout(self.mw_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mw_newCaseButton = QPushButton(self.mw_groupBox)
        self.mw_newCaseButton.setObjectName(u"mw_newCaseButton")

        self.horizontalLayout.addWidget(self.mw_newCaseButton)

        self.mw_openCaseButton = QPushButton(self.mw_groupBox)
        self.mw_openCaseButton.setObjectName(u"mw_openCaseButton")

        self.horizontalLayout.addWidget(self.mw_openCaseButton)

        self.mw_addDataSourceButton = QPushButton(self.mw_groupBox)
        self.mw_addDataSourceButton.setObjectName(u"mw_addDataSourceButton")

        self.horizontalLayout.addWidget(self.mw_addDataSourceButton)

        self.pushButton = QPushButton(self.mw_groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.mw_searchBarEdit = QLineEdit(self.mw_groupBox)
        self.mw_searchBarEdit.setObjectName(u"mw_searchBarEdit")

        self.horizontalLayout.addWidget(self.mw_searchBarEdit)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 5)

        self.mw_textButton = QPushButton(self.mw_groupBox)
        self.mw_textButton.setObjectName(u"mw_textButton")

        self.gridLayout_2.addWidget(self.mw_textButton, 3, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 1, 1, 1)

        self.mw_mediaButton = QPushButton(self.mw_groupBox)
        self.mw_mediaButton.setObjectName(u"mw_mediaButton")

        self.gridLayout_2.addWidget(self.mw_mediaButton, 3, 3, 1, 1)

        self.mw_treeView = QTreeView(self.mw_groupBox)
        self.mw_treeView.setObjectName(u"mw_treeView")

        self.gridLayout_2.addWidget(self.mw_treeView, 1, 0, 4, 1)

        self.mw_hexButton = QPushButton(self.mw_groupBox)
        self.mw_hexButton.setObjectName(u"mw_hexButton")

        self.gridLayout_2.addWidget(self.mw_hexButton, 3, 1, 1, 1)

        self.mw_tableView = QTableView(self.mw_groupBox)
        self.mw_tableView.setObjectName(u"mw_tableView")

        self.gridLayout_2.addWidget(self.mw_tableView, 1, 1, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.mw_textEdit = QTextEdit(self.mw_groupBox)
        self.mw_textEdit.setObjectName(u"mw_textEdit")

        self.gridLayout_2.addWidget(self.mw_textEdit, 4, 1, 1, 4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 4, 1, 1)

        self.pushButton_8 = QPushButton(self.mw_groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 3, 4, 1, 1)


        self.horizontalLayout_4.addWidget(self.mw_groupBox)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.mw_menuFile = QMenu(self.menubar)
        self.mw_menuFile.setObjectName(u"mw_menuFile")
        self.mw_menuView = QMenu(self.menubar)
        self.mw_menuView.setObjectName(u"mw_menuView")
        self.mw_menuTools = QMenu(self.menubar)
        self.mw_menuTools.setObjectName(u"mw_menuTools")
        self.mw_menuHelp = QMenu(self.menubar)
        self.mw_menuHelp.setObjectName(u"mw_menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.mw_menuFile.menuAction())
        self.menubar.addAction(self.mw_menuView.menuAction())
        self.menubar.addAction(self.mw_menuTools.menuAction())
        self.menubar.addAction(self.mw_menuHelp.menuAction())
        self.mw_menuFile.addAction(self.actionNew_Case)
        self.mw_menuFile.addAction(self.actionOpen_Case)
        self.mw_menuFile.addAction(self.actionClose_Case)
        self.mw_menuFile.addAction(self.actionAdd_Data_Source)
        self.mw_menuFile.addAction(self.actionRemove_Data_Source)
        self.mw_menuFile.addSeparator()
        self.mw_menuFile.addSeparator()
        self.mw_menuFile.addAction(self.actionExit)
        self.mw_menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Disk Imager", None))
        self.actionNew_Case.setText(QCoreApplication.translate("MainWindow", u"New Case", None))
        self.actionOpen_Case.setText(QCoreApplication.translate("MainWindow", u"Open Case", None))
        self.actionClose_Case.setText(QCoreApplication.translate("MainWindow", u"Close Case", None))
        self.actionAdd_Data_Source.setText(QCoreApplication.translate("MainWindow", u"Add Data Source", None))
        self.actionRemove_Data_Source.setText(QCoreApplication.translate("MainWindow", u"Remove Data Source", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.mw_groupBox.setTitle("")
        self.mw_newCaseButton.setText(QCoreApplication.translate("MainWindow", u"New Case", None))
        self.mw_openCaseButton.setText(QCoreApplication.translate("MainWindow", u"Open Case", None))
        self.mw_addDataSourceButton.setText(QCoreApplication.translate("MainWindow", u"Add Data Source", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PlaceHolder", None))
        self.mw_searchBarEdit.setText(QCoreApplication.translate("MainWindow", u"Keyword Search", None))
        self.mw_textButton.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.mw_mediaButton.setText(QCoreApplication.translate("MainWindow", u"Media", None))
        self.mw_hexButton.setText(QCoreApplication.translate("MainWindow", u"Hex", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PlaceHolder", None))
        self.mw_menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.mw_menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.mw_menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.mw_menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

