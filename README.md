README
==============
***This file will describe the project represented by each source code.***

|Author|Walker|
|---|---
|E-mail|402264457@qq.com

****
## Basic.py
*Study notes（Automate The Boring Stuff With Python）*
*****
## autoThread.py
*Automatic query automatically pushes qq messages through win32 module*
*****
## inspectionThread.py
*Automated inspection and generation of excel documents to send OA system*
*****
## dist folder
该文件夹是一个由pyinstaller执行打包的可执行的exe文件（包含两个项目autoThread、inspectionThread）  

***系统环境：windows server 2016***  
***SDK版本：python3.6以上***  

***autoThread使用方法：***  
1、gywl.bak gywl.dat gywl.dir 三个文件放入dist对应的程序文件中（该文件中包含数据库tns连接相关的信息以及web应用user、passwd信息，由于文件存在敏感信息，本项目中并没有将该文件上传）。  

2、autoThread文件夹下对应的DevopsConf是配置文件。  
