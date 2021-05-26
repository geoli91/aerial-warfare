'''
Description: 
Author: DJ
Date: 2021-05-26 12:44:22
LastEditTime: 2021-05-26 12:45:08
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DJ_Form_main import FormMain

if __name__ == '__main__':
    # 启动系统
    app = QApplication(sys.argv)
    # app.setStyle("fusion")
    MainWindow = QMainWindow()
    dict_par_modify={} # 该字典用于存储一些用户无需关注的参数，实际运行的时候该字典会被合并到 dict_par_recognize 中
    with open(path_par_modify,'r',encoding='gbk') as f:
        dict_par_modify=json.loads(f.read())
    ui = FormMain()
    # 显示窗口
    ui.show() # 正常显示
    # 系统打开即窗口最大化
    MainWindow.showMaximized() # 窗口最大化显示
    sys.exit(app.exec_())