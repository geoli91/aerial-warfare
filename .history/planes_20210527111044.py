'''
Description: 飞机类，包括飞机的基类和继承基类的玩家飞机类和敌军飞机类
Author: DJ
Date: 2021-05-26 16:16:52
LastEditTime: 2021-05-27 11:10:41
LastEditors: DJ
'''
from bullets import Bullet
from PyQt5 import QtCore, QtGui, QtWidgets
import random

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

        self.move_step=3 # 飞机每次移动的步长
        pass
    
    '''
    @description: 发射子弹
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def shot(self):
        # # 实例化子弹对象并添加至子弹列表中
        bullet=Bullet(self.class_bulet)
        self.list_bullet.append(bullet)
        pass

    '''
    @description: 飞机向左飞
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_left(self):
        if self.x>0:
            self.x-=self.move_step

    '''
    @description: 飞机向右飞
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_right(self):
        if self.x<self.max_x:
            self.x+=self.move_step

    '''
    @description: 飞机向上飞
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_up(self):
        if self.y>0:
            self.y-=self.move_step
            
    '''
    @description: 飞机向下飞
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_low(self):
        if self.y<self.max_y:
            self.y+=self.move_step

'''
@description: 玩家飞机类
@param  {*}
@return {*}
'''
class PlanePlayer(BasePlane):
    def __init__(self,class_plane,class_bulet,list_bullet,max_x,max_y) -> None:
        # 重写了子类的 __init__ 方法，如果还希望继承父类的 __init__ 方案，可以使用 super 关键字，
        super(PlanePlayer,self).__init__(class_plane,class_bulet,list_bullet,max_x,max_y)
        self.__plane_flow='general' # 玩家飞机的飞行方向，有 正常 general、左偏 left、右偏 right 三种
        # 初始化飞机图标
        path_pixmap=r'resources\photo\plane.png'
        self.pixmap=QtGui.QPixmap(path_pixmap)
        # 初始化最大x值
        self.max_x-=self.pixmap.width() # 飞机能飞到的最大x值应为max_x减去飞机宽度
        # 初始化玩家飞机位置
        self.x=self.max_x/2
        self.y=self.max_y-self.pixmap.height()

    # 创建一个 plane_flow 属性
    @property
    def plane_flow(self):
        return self.__plane_flow
        
    # 为 plane_flow 属性添加一个 setter ，当 plane_flow 属性修改时修改飞机的 pixmap
    @plane_flow.setter
    def plane_flow(self,value):
        dict_value_path={'general':r'resources\photo\plane.png','left':r'resources\photo\planeLeft.png','right':r'resources\photo\planeRight.png'}
        func_value_path=lambda value:dict_value_path.get(value,r'resources\photo\plane.png')
        path_pixmap=func_value_path(value)
        self.pixmap=QtGui.QPixmap(path_pixmap)
        self.__plane_flow=value

    '''
    @description: 重写 move_left 方法，左移时修改飞机 plane_flow 属性
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_left(self):
        self.plane_flow='left'
        return super().move_left()

    '''
    @description: 重写 move_right 方法，右移时修改飞机 plane_flow 属性
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_right(self):
        self.plane_flow='right'
        return super().move_right()

    '''
    @description: 重写 shot 方法，发射玩家飞机的子弹
    @param  {*}
    @return {*}
    '''
    def shot(self):
        # 实例化一个子弹对象，设置其属性，并添加到子弹列表中
        self.bullet=Bullet(self.max_y,'player')
        self.bullet.x=self.x
        self.bullet.y=self.y
        self.bullet.signal_bullet_vanish.connect(self.remove_bullet) # 绑定子弹消失信号与移除子弹槽函数
        self.list_bullet.append(self.bullet)
        # return super().shot()
    
    '''
    @description: 从子弹列表中移除子弹
    @param  {*}
    @return {*}
    @param {*} self
    @param {*} bullet
    '''    
    def remove_bullet(self,bullet):
        self.list_bullet.remove(bullet)

'''
@description: 敌军飞机类
@param  {*}
@return {*}
'''
class PlaneEnemy(BasePlane):
    def __init__(self,class_plane,class_bulet,list_bullet,max_x,max_y) -> None:
        super(PlaneEnemy,self).__init__(class_plane,class_bulet,list_bullet,max_x,max_y)
        # 初始化飞机图标
        dict_class_path={'enemy_red':r'','enemy_green':r''}
        path_pixmap=r'resources\photo\plane.png'
        self.pixmap=QtGui.QPixmap(path_pixmap)
        # 初始化最大x值
        self.max_x-=self.pixmap.width() # 飞机能飞到的最大x值应为max_x减去飞机宽度
        # 初始化飞机位置
        self.x=random.randint(0,self.max_x)
        self.y=0
    