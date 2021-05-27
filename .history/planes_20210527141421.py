'''
Description: 飞机类，包括飞机的基类和继承基类的玩家飞机类和敌军飞机类
Author: DJ
Date: 2021-05-26 16:16:52
LastEditTime: 2021-05-27 14:14:19
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
class BasePlane(QtCore.QObject):
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
        self.__HP=1 # 飞机HP
        self.MP=0 # 飞机 MP

        self.move_step=3 # 飞机每次移动的步长

        QtCore.QObject.__init__(self)

    """将HP设置为飞机属性，以便"""
    @property
    def HP(self):
        return self.__HP

    @HP.setter
    def HP(self,value):
        self.__HP=value
        # 判断飞机血量，如果为0，则触发爆炸
        if self.HP==0:
            self.bomb()

    def bomb(self):
        """依据飞机不同，设置不同的爆炸效果"""
        dict_class_path={}

        """如果爆炸的是玩家飞机，传递游戏结束信号；如果爆炸的是敌军飞机，使用Qtimer，爆炸几秒后，移除飞机"""
        
        pass
   
    def shot(self):
        '''
        @description: 发射子弹
        @param  {*}
        @return {*}
        @param {*} self
        ''' 
        # # 实例化子弹对象并添加至子弹列表中
        bullet=Bullet(self.max_y,self.list_bullet,self.class_bulet)
        self.list_bullet.append(bullet)
        pass


    '''
    @description: 飞机向左飞
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_left(self):
        self.x-=self.move_step

    '''
    @description: 飞机向右飞
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_right(self):
        self.x+=self.move_step

    '''
    @description: 飞机向上飞
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_up(self):
        self.y-=self.move_step
            
    '''
    @description: 飞机向下飞
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_low(self):
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
        # 初始化玩家生命值
        self.HP=100

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
        if self.x>0:
            self.x-=self.move_step

    '''
    @description: 重写 move_right 方法，右移时修改飞机 plane_flow 属性
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_right(self):
        self.plane_flow='right'
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
    @description: 重写 shot 方法，发射玩家飞机的子弹
    @param  {*}
    @return {*}
    '''
    def shot(self):
        # 实例化一个子弹对象，设置其属性，并添加到子弹列表中
        # self.bullet=Bullet(self.max_y,'player')
        bullet=Bullet(self.max_y,self.list_bullet,self.class_bulet)
        bullet.x=self.x
        bullet.y=self.y
        self.list_bullet.append(bullet)
    


'''
@description: 敌军飞机类
@param  {*}
@return {*}
'''
class PlaneEnemy(BasePlane):
    def __init__(self,class_plane,class_bulet,list_bullet,list_enemy,max_x,max_y) -> None:
        super(PlaneEnemy,self).__init__(class_plane,class_bulet,list_bullet,max_x,max_y)
        self.list_enemy=list_enemy
        # 依据飞机类型初始化飞机图标
        dict_class_path={
            'enemy_red':r'resources\photo\fighterRed.png',
            'enemy_green':r'resources\photo\fighterGreen.png',
            'enemy_yellow':r'resources\photo\fighterYellow.png'
            }
        func_class_path=lambda class_plane:dict_class_path.get(class_plane,r'resources\photo\fighterRed.png')
        path_pixmap=func_class_path(class_plane)
        self.pixmap=QtGui.QPixmap(path_pixmap)
        # 初始化最大x值
        self.max_x-=self.pixmap.width() # 飞机能飞到的最大x值应为max_x减去飞机宽度
        # 初始化飞机位置
        self.x=random.randint(0,self.max_x)
        self.y=0
        # 创建定时器，定时移动敌机
        self.qtimer_move_nenmy=QtCore.QTimer()
        self.qtimer_move_nenmy.start(200)
        self.qtimer_move_nenmy.timeout.connect(self.move_enemy)
        # 创建定时器，定时发射子弹
        self.qtimer_shot=QtCore.QTimer()
        self.qtimer_shot.start(200)
        self.qtimer_shot.timeout.connect(self.shot)
    
    
    '''
    @description: 重写 shot 方法，实现敌军发射子弹
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def shot(self):
        # 实例化一个子弹对象，设置其属性，并添加到子弹列表中
        # self.bullet=Bullet(self.max_y,'enemy')
        bullet=Bullet(self.max_y,self.list_bullet,self.class_bulet)
        bullet.x=self.x+self.pixmap.width()/2
        bullet.y=self.y+self.pixmap.height()
        # self.bullet.signal_bullet_vanish.connect(self.remove_bullet) # 绑定子弹消失信号与移除子弹槽函数
        self.list_bullet.append(bullet)
        # return super().shot()

    '''
    @description: 敌军移动，随机向一个方向移动3次
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move_enemy(self):
        # print("move_enemy")
        dict_int_move={1:self.move_left,2:self.move_right}
        func_int_move=lambda int_i:dict_int_move.get(int_i,self.move_low)()
        int_i=random.randint(1,2)
        for i in range(0,3):
            func_int_move(int_i)
            self.move_low()
        # 判断敌机是否超出范围，如果是，移除敌机
        if self.x<0 or self.x>self.max_x or self.y<0 or self.y>self.max_y:
            self.remove_enemy()

    '''
    @description: 去除敌军
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def remove_enemy(self):
        self.list_enemy.remove(self)
        del self