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
|`autoThread.py`|___Use the cx_oracle module to query the available data, structure the data, and automatically push the data to qq through the win32 module (timer configurable)___|
|`inspectionThread.py`|___Use the selenium and openpyxl modules to log in to the grafana(Data source zabbix) visual monitoring system for automatic inspection and generate inspection excel documents. After formatting the data, send the document to the OA system.___|  


## Deployment
|ENVIRONMENT|DEPLOY|
|----|-----|
|`System environment`|***windows server 2016/2008(recommend 2016)***|
|`SDK version`|___python3.6↑___|  
|`Installation module`|___cx_Oracle、pymysql、win32、ctypes、pythoncom、logformat、requests、schedule、openpyxl、selenium、Pilow、pyinstaller___|       
|`Install`|___Step1. Pyinstaller py files___|  
| |___Step2. Put the configuration file(gywl.bak gywl.dat gywl.dir DevopsConf.ini) in the dist folder___|     
| |___Step3. Start the exe application in the dist directory___|  
 
## Instructions
|SCRIPT|HISTORIC VER|
|----|-----|
| |***1、07-12 single process***|
| |___Problem：High CPU consumption (25%)___|
| |___2、07-13  Add logging format___|
| |___3、07-15  Modify simple format___|
| |___4、07-17  Update logging___|
|`autoThread` |___Add output file___|
| |___4、07-23  Modify class(__init__)___| 
| |___Add clean screen___|
| |___Add Multi-threaded mode___|
| |___Solve：High CPU consumption___|
| |___Solve：Concurrency problem(mutex、join)___|
| |___5、09-05  Add openpyxl module___|
| |___6、09-06  Modify send file function(mutex clipboard)___
| |___7、09-12  Modify single thread___
| | |
| | |
| |***1、07-05 single process、***|
| |***2、07-06 logging format***|
| |***3、07-14 Update element(07-13 oa web update)***|
| |***Update log level***|
| |***Problem：High CPU consumption (25%)***|
|`inspectionThread` |***Problem：Unable to find element(No visual page available)***|
| |***Problem：Drive error***|
| |***4、07-15 Add clean screen***|
| |***Solve：High CPU consumption***|
| |***5、07-16 Update Chrome driver log level***|
| |***Solve：Unable to find element(window_size)***|
| |***Solve：Drive error(find exit element)***|
| |***6、09-08 Update element***|  

***Project1***   
>>autoThread：  
>>1、gywl.bak、gywl.dat、gywl.dir、DevopsConf.ini四个文件放入dist对应的程序文件中（该文件中包含数据库tns连接相关的信息以及web应用user、passwd信息，由于文件存在敏感信息，本项目中并没有将该文件上传）dist目录下文件是由pyinstaller打包生成exe可执行文件，在windows注册列表可配置成开机自启程序，所以这里建议使用windows server 2016环境运行，实测2008版本打包会出现错误。  

>>2、DevopsConf是相关查询sql、发送规则等配置文件。  

>>3、以上两步执行过后，执行dist文件夹下的autoThread.exe即可。    

   
***Project2***  
>>inspectionThread：  
>>1、请将gywl.bak、gywl.dat、gywl.dir、DevopsConf.ini、webdriver驱动、tem（模板文件）六个文件放入dist对应的程序文件中（该文件中包含数据库tns连接相关的信息以及web应用user、passwd信息，由于文件存在敏感信息，本项目中并没有将该文件上传）。  

>>2、DevopsConf可配置巡检时间。  

>>3、以上两步执行过后，执行dist文件夹下的inspectionThread.exe即可。   

***DevopsConf***    
>>该配置文件是全局配置文件，包含以下配置信息:  
>>1、SQL模块配置，若查询条件发生变更，请直接修改Oracle中视图即可，并且无需重启程序。(*标注的配置修改后，需重启程序，其余配置修改后无需重启)  

>>2、赛飞订单拦截规则配置，“物流中心名称”和QQ群名需要一一对应,列表中index前三位代表“出库”、“入库”、“调整单”，0表示开启推送1表示关闭推送。  

>>3、二方货主和三方货主每日截单配置，二方货主需按照“运营中心”和QQ群名一一对照，三方货主按照“货主名称”和QQ群名一一对照配置  

>>4、logging日志备份数量配置，默认配置7，可自定调整，(log_level info、error)。

>>5、Grafana可视化自动化巡检配置，包含巡检时间区间、url、OA发送模板。  

>>6、请注意！全局配置中0始终代表True，1代表False。

***Shelve conf***
>>gywl.bak、gywl.dat、gywl.dir该配置文件属于二进制文件，包含以下配置：  
>>1、Oracle IP、Name、User、Password  
>>2、Mysql IP、Port、User、Password、DB、Charset  
  
  
**注意事项1：若对源码进行修改，修改后用pyinstaller工具打包py文件。**  
**注意事项2：所有配置文件的修改，请提前做好备份，以免配置错误导致程序报错。**   
**注意事项3：gywl.bak、gywl.dat、gywl.dir二进制文件，在数据连接信息不发生改变无需修改，若需要修改请使用shelve重新生成文件即可。**   


## Display  
|·|AUTOTHREAD|DISPLAY|
|---|---|----
|1|`LOGGER`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/query_sendqq_log_0.png)
|2|`MESS`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/query_sendqq_log_1.png)
|3|`FILE1`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/query_sendqq_log_2.png)
|4|`FILE2`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/pic1.png)  
|5|`FILE3`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/excel1.png)  
|6|`FILE4`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/excel2.png)    
|7|`FILE5`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/excel3.png)     
|8|`Conf1`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/DevopConf1.png)  
|9|`Conf2`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/DevopConf2.png)  
|10|`Conf3`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/DevopConf3.png)  
|11|`Conf4`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/DevopConf4.png)  
|12|`Conf5`|![](https://github.com/walkeradmin/Pub/blob/master/Dispic/DevopConf5.png)  
*********
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

## Reward  
**知行合一，学以致用。**    
**Automate the boring stuff with python**  
>>1、如何将数据结构化，以便处理?  
>>2、如何熟练定义使用Class类对象?  
>>3、如何选择多进程or多线程?各有什么特点?  
>>4、如何解决并发问题?  
>>5、如何理解python GIL?  
>>6、如何解决死锁现象?(Timeout、**银行家算法**)  
>>7、如何使用configparser灵活配置?  
>>8、如何使用selenium?如何处理(text field or textarea、Button、form、Mouse   MoveOn、富文本框、alert/confirm/prompt)?   
>>9、如何不重复创建thread降低系统开销资源消耗?(待深究)   
>>10、如何灵活运用openpyxl模块生成execel文档?   
>>11、如何使用ctypes拷贝出BMP数据以及copy_paste?(此处参考https://www.programcreek  .com/python/example/63206/pythoncom.TYMED_HGLOBAL)   
>>12、如何使用selenium捕获伪元素(before)、隐藏元素?(待研究)   