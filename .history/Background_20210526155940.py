'''
Description: 背景类
Author: DJ
Date: 2021-05-26 15:24:54
LastEditTime: 2021-05-26 15:59:37
LastEditors: DJ
'''
from PyQt5 import QtCore, QtGui, QtWidgets

'''
@description: 背景类
@param  {*}
@return {*}
'''
class BackGround():
    
    '''
    @description: 初始化背景类
    @param  {*}
    @return {*}
    @param {*} self
    @param {*} move_step 背景图片每次移动步长
    @param {*} max_y 背景图片最大的放置位置，超过该值则置零。通常为窗口高度
    '''    
    def __init__(self,move_step,max_y) -> None:
        # self.path_img=path_img
        self.move_step=move_step
        self.max_y=max_y
        self.pixmap=QtGui.QPixmap(self.path_img) # 背景图片对应pixmap
        self.x=0 # 背景的放置位置x
        self.y=0 # 背景的放置位置y
    
    
    '''
    @description: 背景y值增加指定步长。如果超过max_y，则置零
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move(self):
        self.y+=self.move_step
        if self.y>self.max_y:
            self.y=0
