'''
Description: 
Author: DJ
Date: 2021-05-26 16:21:19
LastEditTime: 2021-05-27 11:45:06
LastEditors: DJ
'''
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5

'''
@description: 子弹类
@param  {*}
@return {*}
'''
class Bullet(QtCore.QObject):
    signal_bullet_vanish=QtCore.pyqtSignal(QtCore.QObject)

    def __init__(self,max_y,class_bullet="player") -> None:
        self.class_bullet=class_bullet
        self.max_y=max_y # 子弹能到达的最大y值
        # 初始化子弹属性
        self.init_attribute()

        QtCore.QObject.__init__(self)


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
        self.pixmap=QtGui.QPixmap(path_img_bullet)
        # 使用定时器定时移动子弹
        self.qtimer=QtCore.QTimer()
        self.qtimer.start(20)
        self.qtimer.timeout.connect(self.move)

    '''
    @description: 子弹移动
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def move(self):
        # 如果是玩家的子弹，向上移动
        if self.class_bullet=='player':
            self.y-=self.move_speed
        # 如果是地方的子弹，向下移动
        elif self.class_bullet == 'enemy':
            self.y+=self.move_speed
        # 判断子弹是否出界，如果子弹出界，发送信号
        if self.y>self.max_y or self.y<0:
            self.signal_bullet_vanish.emit(self)
