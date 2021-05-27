'''
Description: 
Author: DJ
Date: 2021-05-27 15:29:34
LastEditTime: 2021-05-27 15:32:57
LastEditors: DJ
'''

class MyKeyBoard():
    def __init__(self) -> None:
        self.set_key=set()
        pass

    def key_up(self,key):
        self.set_key.remove(key)

    def key_down(self,key):
        self.set_key.add(key)

    def is_key_down(self,key):
        return key in self.set_key