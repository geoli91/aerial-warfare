# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\DJ_programming\DJ_程序设计方法学作业\DJ_打飞机\resources\UI\start_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowPlane(object):
    def setupUi(self, MainWindowPlane):
        MainWindowPlane.setObjectName("MainWindowPlane")
        MainWindowPlane.resize(528, 828)
        self.centralwidget = QtWidgets.QWidget(MainWindowPlane)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/start/resources/photo/background1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        MainWindowPlane.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowPlane)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 23))
        self.menubar.setObjectName("menubar")
        MainWindowPlane.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowPlane)
        self.statusbar.setObjectName("statusbar")
        MainWindowPlane.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowPlane)
        QtCore.QMetaObject.connectSlotsByName(MainWindowPlane)

    def retranslateUi(self, MainWindowPlane):
        _translate = QtCore.QCoreApplication.translate
        MainWindowPlane.setWindowTitle(_translate("MainWindowPlane", "飞机大战"))
        self.pushButton.setText(_translate("MainWindowPlane", "开    始    游    戏"))
        self.label_2.setText(_translate("MainWindowPlane", "使用说明：\n"
"点击开始游戏按钮开始游戏\n"
"移动：使用 W S A D 按钮控制飞机 ↑ ↓ ← → 移动\n"
"攻击：使用 J 发射单向子弹 K 发射多向子弹\n"
"血量：游戏中存在血量限制，可以通过吃血包的方式恢复自身血量"))
import img_rc
