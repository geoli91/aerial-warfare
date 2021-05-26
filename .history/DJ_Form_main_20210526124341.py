'''
Description: 
Author: DJ
Date: 2021-05-26 12:38:48
LastEditTime: 2021-05-26 12:43:41
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from resources.UI.Ui_start_window import Ui_MainWindowPlane

class FormMain(QtWidgets.QMainWindow,Ui_MainWindowPlane):
    # def __init__(self,) -> None:
    #     super().__init__()
    # sigmal_not_warning_voice=pyqtSignal() # 用于指示报警声音停止的信号

    def __init__(self,parent=None):
        super(FormMain,self).__init__(parent)
        self.setupUi(self)
