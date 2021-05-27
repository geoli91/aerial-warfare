'''
Description: 程序的主函数，从此处开始运行
Author: DJ
Date: 2021-05-26 12:44:22
LastEditTime: 2021-05-27 14:23:44
LastEditors: DJ
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia

from Form_main import FormMain

if __name__ == '__main__':
    # 启动系统
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle("fusi on")
    ui = FormMain()
    # 显示窗口
    ui.show() # 正常显示
    # 系统打开即窗口最大化
    # ui.showMaximized() # 窗口最大化显示
    sys.exit(app.exec_())