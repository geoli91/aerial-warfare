'''
Description: 
Author: DJ
Date: 2021-05-26 16:21:19
LastEditTime: 2021-05-26 17:10:08
LastEditors: DJ
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class Bullet():
    def __init__(self,class_bullet) -> None:
        self.class_bullet=class_bullet

        pass

    def init_attribute(self):
        if self.class_bullet=="player":
            self.pixmap=QtGui.QPixmap()