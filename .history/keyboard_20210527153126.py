'''
Description: 
Author: DJ
Date: 2021-05-27 15:29:34
LastEditTime: 2021-05-27 15:31:22
LastEditors: DJ
'''

class MyKeyBoard():
    def __init__(self) -> None:
        self.list_key=[]
        pass

    def key_up(self,key):
        self.list_key.append(key)

    def key_down(self.key)