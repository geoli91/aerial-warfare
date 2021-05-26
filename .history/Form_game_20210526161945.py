'''
Description: 继承游戏窗口UI类，并实现相关操作
Author: DJ
Date: 2021-05-26 13:39:58
LastEditTime: 2021-05-26 16:19:44
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from resources.UI.Ui_game_Form import Ui_Form
from background import BackGround
from gameControl import GameControl
from planes import PlanePlayer,PlaneEnemy

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

        
    '''
    @description: 初始化游戏
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def init_game(self):
        # 实例化背景类对象
        self.background=BackGround(5,self.height())
        # 实例化玩家飞机对象
        self.plane_palyer=None
        # 创建空敌机列表
        self.list_enemy=[]
        # 创建空子弹列表
        self.list_bullet=[]
        # 获取玩家名称和玩家图标文件路径
        self.str_name_player='李华'
        self.path_player_img=None
        # 获取背景图标文件路径列表
        self.list_background_img_path=[r'resources\photo\background1.jpg',r'resources\photo\background2.jpg',r'resources\photo\background3.jpg',r'resources\photo\background4.jpg']
        # 实例化游戏控制对象
        self.gameControl=GameControl(self.background,self.plane_palyer,self.list_enemy,self.list_enemy,self.list_bullet,self.str_name_player,self.path_player_img,self.list_background_img_path)
        # 创建关卡
        self.gameControl.create_stage()
        pass



    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        # 绘制背景
        painter.drawPixmap(self.background.x,self.background.y, self.background.pixmap)
        # 绘制我方飞机
        if isinstance(self.plane_palyer,PlanePlayer):
            painter.drawPixmap(self.plane_palyer.x,self.plane_palyer.y, self.background.pixmap)
        # 依据敌机列表绘制敌机

        # 依据子弹列表绘制子弹

        # 绘制左上角状态，包括我方驾驶员图标、血条、蓝条、玩家名称、关卡数



        
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

        path_img_2=r'resources\photo\fighterRed.png'
        pixmap_2=QPixmap(path_img_2)
        painter.drawPixmap(100,200, pixmap_2)


        return super().paintEvent(a0)


    # 尝试做一些操作，测试完成后需删除
    def try_do(self):
        # self.draw_img()
        # self.pushButton_1.clicked.connect(self.test)
        # self.pushButton.clicked.connect(self.test)
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

            