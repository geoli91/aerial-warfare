'''
Description: 
Author: DJ
Date: 2021-05-26 15:24:54
LastEditTime: 2021-05-26 15:28:50
LastEditors: DJ
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class BackGround():
    def __init__(self,path_img,move_step) -> None:
        self.path_img=path_img
        self.move_step=move_step
        self.pixmap=QtGui.QPixmap(self.path_img)
        pass