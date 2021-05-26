'''
Description: 
Author: DJ
Date: 2021-05-26 15:24:54
LastEditTime: 2021-05-26 15:30:46
LastEditors: DJ
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class BackGround():
    def __init__(self,path_img,move_step,max_y) -> None:
        self.path_img=path_img # 背景图片路径
        self.move_step=move_step # 背景图片每次移动步长
        self.max_y=max
        self.pixmap=QtGui.QPixmap(self.path_img) # 背景图片对应pixmap
        self.x=0 # 背景的放置位置x
        self.y=0 # 背景的放置位置y
    
    def move(self):
        self.y+=self.move_step
