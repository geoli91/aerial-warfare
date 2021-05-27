'''
Description: 游戏控制类，用于控制游戏的各种操作和状态
Author: DJ
Date: 2021-05-26 15:35:06
LastEditTime: 2021-05-27 11:38:04
LastEditors: DJ
'''
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from planes import PlaneEnemy

'''
@description: 游戏控制类，用于控制游戏的各种操作和状态
@param  {*}
@return {*}
'''
class GameControl():
    '''
    @description: 初始化游戏控制类
    @param  {*}
    @return {*}
    @param {*} self
    @param {*} background 背景对象
    @param {*} our_plane 玩家飞机对象
    @param {*} list_enemy 敌机列表对象
    @param {*} list_bullet 子弹列表对象
    @param {*} str_name_player 玩家名称
    @param {*} path_player_img 玩家图标文件路径
    @param {*} list_background_img_path 背景图片文件路径列表
    '''    
    def __init__(self,background,plane_palyer,list_enemy,list_bullet,str_name_player,path_player_img,list_background_img_path,max_x,max_y) -> None:
        self.background=background
        self.our_plane=plane_palyer
        self.list_enemy=list_enemy
        self.list_bullet=list_bullet
        self.str_name_player=str_name_player
        self.path_player_img=path_player_img
        self.list_path_background_img=list_background_img_path
        self.max_x=max_x
        self.max_y=max_y
        # 初始化其他属性
        self.int_score=0 # 我方分数
        self.int_stage=1 # 当前关卡数
        self.float_new_enemy_speed=2.0 # 当前生成敌机间隔，单位为s
        # 使用定时器定时创建敌军
        # 定时器 QTimer 对象必须使用 self. 变成类的
        self.qtimer_create_enemy=QtCore.QTimer()
        self.qtimer_create_enemy.start(self.float_new_enemy_speed*1000)
        self.qtimer_create_enemy.timeout.connect(self.create_enemy)
        
 
    '''
    @description: 创建关卡
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def create_stage(self):
        # 修改状态参数，分数清零，关卡数+1
        self.int_score=0
        self.int_stage+=1
        # 生成敌机速度加快0.1s，直到生成速度=0.2s为止
        if self.float_new_enemy_speed>0.2:
            self.float_new_enemy_speed-=0.1
        # 随机选择背景，并赋值给背景类的pixmap属性
        index_background_img=random.randint(0,len(self.list_path_background_img)-1) # 使用 random.randint(int_min.int_max) 生成指定范围内的整数，包括int_min和int_max
        path_background_img=self.list_path_background_img[index_background_img]
        pixmap_bg=QtGui.QPixmap(path_background_img)
        self.background.pixmap=pixmap_bg

    def create_enemy(self):
        list_class_plane=['enemy_red','enemy_green','enemy_yellow']
        class_plane=list_class_plane[random.randint(0,len(list_class_plane)-1)]
        enemy=PlaneEnemy(class_plane,'enemy',self.list_bullet,self.list_enemy,self.max_x,self.max_y)
        self.list_enemy.append(enemy)
        print('create_enemy')
        