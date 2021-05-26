'''
Description: 
Author: DJ
Date: 2021-05-26 16:21:19
LastEditTime: 2021-05-26 17:13:07
LastEditors: DJ
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class Bullet():
    def __init__(self,class_bullet) -> None:
        self.class_bullet=class_bullet
        

        pass

    def init_attribute(self):
        self.move_speed=0.5 # 子弹移动速度
        self.class_shot=""
        path_img_bullet=None # 子弹图片文件路径
        if self.class_bullet=="player":
            path_img_bullet=r'resources\photo\bul02.png'
        self.pixmap=QtGui.QPixmap(path_img_bullet)