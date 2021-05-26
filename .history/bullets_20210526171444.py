'''
Description: 
Author: DJ
Date: 2021-05-26 16:21:19
LastEditTime: 2021-05-26 17:14:44
LastEditors: DJ
'''
from PyQt5 import QtCore, QtGui, QtWidgets

'''
@description: 子弹类
@param  {*}
@return {*}
'''
class Bullet():
    def __init__(self,class_bullet) -> None:
        self.class_bullet=class_bullet
        # 初始化子弹属性
        self.init_attribute()
        pass


    '''
    @description: 
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def init_attribute(self):
        self.move_speed=0.5 # 子弹移动速度
        path_img_bullet=None # 子弹图片文件路径
        self.x=0 # 子弹位置x
        self.y=0 # 子弹位置y
        if self.class_bullet=="player":
            path_img_bullet=r'resources\photo\bul02.png'
        self.pixmap=QtGui.QPixmap(path_img_bullet)