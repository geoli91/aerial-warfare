'''
Description: 
Author: DJ
Date: 2021-05-26 16:21:19
LastEditTime: 2021-05-26 22:15:32
LastEditors: DJ
'''
from PyQt5 import QtCore, QtGui, QtWidgets

'''
@description: 子弹类
@param  {*}
@return {*}
'''
class Bullet():
    def __init__(self,class_bullet="player") -> None:
        self.class_bullet=class_bullet
        # 初始化子弹属性
        self.init_attribute()
        pass


    '''
    @description: 初始化子弹属性
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def init_attribute(self):
        self.move_speed=5 # 子弹移动速度
        self.angle=0 # 子弹移动的角度
        self.x=0 # 子弹位置x
        self.y=0 # 子弹位置y
        # 设置子弹图标
        path_img_bullet=None # 子弹图片文件路径
        # 通过字典映射的方式实现switch case 选择
        dict_path_img_bullet={'player':r'resources\photo\bul02.png','player_-30':r'resources\photo\bul02_-30.png','player_-60':r'resources\photo\bul02_-60.png','player_30':r'resources\photo\bul02_30.png','player_60':r'resources\photo\bul02_60.png',
        'enemy':r'resources\photo\en_bul01.png'}
        func_get_path_img_bullet=lambda class_bullet:dict_path_img_bullet.get(class_bullet,r'resources\photo\bul02.png') # 创建 lambda匿名函数
        path_img_bullet=func_get_path_img_bullet(self.class_bullet) # 调用匿名函数获取对应图片路径
        # if self.class_bullet=="player":
        #     path_img_bullet=r'resources\photo\bul02.png'
        # elif self.class_bullet=="enemy":
        #     path_img_bullet=r'resources\photo\en_bul01.png'
        # elif self.class_bullet=="player_-30":
        #     path_img_bullet=r'resources\photo\bul02_-30.png'
        self.pixmap=QtGui.QPixmap(path_img_bullet)

    
    def move(self):
        if self.
        pass