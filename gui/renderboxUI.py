# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'renderboxUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.treeWidget = QTreeWidget(self.frame)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout_2.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RenderBOX AI", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Render Time", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Export Time", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"File Size", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Type", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"RenderBox - Artificial Inteligence & Machine learning", None))
    # retranslateUi

