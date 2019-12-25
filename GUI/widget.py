# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 836)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_img_widget = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_img_widget.sizePolicy().hasHeightForWidth())
        self.show_img_widget.setSizePolicy(sizePolicy)
        self.show_img_widget.setMinimumSize(QtCore.QSize(600, 600))
        self.show_img_widget.setMaximumSize(QtCore.QSize(1280, 1280))
        self.show_img_widget.setObjectName("show_img_widget")
        self.verticalLayout.addWidget(self.show_img_widget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectbtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectbtn.setObjectName("selectbtn")
        self.horizontalLayout.addWidget(self.selectbtn)
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)
        self.previous_btn = QtWidgets.QPushButton(self.centralwidget)
        self.previous_btn.setObjectName("previous_btn")
        self.horizontalLayout.addWidget(self.previous_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.open_dirbtn = QtWidgets.QPushButton(self.centralwidget)
        self.open_dirbtn.setObjectName("open_dirbtn")
        self.verticalLayout_2.addWidget(self.open_dirbtn)
        self.set_default_dirbtn = QtWidgets.QPushButton(self.centralwidget)
        self.set_default_dirbtn.setObjectName("set_default_dirbtn")
        self.verticalLayout_2.addWidget(self.set_default_dirbtn)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.show_img_widget.setText(_translate("MainWindow", "show_img"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.selectbtn.setText(_translate("MainWindow", "选中"))
        self.next_btn.setText(_translate("MainWindow", "下一张"))
        self.previous_btn.setText(_translate("MainWindow", "上一张"))
        self.open_dirbtn.setText(_translate("MainWindow", "打开文件夹"))
        self.set_default_dirbtn.setText(_translate("MainWindow", "设置保存默认文件夹"))
