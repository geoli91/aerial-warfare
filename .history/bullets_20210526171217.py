'''
Description: 
Author: DJ
Date: 2021-05-26 16:21:19
LastEditTime: 2021-05-26 17:12:17
LastEditors: DJ
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class Bullet():
    def __init__(self,class_bullet) -> None:
        self.class_bullet=class_bullet
        self.move_speed=0.

        pass

    def init_attribute(self):
        path_img_bullet=None
        if self.class_bullet=="player":
            path_img_bullet=r'resources\photo\bul02.png'
        self.pixmap=QtGui.QPixmap(path_img_bullet)