'''
Description: 
Author: DJ
Date: 2021-05-26 12:38:48
LastEditTime: 2021-05-26 12:40:24
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from 
from resources.UI.Ui_start_window import Ui_Main

class Ui_MainWindow(QObject,Ui_Main):
    # def __init__(self,) -> None:
    #     super().__init__()
    sigmal_not_warning_voice=pyqtSignal() # 用于指示报警声音停止的信号

    def init(self,MainWindow,path_par_db,path_par_recognize):
        """添加类的属性"""
         # 设置参数文件路径
        self.path_par_db=path_par_db
        self.path_par_recognize=path_par_recognize

        self.MainWindow=MainWindow
        self.bool_is_end_recognize=mp.Manager().Value('b',False) # 指定识别程序是否结束
        self.bool_is_end_fresh_recording=False # 指定刷新记录的线程是否结束
        # self._translate = QtCore.QCoreApplication.translate
        # self.setupUi(Ui_MainWindow)
        # 读取配置文件
        self.dict_par_db={} # 参数字典
        self.dict_par_recognize={}
        with open(self.path_par_db,'r',encoding='gbk') as f:
            self.dict_par_db=json.loads(f.read())
        with open(self.path_par_recognize,'r',encoding='gbk') as f:
            self.dict_par_recognize=json.loads(f.read())
        # 运行自建函数，初始化所有进程和控件
        self.init_all()