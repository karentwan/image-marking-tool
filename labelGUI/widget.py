# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from labelGUI.model import ImageShow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        # self.img_show = QtWidgets.QLabel(self.centralwidget)
        self.img_show = ImageShow(self.centralwidget)
        self.img_show.setMinimumSize(QtCore.QSize(600, 600))
        # self.img_show.setMaximumSize(QtCore.QSize(1280, 1280))
        self.img_show.setObjectName("img_show")
        self.verticalLayout.addWidget(self.img_show)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.savebtn = QtWidgets.QPushButton(self.centralwidget)
        self.savebtn.setObjectName("savebtn")
        self.horizontalLayout.addWidget(self.savebtn)
        self.previousbtn = QtWidgets.QPushButton(self.centralwidget)
        self.previousbtn.setObjectName("previousbtn")
        self.horizontalLayout.addWidget(self.previousbtn)
        self.nextbtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextbtn.setObjectName("nextbtn")
        self.horizontalLayout.addWidget(self.nextbtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.opendirbtn = QtWidgets.QPushButton(self.centralwidget)
        self.opendirbtn.setObjectName("opendirbtn")
        self.verticalLayout_2.addWidget(self.opendirbtn)
        self.setdefaultdirbtn = QtWidgets.QPushButton(self.centralwidget)
        self.setdefaultdirbtn.setObjectName("setdefaultdirbtn")
        self.verticalLayout_2.addWidget(self.setdefaultdirbtn)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1025, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片打标工具"))
        self.img_show.setText(_translate("MainWindow", "显示图片的区域"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.savebtn.setText(_translate("MainWindow", "保存TxT文件"))
        self.previousbtn.setText(_translate("MainWindow", "上一张"))
        self.nextbtn.setText(_translate("MainWindow", "下一张"))
        self.opendirbtn.setText(_translate("MainWindow", "打开文件夹"))
        self.setdefaultdirbtn.setText(_translate("MainWindow", "设置保存默认文件夹"))
