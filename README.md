# 校园共享打印助手微信小程序（客户端）

*注意：禁止用于商业用途，欢迎个人学习交流！*


## 简介

基于Socketio全双工通信与Pyqt5开发的微信小程序-校园共享打印助手。本程序为小程序对应的客户端程序，供有打印机的同学快速上线自己的打印服务，旨在改善校园、社区打印不便的情况。为个人想法的小小实现，不喜勿喷！

### 特点：
* 客户端程序有自动检索本机所连接的打印设备的功能；
* 支持用户开机自启动、并按照默认设置快速自动连接（即安装一次永久方便使用）；
* 用户只要打开微信小程序下拉刷新即可获取身边实时在线的打印机信息，在线下进行打印交易。


<img src="https://mmbiz.qpic.cn/mmbiz_png/QsUWqPChJWY8I5AsoW8j1lIThuibf4YqVV583L6PWhAhe46B9NzhJHcT48rCibrfWYC5upDxe5747m5JrQtKSP4w/0?wx_fmt=png" width = "400" height = "200" 
align=center>


<img src="https://mmbiz.qpic.cn/mmbiz_jpg/QsUWqPChJWZEj6CLVpYsUftHauom2ah0vz6Uzrb4PCQeFMQBwLdeFokLaSIwwgPWtlTBeXvMExSOlBVqb1vKwQ/0?wx_fmt=jpeg" width = "207" height = "448" 
align=center>




## 环境


在微软windows x64或者x86操作系统下运行。



## 如何使用该软件?

1.您可以在windows x64的操作系统上直接从百度网盘或者releases处下载该软件对应版本的安装包，解压或者安装直接点击使用。（x64版本安装包网盘链接为：https://pan.baidu.com/s/1Z3IHQlBf6cKolt1jbcdzow 
提取码：simt）
2. 初次使用，请填写您的相关位置信息（例如：d17栋/307宿舍/3床），并从复选框中选取您电脑连接的打印设备，程序会自动将当前的宿舍信息与打印设备信息保留在目录下的`config.ini`配置文件中，作为默认设置为供下次连接使用，然后点击点击连接即可。
3. 非初次使用会自动使用上次使用的宿舍信息进行连接，用户无需重新输入宿舍与打印设备信息；如信息有更改，则直接重新输入信息，并在询问是否使用默认设置的弹窗中点击No即可更新当前信息为默认设置，并以新信息连接。
4. 打印机的上下线情况，用户均可即时在小程序看到打印设备的上下线情况。

## 注意事项
* 请勿在开启VPN全局代理模式下使用，否则可能会出现连接失败报错等问题）
* 安装至开机自启动目录过程中，部分杀毒软件可能会阻止，选择解除阻止即可安装
* 关闭客户端程序，即断开连接下线，微信小程序端也不会下拉刷新到您的打印服务


## 小程序请见
<img src="https://mmbiz.qpic.cn/mmbiz_jpg/QsUWqPChJWY8I5AsoW8j1lIThuibf4YqV8KFlUmiaGVswt4mlCAoxUNZ1avthhtCiamicjuQsgniaZDc4XEH0kx0QvA/0?wx_fmt=jpeg" width = "200" height = "200" 
align=center>
