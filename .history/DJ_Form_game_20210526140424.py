'''
Description: 继承游戏窗口UI类，并实现相关操作
Author: DJ
Date: 2021-05-26 13:39:58
LastEditTime: 2021-05-26 14:04:23
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from resources.UI.Ui_game_Form import Ui_DialogGame

class FormGame(QtWidgets.QDialog,Ui_DialogGame):
    '''
    @description: 初始化游戏窗口类
    @param  {*}
    @return {*}
    @param {*} self
    @param {*} parent
    '''    
    def __init__(self,parent=None):
        super(FormGame,self).__init__(parent)
        self.setupUi(self)

        # 初始化游戏
        self.init_game()

        
        # 尝试做一些操作；测试完成后需删除
        self.try_do()
    # 尝试做一些操作，测试完成后需删除
    def try_do(self):
        self.draw_img()
    '''
    @description: 初始化游戏
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def init_game(self):
        # 为 graphicsView 创建 scene 并设置为当前 scene
        self.scene=QGraphicsScene()
        self.graphicsView_game.setScene(self.scene)
        # 关闭滑动条
        self.graphicsView_game.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView_game.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def draw_img(self):
        path_img=r'resources\photo\background4.jpg'
        
        pixmap=QPixmap(path_img)# .scaled(self.graphicsView.geometry().width(),self.graphicsView.geometry().height(),Qt.KeepAspectRatio)

        self.item_map=QGraphicsPixmapItem(pixmap)
        
        # self.scene.view=self.graphicsView
        # scene.addItem(item)
        self.scene.addPixmap(pixmap)
        # self.scene.addItem(self.item_map)
        

        self.graphicsView_game.show()

            