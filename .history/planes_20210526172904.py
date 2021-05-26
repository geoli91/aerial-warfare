'''
Description: 飞机类，包括飞机的基类和继承基类的玩家飞机类和敌军飞机类
Author: DJ
Date: 2021-05-26 16:16:52
LastEditTime: 2021-05-26 17:28:58
LastEditors: DJ
'''
from bullets import Bullet

'''
@description: 
@param  {*}
@return {*}
'''
class BasePlane():
    def __init__(self,class_plane,list_bullet) -> None:
        self.class_plane=class_plane
        self.class_bulet=
        self.list_bullet=list_bullet
        # 设置一些默认属性
        self.pixmap=None #  飞机图标
        self.x=0 # 飞机位置x
        self.y=0 # 飞机位置y
        self.HP=0 # 飞机 HP
        self.MP=0 # 飞机 MP
        self.class_bulet='general' # 子弹类型，默认为 general 一般的子弹，canister 为霰弹
        pass

    def shot(self):
        bullet=Bullet()


class PlanePlayer(BasePlane):
    def __init__(self) -> None:
        super().__init__()

class PlaneEnemy(BasePlane):
    def __init__(self) -> None:
        super().__init__()