# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:12:41 2021

@author: kayak
"""

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import win32print
import socketio
import PyQt5.QtCore as qc



class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()
        
        #程序样式代码
        self.setMaximumSize(530, 150)
        self.setWindowTitle("校园共享打印助手（客户端)")

        self.label = QLabel(self)
        self.label.setText("请选择您的打印设备")
        self.label.setFixedSize(150, 25)
        self.label.move(10, 18)

        
        self.cb = QComboBox(self)
        self.cb.move(150, 20)
        self.cb.addItems(printer_list)


        self.textEdit = QLineEdit(self)
        self.textEdit.setPlaceholderText("请输入校区/宿舍/床号")
        self.textEdit.move(10, 60)
        self.textEdit.resize(400, 30)

        btn = QPushButton(self)
        btn.setText("连接上线")
        btn.move(155, 105)
        btn.clicked.connect(self.getmsg)


    #信号与槽绑定发送事件    
    def getmsg(self):
        try:
            if settings.value("PRINTER/information_msg")==None:
                data = self.textEdit.text()+self.cb.currentText()+'设备上线'
                settings.setValue("PRINTER/information_msg",self.textEdit.text())
                settings.setValue("PRINTER/device",self.cb.currentText())
                io_client(data)
                QMessageBox.about(self, '消息提示', '成功上线！')
            else:                
                button = QMessageBox.question(self,"Question","是否使用此前的默认设置连接？",
                                          QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                if button == QMessageBox.Yes:
                    data = settings.value("PRINTER/information_msg")+settings.value("PRINTER/device")+'设备上线'
                    io_client(data)
                    QMessageBox.about(self, '消息提示', '成功上线！')
                else:
                    data = self.textEdit.text()+self.cb.currentText()+'设备上线'
                    settings.setValue("PRINTER/information_msg",self.textEdit.text())
                    settings.setValue("PRINTER/device",self.cb.currentText())
                    io_client(data)
                    QMessageBox.about(self, '消息提示', '成功上线！')                    
        except:
            QMessageBox.about(self, '消息提示', '连接失败，请重新操作检查网络连接！')
            
#socketio连接flask-socketio服务器端（连接到您的域名，对应的命名空间）
def io_client(data):    
    sio = socketio.Client()
    sio.connect('https://yourdominatename.com', namespaces=['/your_name_space'])
    sio.emit('my_event',{'data': data},namespace='/your_name_space')
    




if __name__ == "__main__":
    settings = qc.QSettings("config.ini", qc.QSettings.IniFormat)
    #win32print获取本机打印设备列表
    printer_list = []
    for i in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL):
            printer_list.append(i[2])
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())

