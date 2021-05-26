'''
Description: 
Author: DJ
Date: 2021-05-26 16:16:52
LastEditTime: 2021-05-26 16:54:41
LastEditors: DJ
'''

class Plane():
    def __init__(self,class_plane) -> None:
        self.class_plane=class_plane
        self.pixmap=None
        self.x=0
        self.y=0
        self.HP=0
        self.MP=0
        self.class_bulet=''
        pass


class PlanePlayer(Plane):
    def __init__(self) -> None:
        super().__init__()

class PlaneEnemy(Plane):
    def __init__(self) -> None:
        super().__init__()