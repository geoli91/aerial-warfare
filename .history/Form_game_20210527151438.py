'''
Description: 继承游戏窗口UI类，并实现相关操作
Author: DJ
Date: 2021-05-26 13:39:58
LastEditTime: 2021-05-27 15:14:38
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from resources.UI.Ui_game_Form import Ui_FormGame
from background import BackGround
from gameControl import GameControl
from planes import PlanePlayer,PlaneEnemy
from bullets import Bullet

class FormGame(QtWidgets.QDialog,Ui_FormGame):
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
        
    '''
    @description: 初始化游戏
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def init_game(self):
        self.bool_game_over=False # 指示游戏是否结束
        path_img_gameover=r'resources\photo\game_over.png'
        self.pixmap_gameover=QPixmap(path_img_gameover).scaledToWidth(self.width()*0.8)
        # 设置玩家名称和玩家头像文件路径
        self.str_name_player='冰冰'
        self.path_player_img=r'resources\photo\imgHeadSheep.png'
        # 实例化背景类对象
        self.background=BackGround(5,self.height())
        # 创建空敌机列表
        self.list_enemy=[]
        # 创建空子弹列表
        self.list_bullet=[]
        # 实例化玩家飞机对象
        self.plane_palyer=PlanePlayer('player','player',self.list_bullet,self.width(),self.height())
        self.plane_palyer.sigmal_game_over.connect(self.game_over)
        # 获取背景图标文件路径列表
        self.list_background_img_path=[r'resources\photo\background1.jpg',r'resources\photo\background2.jpg',r'resources\photo\background3.jpg',r'resources\photo\background4.jpg']
        # 实例化游戏控制对象
        self.gameControl=GameControl(self.background,self.plane_palyer,self.list_enemy,self.list_bullet,self.str_name_player,self.path_player_img,self.list_background_img_path,self.width(),self.height())
        # 创建关卡
        self.gameControl.create_stage()
        # 创建定时器，定时刷新
        self.qtimer_update=QTimer() # 创建 QTimer 对象
        self.qtimer_update.start(20) # 开始定时，传入参数为时间间隔，单位为 毫秒
        self.qtimer_update.timeout.connect(self.update)
     
    
    '''
    @description: 重写绘图事件
    @param  {*}
    @return {*}
    @param {*} self
    @param {QtGui} a0
    '''    
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        # 实例化画图对象
        painter = QPainter(self)
        # 绘制背景
        painter.drawPixmap(self.background.x,self.background.y, self.background.pixmap)
        painter.drawPixmap(self.background.x,self.background.y-self.height(), self.background.pixmap)
        # 绘制我方飞机
        if isinstance(self.plane_palyer,PlanePlayer):
            painter.drawPixmap(self.plane_palyer.x,self.plane_palyer.y, self.plane_palyer.pixmap)
        # 依据敌机列表绘制敌机
        for plane_enemy in self.list_enemy:
            if isinstance(plane_enemy,PlaneEnemy):
                painter.drawPixmap(plane_enemy.x,plane_enemy.y, plane_enemy.pixmap)
        # 依据子弹列表绘制子弹
        for bullet in self.list_bullet:
            if isinstance(bullet,Bullet):
                painter.drawPixmap(bullet.x,bullet.y, bullet.pixmap)
        """绘制左上角状态，包括我方驾驶员图标、血条、蓝条、玩家名称、关卡数"""
        # 绘制驾驶员图标
        pixmap_player_img=QPixmap(self.path_player_img)
        painter.drawPixmap(10,10,pixmap_player_img)
        # 绘制血条
        painter.drawRect(10,90,102,10)
        painter.fillRect(11,91,self.plane_palyer.HP,9,QColor(255,0,0))
        # 绘制蓝条
        painter.drawRect(10,110,102,10)
        painter.fillRect(11,111,100,9,QColor(0,0,255))
        # 绘制玩家名称、得分和关卡数
        # 设置字体
        font=QFont()
        font.setFamily("宋体")
        font.setBold(True)
        font.setPointSize(9)
        painter.setFont(font)
        painter.drawText(10,135,f'Player:{self.str_name_player}')
        painter.drawText(10,150,f'Score:{self.gameControl.int_score}')
        painter.drawText(10,165,f'Stage:{self.gameControl.int_stage}')
        if self.bool_game_over:
            painter.drawPixmap(20,self.height()-self.pixmap_gameover.height(),self.pixmap_gameover)
        return super().paintEvent(a0)

 

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        dict_key_func={
            Qt.Key_A:self.plane_palyer.move_left, 
            Qt.Key_D:self.plane_palyer.move_right,
            Qt.Key_W:self.plane_palyer.move_up,
            Qt.Key_S:self.plane_palyer.move_low,
            Qt.Key_J:self.plane_palyer.shot,
            }
        func_key=lambda key:dict_key_func.get(key,lambda :None)()
        func_key(a0.key())
        # 刷新显示
        self.update()

        return super().keyPressEvent(a0)


    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        self.plane_palyer.plane_flow='general'
        # 刷新显示
        self.update()
        return super().keyReleaseEvent(a0)

    def game_over(self):
        # 所有的定时器都停止
        for enemy in self.list_enemy:
            enemy.qtimer_move_nenmy.stop()
            enemy.qtimer_shot.stop()
        for bullet in self.list_bullet:
            bullet.qtimer.stop()
        self.gameControl.qtimer_create_enemy.stop()
        self.gameControl.qtimer_crack_detect.stop()
        self.gameControl.qtimer_move_bg.stop()
        # 
        # 设置游戏状态为game_over
        self.bool_game_over=True
        
        pass
