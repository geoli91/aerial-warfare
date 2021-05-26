'''
Description: 游戏控制类，用于控制游戏的各种操作和状态
Author: DJ
Date: 2021-05-26 15:35:06
LastEditTime: 2021-05-26 15:50:52
LastEditors: DJ
'''

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
    @param {*} str_name_player 玩家图标文件路径
    '''    
    def __init__(self,background,our_plane,list_enemy,list_bullet,str_name_player,path_player_img,list_) -> None:
        self.background=background
        self.our_plane=our_plane
        self.list_enemy=list_enemy
        self.list_bullet=list_bullet
        self.str_name_player=str_name_player
        self.path_player_img=path_player_img
        # 初始化其他属性
        self.int_score=0
        self.int_stage=1
        self.float_new_enemy_speed=2.0

    '''
    @description: 创建关卡
    @param  {*}
    @return {*}
    @param {*} self
    '''    
    def create_stage(self):
        pass