'''
Description: 游戏控制类，用于控制游戏的各种操作和状态
Author: DJ
Date: 2021-05-26 15:35:06
LastEditTime: 2021-05-27 14:39:36
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
        self.plane_player=plane_palyer
        self.list_enemy=list_enemy
        self.list_bullet=list_bullet
        self.str_name_player=str_name_player
        self.path_player_img=path_player_img
        self.list_path_background_img=list_background_img_path
        self.max_x=max_x
        self.max_y=max_y
        # 初始化其他属性
        # self.int_score=0 # 我方分数
        self.__int_score=0 # 我方分数
        self.int_stage=0 # 当前关卡数
        self.float_new_enemy_speed=2.0 # 当前生成敌机间隔，单位为s
        self.crack_threshold=0 # 认定为碰撞的重叠度阈值，当重叠度大于阈值时才认为两个对象碰撞了
        # 使用定时器定时创建敌军
        # 定时器 QTimer 对象必须使用 self. 变成类的属性才能生效，否则会一直报错但是也不生效
        self.qtimer_create_enemy=QtCore.QTimer()
        self.qtimer_create_enemy.start(self.float_new_enemy_speed*1000)
        self.qtimer_create_enemy.timeout.connect(self.create_enemy)
        # 使用定时器定时移动背景
        self.qtimer_move_bg=QtCore.QTimer()
        self.qtimer_move_bg.start(200)
        self.qtimer_move_bg.timeout.connect(self.background.move)
        # 使用定时器定时做碰撞检测
        self.qtimer_crack_detect=QtCore.QTimer()
        self.qtimer_crack_detect.start(20)
        self.qtimer_crack_detect.timeout.connect(self.crack_detect)
        
    """将 int-score 设置为飞机属性，以便使用 setter 监控飞机血量"""
    @property
    def int_score(self):
        return self.__int_score

    @int_score.setter
    def int_score(self,value):
        self.__int_score=value
        # 判断当前得分，如果大于1000，则进入下一关
        if self.int_score>=1000:
            self.create_stage()
 
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
        # 玩家回到初始状态
        self.plane_player.x=self.plane_player.max_x/2
        self.plane_player.y=self.plane_player.max_y-self.plane_player.pixmap.height()
        self.plane_player.HP=100
        # 敌机列表和子弹列表清空
        self.list_enemy=[]
        self.list_enemy=[]
        # 生成敌机速度加快0.1s，直到生成速度=0.2s为止
        if self.float_new_enemy_speed>0.2:
            self.float_new_enemy_speed-=0.1
        # 随机选择背景，并赋值给背景类的pixmap属性
        index_background_img=random.randint(0,len(self.list_path_background_img)-1) # 使用 random.randint(int_min.int_max) 生成指定范围内的整数，包括int_min和int_max
        path_background_img=self.list_path_background_img[index_background_img]
        pixmap_bg=QtGui.QPixmap(path_background_img)
        self.background.pixmap=pixmap_bg

    '''
    @description: 创建敌军
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def create_enemy(self):
        list_class_plane=['enemy_red','enemy_green','enemy_yellow']
        class_plane=list_class_plane[random.randint(0,len(list_class_plane)-1)]
        enemy=PlaneEnemy(class_plane,'enemy',self.list_bullet,self.list_enemy,self.max_x,self.max_y)
        self.list_enemy.append(enemy)
        # print('create_enemy')


    '''
    @description: 碰撞检测，检测到碰撞就依据种类进行对应处理
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def crack_detect(self):
        """检测玩家飞机与敌方飞机的碰撞"""
        for enemy in self.list_enemy:
            overlap_percent=self.crack_detect_object(self.plane_player,enemy)
            if overlap_percent>self.crack_threshold:
                enemy.HP-=1
                self.plane_player.HP-=1
                self.int_score+=1
        """检测玩家飞机与敌方子弹的碰撞"""
        for bullet in [x for x in self.list_bullet if x.class_bullet=='enemy' ]:
            overlap_percent=self.crack_detect_object(self.plane_player,bullet)
            if overlap_percent>self.crack_threshold:
                self.plane_player.HP-=1
                bullet.remove_bullet()
        """检测敌方飞机与玩家子弹的碰撞"""
        for enemy in self.list_enemy:
            for bullet in [x for x in self.list_bullet if x.class_bullet=='player' ]:
                overlap_percent=self.crack_detect_object(enemy,bullet)
                if overlap_percent>self.crack_threshold:
                    enemy.HP-=1
                    self.int_score+=1
                    bullet.remove_bullet()
        

    '''
    @description: 检测两个对象的重叠度，如果不重叠返回0，如果重叠返回重叠度
    @param  {*}
    @return {*}
    @param {*} self
    @param {*} object_a 待检测的第一个对象
    @param {*} object_b 待检测的第二个对象
    '''    
    def crack_detect_object(self,object_a,object_b):
        # 获取对象的位置和长宽
        x1, y1, w1, h1=[object_a.x,object_a.y,object_a.pixmap.width(),object_a.pixmap.width()]
        x2, y2, w2, h2=[object_b.x,object_b.y,object_b.pixmap.width(),object_b.pixmap.width()]
        # 计算重叠度
        overlap_percent=0
        if x1>x2+w2 or y1>y2+h2 or x1+w1<x2 or y1+h1<y2:
            overlap_percent= 0
        else:
            colInt = abs(min(x1 +w1 ,x2+w2) - max(x1, x2))
            rowInt = abs(min(y1 + h1, y2 +h2) - max(y1, y2))
            overlap_area = colInt * rowInt
            area1 = w1 * h1
            area2 = w2 * h2
            overlap_percent= overlap_area / (area1 + area2 - overlap_area)
        # print(overlap_percent)
        return overlap_percent
