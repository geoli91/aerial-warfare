'''
Description: 
Author: DJ
Date: 2021-05-26 15:24:54
LastEditTime: 2021-05-26 15:29:10
LastEditors: DJ
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class BackGround():
    def __init__(self,path_img,move_step) -> None:
        self.path_img=path_img # 背景图片路径
        self.move_step=move_step # 背景图片每次 
        self.pixmap=QtGui.QPixmap(self.path_img)
        pass