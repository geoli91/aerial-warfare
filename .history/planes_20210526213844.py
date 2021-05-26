'''
Description: 飞机类，包括飞机的基类和继承基类的玩家飞机类和敌军飞机类
Author: DJ
Date: 2021-05-26 16:16:52
LastEditTime: 2021-05-26 21:38:42
LastEditors: DJ
'''
from bullets import Bullet
from PyQt5 import QtCore, QtGui, QtWidgets

'''
@description: 
@param  {*}
@return {*}
'''
class BasePlane():
    def __init__(self,class_plane,class_bulet,list_bullet,max_x,max_y) -> None:
        self.class_plane=class_plane
        self.class_bulet=class_bulet # 子弹类型，默认为 player 玩家的一般子弹，enemy 为地方子弹
        self.list_bullet=list_bullet
        self.max_x=max_x # 飞机能飞到的最大x
        self.max_y=max_y # 飞机能飞到的最大y
        # 设置一些默认属性
        self.pixmap=None #  飞机图标
        self.x=0 # 飞机位置x
        self.y=0 # 飞机位置y
        self.HP=0 # 飞机 HP
        self.MP=0 # 飞机 MP
        pass
    
    '''
    @description: 发射子弹
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def shot(self):
        # 实例化子弹对象并添加至子弹列表中
        bullet=Bullet(self.class_bulet)
        self.list_bullet.append(bullet)

    def move_left(self):
        if self.x>0:
            self.x-=1

    def move_right(self):
        if self.x<self.max_x:
            self.x+=1

    def move_up(self):
        if self.y>0:
            self.y-=1
            
    def move_low(self):
        if self.y<self.max_y:
            self.y+=1

'''
@description: 玩家飞机类
@param  {*}
@return {*}
'''
class PlanePlayer(BasePlane):
    def __init__(self,class_plane,class_bulet,list_bullet,max_x,max_y) -> None:
        # 重写了子类的 __init__ 方法，如果还希望继承父类的 __init__ 方案，可以使用 super 关键字，
        super(PlanePlayer,self).__init__(class_plane,class_bulet,list_bullet,max_x,max_y)
        # 初始化飞机图标
        path_pixmap=r'resources\photo\plane.png'
        self.pixmap=QtGui.QPixmap(path_pixmap)

'''
@description: 敌军飞机类
@param  {*}
@return {*}
'''
class PlaneEnemy(BasePlane):
    def __init__(self) -> None:
        super().__init__()