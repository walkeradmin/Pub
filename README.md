README
==============
***This file will describe the project represented by each source code.***

|Author|Walker|
|---|---
|QQ|402264457


## Description
|SCRIPT|DESCRIPTION|
|----|-----|
|`Basic.py`|***Study notes（Automate The Boring Stuff With Python）***|
|`autoThread.py`|___Automatic query automatically pushes qq messages through win32 module___|
|`inspectionThread.py`|___Automated inspection and generation of excel documents to send OA system___|  


## Deployment
|ENVIRONMENT|DEPLOY|
|----|-----|
|`System environment`|***windows server 2016***|
|`SDK Version`|___python3.6↑___|
|`Installation module`|___cx_Oracle、win32、ctypes、pythoncom___|       
  
  
## Instructions
|SCRIPT|HISTORIC VER|
|----|-----|
| |***1、07-12 single process***|
| |__Problem：High CPU consumption (25%)__|
| |___2、07-13  Add logging format___|
| |___3、07-15  Modify simple format___|
| |___4、07-17  Update logging___|
|`autoThread` |__Add output file__|
| |___4、07-23  Modify class(__init__)___| 
| |__Add clean screen__|
| |__Add Multi-threaded mode__|
| |__Solve：High CPU consumption__|
| |__Solve：Concurrency problem(mutex、join)__|
| | |
| | |
| |***1、07-05 single process、***|
| |***2、07-06 logging format***|
| |***3、07-14 Update element(07-13 oa web update)***|
| |***Update log level***|
| |__Problem：High CPU consumption (25%)__|
|`inspectionThread` |__Problem：Unable to find element(No visual page available)__|
| |__Problem：Drive error__|
| |***4、07-15 Add clean screen***|
| |__Solve：High CPU consumption__|
| |***5、07-16 Update：Chrome dirver log level***|
| |__Solve：Unable to find element(window_size)__|
| |__Solve：Drive error(find exit element)__|
********
***Project1***   
>>*autoThread：*  
>>*1、请将gywl.bak、gywl.dat、gywl.dir、DevopsConf.ini四个文件放入dist对应的程序文件中（该文件中包含数据库tns连接相关的信息以及web应用user、passwd信息，由于文件存在敏感信息，本项目中并没有将该文件上传）。*  

>>*2、DevopsConf是相关查询sql、发送规则等配置文件。*  

>>*3、以上两步执行过后，执行dist文件夹下的autoThread.exe即可。*    
  
  
***Project2***  
>>*inspectionThread：*  
>>*1、请将gywl.bak、gywl.dat、gywl.dir、DevopsConf.ini、webdriver驱动、tem（模板文件）六个文件放入dist对应的程序文件中（该文件中包含数据库tns连接相关的信息以及web应用user、passwd信息，由于文件存在敏感信息，本项目中并没有将该文件上传）。*  

>>*2、DevopsConf可配置巡检时间。*  

>>*3、以上两步执行过后，执行dist文件夹下的inspectionThread.exe即可。*   


## Display  

|·|AUTOTHREAD|DISPLAY|
|---|---|----
|1|`MESS`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/query_sendqq_log_1.png)
|2|`FILE`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/query_sendqq_log_2.png)  

********
|·|INSPECTION|DISPLAY|
|---|---|----
|1|`LOGGER`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_0.png)
|2|`FILE`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_1.0.png)
|3|`EXCEL`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_1.png)  
|4|`EXCEL`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_2.png)
|5|`PRCSTATUS`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_3.png)
|6|`DISK`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_4.png)
|7|`CPU`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_5.png)
|8|`NETWORK`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_6.png)
|9|`LOAD`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_7.png)
|10|`MEM`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_8.png)
|11|`OA`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/autoins_excel_send_9.png)