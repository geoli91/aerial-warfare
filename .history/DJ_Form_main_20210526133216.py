'''
Description: 继承主窗体UI类，并实现相关操作
Author: DJ
Date: 2021-05-26 12:38:48
LastEditTime: 2021-05-26 13:32:12
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from resources.UI.Ui_start_window import Ui_MainWindowPlane

class FormMain(QtWidgets.QMainWindow,Ui_MainWindowPlane):
    
    '''
    @description: 初始化主窗体类
    @param  {*}
    @return {*}
    @param {*} self
    @param {*} parent
    '''    
    def __init__(self,parent=None):
        super(FormMain,self).__init__(parent)
        self.setupUi(self)

        # 绑定信号与槽函数
        self.bound_func()

    '''
    @description: 绑定信号与槽函数
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def bound_func(self):
        self.pushButton_start_game.clicked.connect(self.start_game)

    '''
    @description: 开始游戏
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def start_game(self):
        print("start")
        self.label_start_img.hide()
        self.label_start_note.hide()
        self.pushButton_start_game.hide()
        self.g
        