'''
Description: 飞机类，包括飞机的基类和
Author: DJ
Date: 2021-05-26 16:16:52
LastEditTime: 2021-05-26 16:59:27
LastEditors: DJ
'''

'''
@description: 
@param  {*}
@return {*}
'''
class  Plane():
    def __init__(self,class_plane) -> None:
        self.class_plane=class_plane
        self.pixmap=None
        self.x=0
        self.y=0
        self.HP=0
        self.MP=0
        self.class_bulet='general' # 子弹类型，默认为 general 一般的子弹，canister 为霰弹
        pass


class PlanePlayer(Plane):
    def __init__(self) -> None:
        super().__init__()

class PlaneEnemy(Plane):
    def __init__(self) -> None:
        super().__init__()