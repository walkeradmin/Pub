README
==============
***This file will describe the project represented by each source code.***

|Author|Walker|
|---|---
|E-mail|402264457@qq.com

****

|SCRIPT|DESCRIPTION|
|----|-----|
|`Basic.py`|***Study notes（Automate The Boring Stuff With Python）***|
|`autoThread.py`|___Automatic query automatically pushes qq messages through win32 module___|
|`inspectionThread.py`|___Automated inspection and generation of excel documents to send OA system___|  


*****
## dist folder

|环境|配置|
|----|-----|
|`系统环境`|***windows server 2016***|
|`SDK版本`|___python3.6以上___|
|`安装模块`|___cx_Oracle、win32、ctypes、pythoncom___|       
  
  
***Project1***   
*autoThread使用方法：*  
>>*1、请将gywl.bak gywl.dat gywl.dir、DevopsConf.ini四个文件放入dist对应的程序文件中（该文件中包含数据库tns连接相关的信息以及web应用user、passwd信息，由于文件存在敏感信息，本项目中并没有将该文件上传）。*  

>>*2、DevopsConf是相关查询sql、发送规则等配置文件。*  

>>*3、以上两步执行过后，执行dist文件夹下的autoThread.exe即可。*    
  
  
***Project2***  
*inspectionThread使用方法：*  
>>*1、请将gywl.bak gywl.dat gywl.dir、DevopsConf.ini、webdriver驱动、tem（模板文件）六个文件放入dist对应的程序文件中（该文件中包含数据库tns连接相关的信息以及web应用user、passwd信息，由于文件存在敏感信息，本项目中并没有将该文件上传）。*  

>>*2、DevopsConf可配置巡检时间。*  

>>*3、以上两步执行过后，执行dist文件夹下的inspectionThread.exe即可。*   
