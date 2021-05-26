'''
Description: 继承主窗体UI类，并实现相关操作
Author: DJ
Date: 2021-05-26 12:38:48
LastEditTime: 2021-05-26 14:32:36
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from resources.UI.Ui_start_window import Ui_MainWindowPlane
from DJ_Form_game import FormGame

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
        # 创建游戏窗口对象并显示
        # self.dialog_game=FormGame()
        from DJ_Form_game_2 import FormGame as FormGame_2
        self.dialog_game=FormGame_2()
        self.dialog_game.show()
        # 隐藏主窗口
        self.hide()
        