'''
Description: 
Author: DJ
Date: 2021-05-26 12:38:48
LastEditTime: 2021-05-26 12:43:49
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from resources.UI.Ui_start_window import Ui_MainWindowPlane

class FormMain(QtWidgets.QMainWindow,Ui_MainWindowPlane):
    '''
    @description: 
    @param  {*}
    @return {*}
    @param {*} self
    @param {*} parent
    '''    
    def __init__(self,parent=None):
        super(FormMain,self).__init__(parent)
        self.setupUi(self)
