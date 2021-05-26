'''
Description: 继承游戏窗口UI类，并实现相关操作
Author: DJ
Date: 2021-05-26 13:39:58
LastEditTime: 2021-05-26 14:41:09
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from resources.UI.Ui_game_Form_2 import Ui_Form

class FormGame(QtWidgets.QDialog,Ui_Form):
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

        # TODO:测试完成后删除
        # 尝试做一些操作；测试完成后需删除
        self.try_do()
        
    # 尝试做一些操作，测试完成后需删除
    def try_do(self):
        # self.draw_img()
        self.pushButton_1.clicked.connect(self.test)
        # self.pushButton.clicked.connect(self.test)


    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        # 画图必须放到 paintEvent 中去做，否则会抛出 “QWidget::paintEngine: Should no longer be called” 异常
        path_img=r'resources\photo\background4.jpg'
        self.pixmap=QPixmap(path_img)# .scaled(self.graphicsView.geometry().width(),self.graphicsView.geometry().height(),Qt.KeepAspectRatio)
        # self.item_background=QGraphicsPixmapItem(pixmap)
        # # self.scene.view=self.graphicsView
        # # scene.addItem(item)
        # # self.scene.addPixmap(pixmap)
        # self.scene.addItem(self.item_background)
        # self.pushButton.clicked.connect(self.test)
        # self.graphicsView_game.show()
        painter = QPainter(self)
        painter.drawPixmap(self.x,self.y, self.pixmap)
        painter.drawPixmap(self.x,self.y-630, self.pixmap)

        return super().paintEvent(a0)
        
    '''
    @description: 初始化游戏
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def init_game(self):
        # # 为 graphicsView 创建 scene 并设置为当前 scene
        # self.scene=QGraphicsScene()
        # self.graphicsView_game.setScene(self.scene)
        # # 关闭滑动条
        # self.graphicsView_game.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.graphicsView_game.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.x,self.y=0,0

        pass

    def draw_img(self):
        path_img=r'resources\photo\background4.jpg'
        pixmap=QPixmap(path_img)# .scaled(self.graphicsView.geometry().width(),self.graphicsView.geometry().height(),Qt.KeepAspectRatio)
        # self.item_background=QGraphicsPixmapItem(pixmap)
        # # self.scene.view=self.graphicsView
        # # scene.addItem(item)
        # # self.scene.addPixmap(pixmap)
        # self.scene.addItem(self.item_background)
        # self.pushButton.clicked.connect(self.test)
        # self.graphicsView_game.show()
        painter = QPainter(self)
        painter.drawPixmap(0, 0, pixmap) 

    def test(self):
        # self.item_background.setY(self.item_background.y()+10)
        # self.item_background.setOffset(-100,-200)
        # self.pixmap.scaled(10,10)
        self.y+=20
        if self.y>630:
            self.y=0
        self.update()
        print(self.x,self.y)
        pass

            