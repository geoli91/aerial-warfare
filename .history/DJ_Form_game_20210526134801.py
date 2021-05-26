'''
Description:  
Author: DJ
Date: 2021-05-26 13:39:58
LastEditTime: 2021-05-26 13:48:01
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from resources.UI.Ui_game_Form import Ui_DialogGame

class FormGame(QtWidgets.QDialog,Ui_DialogGame):
    def __init__(self,parent=None):
        super(FormGame,self).__init__(parent)
        self.setupUi(self)