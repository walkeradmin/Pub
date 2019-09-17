# -*- coding:utf-8 -*-
import configparser

# # 重新定义，解决大小写问题
# class CONF(configparser.ConfigParser):
#     def __init__(self):
#         configparser.ConfigParser.__init__(self)
#
#     def optionxform(self, option):
#         return option


conf = configparser.ConfigParser(allow_no_value=True)
conf['''###########################################################################################
#This is a global configuration file with the following configuration information.
#1. SQL view configuration
#2. logistics center and QQ group, document processing mode configuration
#3. Two-party and three-party documents check the operation center configuration
#4. scheduled task time configuration
#5. the number of log backup configuration
#6. Granfana inspection configuration
#7. 0 means enable 1 means disable
#It is recommended to back up before modifying the configuration file!!!
###########################################################################################'''] = {}
conf['###### SQL configuration ######'] = {}
conf['SQL'] = {"order_all": "select * from order_adj_week_view",
               "order_ma": "select * from order_makadan_view",
               "sql_all_rec": "select * from order_statistics_view",
               "sql_all_feed": "select * from order_statistics_feed_view",
               "sql_sh_sn": "select * from duidanjiaoben_view",
               "db_link": """declare begin save.p_save_erp_check_order; end;""",
               "sql_erp": """select 'ERP',sum(case type when 1 then 1 else 0 end) 入库总数,
sum(case type when 1 then dtlcount else 0 end) 入库明细总数,
sum(case type when 2 then 1 else 0 end) 出库总数,
sum(case type when 2 then dtlcount else 0 end) 出库明细总数 
from save.p_save_erp_check_order_t a union all select '平台',
sum(case when type=1 and a.billno is not null then 1 else 0 end) 入库总数,
sum(case  when type=1 and a.billno is not null then dtlcount_pt else 0 end) 入库明细总数,
sum(case  when type=2 and a.billno is not null then 1 else 0 end) 出库总数,
sum(case  when type=2 and a.billno is not null then dtlcount_pt else 0 end) 出库明细总数 
from save.p_save_erp_check_order_t a 
""",
               "sql_feed": """select billno
from save_feedbackqueue qe
where qe.owner = '115'
and qe.ts > to_char(sysdate - 5, 'yyyy-mm-dd hh24:mi:ss')
and qe.billtype not in ('T500', 'T340')
""",
               "sql_xj": """select
       n.custname 运营中心标识,
       count(*) 明细,
       count(distinct s.orderoid) 总单,
       substr(s.creationtime, 0, 10) || ' 01:01:01' 创建时间,
       to_number(a.custcode) 货主编码,
       a.unicode 货主编码物流,
       a.custname 货主名称,
       c.warecode 仓库代码,
       c.warename 仓库名称,
       r.name 业务类型,
       r1.name 送货方式,
       r2.name 运输方式,
       r3.name 运输时限要求,
       r4.name 原运输时限,
       d.cbid 仓别编码
       --a.pk_owner_h a_pk_owner_h,
       --c.pk_storage_h c_pk_storage_h
  from sbill_out_b b
  left join sbill_out_h h
    on b.pk_logist_h = h.pk_logist_h
  left join sbill_entrout_b e
    on b.pk_entrust_b = e.pk_ownerout_b
  left join sbill_entrout_h s
    on s.pk_ownerout_h = e.pk_ownerout_h
  left join sbase_storage_h c
    on c.pk_storage_h = s.storage
  left join sbase_owner_h a
    on s.ownerid = a.pk_owner_h
  left join sbase_storage_cb d
    on d.pk_storage_cb = e.storageid
  left join bd_defdoc f
    on f.pk_defdoc = e.quanstatus
  left join sbase_cust_h g
    on g.pk_cust_h = s.owneroid
  left join sbase_cust_addr i
    on i.pk_cust_addr = s.address
  left join sbase_ogoods_h j
    on j.pk_ogoods_h = e.goodsid
  left join sic_lotnodoc k
    on k.pk_lotno = e.lotnoid
  left join bd_region l
    on l.pk_region = i.pk_sqz
  left join bd_region m
    on i.pk_cities = m.pk_region
  left join sbase_center_h n
    on c.pk_custdoc = n.pk_center_h
  left join bd_defdoc q
    on q.pk_defdoc = j.pk_packunit_trade
  left join bd_defdoc r
    on r.pk_defdoc = s.pk_operationtype
  left join bd_defdoc r1
    on r1.pk_defdoc = h.pk_outmode
  left join bd_defdoc r2
    on r2.pk_defdoc = h.transmodeid
  left join bd_defdoc r3
    on r3.pk_defdoc = h.timelimit
  left join bd_defdoc r4
    on r4.pk_defdoc = s.timelimit
 where n.custcode in {}
and s.maketime> TO_CHAR (trunc(sysdate), 'yyyy-mm-dd hh24:mi:ss')
 group by r.name,
          r1.name,
          r2.name,
          r3.name,
          r4.name,
          a.custcode,
          a.unicode,
          a.custname,
          c.warename,
          c.warecode,
          d.cbid,
          substr(s.creationtime, 0, 10),
          a.pk_owner_h,
          c.pk_storage_h,
          n.custname
 order by 创建时间 desc, to_number(货主编码) asc, 业务类型 asc
;"""}

conf['''#######Used here to configure the logistics center and group name######'''] = {}
# # OUT IN ADJ
# # Status： 0-True  1-False
# # list1、出库 list2、入库 list3、调整单
conf['Group'] = {"dic": {"国药控股福建有限公司": ['0', '1', '1', '国控福建WMS/TMS上线群'],
                         "国药控股扬州有限公司": ['0', '1', '1', '国控江苏SAVE-TMS-WMS'],
                         "国药控股广东物流有限公司": ['0', '1', '1', '天天查单（广深'],
                         "国药控股常州有限公司": ['0', '1', '1', '国药常州WMS项目组'],
                         "国药控股四川医药股份有限公司": ['0', '1', '1', '国控四川系统沟通群'],
                         "国药控股云南有限公司": ['0', '1', '1', '云南TMS-SAVE-WMS运维'],
                         "国药物流有限责任公司": ['0', '1', '1', '国药物流三方货主维护'],
                         "国药集团医药物流有限公司": ['0', '1', '1', '国药物流三方货主维护'],
                         "国药控股温州有限公司": ['0', '1', '1', '国控温州SAVE-WMS运维群'],
                         "国药控股宁夏有限公司": ['0', '1', '1', '国控宁夏SAVE-WMS'],
                         "国药控股营口有限公司": ['0', '1', '1', '国控沈阳SAVE_WMS'],
                         "国药控股福州有限公司": ['0', '1', '1', '福州CMS-SAVE-WMS-TMS群'],
                         "国药控股朝阳有限公司": ['0', '1', '1', '国控沈阳SAVE_WMS'],
                         "国药控股山东有限公司": ['0', '1', '1', '国控山东SAVE_TMS_WMS'],
                         "国药控股海南有限公司": ['0', '1', '1', '国控海南SAVE_TMS_WMS'],
                         "国药控股湖南有限公司": ['0', '1', '1', '国控湖南SAVE-TMS-WMS'],
                         "国药控股广西物流有限公司": ['0', '0', '1', '国控广西SAVE_TMS_WMS'],
                         "国药控股苏州有限公司": ['0', '1', '1', '国控江苏SAVE-TMS-WMS'],
                         "国药控股天津物流有限公司": ['0', '1', '1', '国控天津、物流、平台'],
                         "国药控股南通有限公司": ['0', '1', '1', '国控南通SAVE_WMS运维'],
                         "国药控股泰州物流中心": ['0', '1', '1', '国控江苏SAVE-TMS-WMS'],
                         "国药控股湖北有限公司": ['0', '1', '1', '国控湖北物流信息系统'],
                         "国药乐仁堂医药有限公司": ['0', '1', '1', '乐仁堂SAVE/WMS/TMS运维'],
                         "国药集团西南医药有限公司": ['0', '1', '1', '国药西南SAVE/TMS项目群'],
                         "国药控股山西有限公司": ['0', '1', '1', '山西单据信息交流'],
                         "国药控股北京华鸿有限公司": ['0', '1', '1', '国控华鸿SAVE-TMS项目'],
                         "国药控股朝阳医疗器械有限公司": ['0', '1', '1', '国控沈阳SAVE_WMS'],
                         "国药控股河南股份有限公司": ['0', '1', '1', '河南TMS-SAVE-WMS运维'],
                         "国药控股沈阳有限公司": ['0', '1', '1', '国控沈阳SAVE_WMS'],
                         "国药集团新疆新特药业有限公司": ['0', '1', '1', '国药新疆信息系统运维'],
                         "苏州恒鼎物流有限公司": ['0', '1', '1', '恒鼎软件项目群'],
                         "国药控股陕西有限公司": ['0', '1', '1', '国控陕西信息群'],
                         "国药控股鲁南有限公司": ['0', '1', '1', '国控山东SAVE_TMS_WMS'],
                         "国药控股安徽有限公司": ['0', '1', '1', '安徽SAVE/WMS/TMS运维'],
                         "国药控股烟台有限公司": ['0', '1', '1', '国控山东SAVE_TMS_WMS'],
                         "国药控股江苏有限公司": ['0', '1', '1', '国控江苏SAVE-TMS-WMS'],
                         "国药集团新疆新特克拉玛依药业有限公司": ['0', '1', '1', '国药新疆信息系统运维'],
                         "国药控股吉林有限公司": ['0', '1', '1', '吉林赛飞、TMS交流群']}}

# # conf['Statistics'] = {"葵花药业集团医药有限公司": "葵花接口",
# #                       "gywl": "国药物流SAVE+WMS+TMS交流"}

conf['######Order processing mode configuration######'] = {}
# dictionary(赛飞卡单处理：key = 卡单原因, value = 处理方式)
conf['Method'] = {"dic1": {"网络或MA服务异常": "根据提供的“拣货单号”，在赛飞 “物流单”节点，点击 “下发wms” 重推单据至wms即可",
                           "库存量不足": "请先核对CMS、SAVE、WMS库存的 “数量” “状态” 以及 “库存供应商” 三个维度是否一致！",
                           "送货地址不允许为空": '''
对于送货方式为“送货”类型的订单必须要传入地址信息，因为TMS和WMS均需要该类信息才能正确地将订单送到客户手中。该类卡单处理有两种：
（1）货主取消订单重新下新的订单
（2）修改单据为自提后再保存提交单据（若单据需要进入TMS不可这么操作）''',
                           "批号不允许为空": '''
赛飞在接收非只运输的出库订单后会进行批号和库存的校验工作。
当出现该类卡单提示时，绝大部分原因是货主发了错误的批号给到平台，平台校验失败了。
请货主方一定要仔细核对入库批号信息哦~ ''',
                           "字段运输地址编码转换失败": '''
（1）因为地址基础资料未下发导致的卡单，在开飞平台‘货主客商’节点，根据卡单提示的编码查看该客商下是否有对应的值信息，如果没有请货主下发对应地址基础资料信息。
（2）货主下发地址基础档案后，请在赛飞平台‘货主客商’节点查看地址是否收到哈。
（3）若收到，请在委托单界面，点击‘修改’按钮填选对应地址信息后，点击‘提交’按钮后就能正常下发wms。''',
                           "字段交易包装单位转换失败": '''
（1）请到‘货主货品’节点查询该订单明细商品的‘出货包装单位’和‘交易包装单位’是否为空，若为空值，请到‘货主档案’节点下查询‘货品单位对码’信息中是否有‘顶’该对码值
（2）若没有该对码，请填写OA通知赛飞运维组、WMS运维组、TMS运维组（若该货主不实用tms则忽略）相关同事新增单位对码，待新增过后需货主重新维护商品上出货包装单位和交易包装单位字段并下发赛飞。查看商品上单位是否收到，若收到，请取消单据重新更换单号下发单据就完成啦~（注意一下哈：已下发的单据且在赛飞已生成的订单，货主方重新下发单据，赛飞订单是不会做任何更新的）''',
                           "并发操作,请重新提交": '''
（1）请到 “委托单节点” 点击 “刷新”按钮
（2）刷新后，请点击 “提交” 按钮即可，收到下发成功提示，则表明单据已生成物流单下发wms'''}}

conf['######GYWL Check order configuration######'] = {}
# # 单独配置
conf['Sinopharm'] = {"GYWL": [0, '国药物流SAVE+WMS+TMS交流']}

conf['######Tripartite Check order configuration######'] = {}
# # Status：0-True  1-False
# # key = custname、status、groupname
# # San_fang
conf['Stas'] = {"葵花药业集团医药有限公司": [0, '葵花接口'],
                "丽珠医药集团股份有限公司": [1, 'Test']}

conf['######Two parties Check order configuration######'] = {}
# # Er_fang
conf['Center'] = {"国药集团新疆新特克拉玛依药业有限公司": [0, '国药新疆信息系统运维'],
                  "国药集团新疆新特药业有限公司": [0, '国药新疆信息系统运维'],
                  "国药控股宁夏有限公司": [0, 'pyAuto']}

conf['######Excel temple title######'] = {}
# # excel temple title
conf['excel'] = {
    "title": ['货主名称', 'SAVE入库已收数量', 'SAVE出库已收数量', '入库已收订单号', '出库已收订单号', 'SAVE入库反馈数量', 'SAVE出库反馈数量', '入库反馈订单号',
              '出库反馈订单号', '截单时间'],
    "title1": ['运营中心标识', '明细', '总单', '创建时间', '货主编码', '货主编码物流', '货主名称', '仓库代码', '仓库名称', '业务类型', '送货方式', '运输方式', '运输时限要求',
               '原运输时限', '仓别编码']}

conf['######GYWL send name configuration####'] = {}
# # gywl send name
conf['Name'] = {"上海SAVE运维主管": [0, '平台-刘慧'],
                "全国SAVE运维": [0, '平台-周俊'],
                "ME": [1, 'shy']}

conf['######Thread polling time,Not recommended to modify!!!######'] = {}
# # Thread Timer clock
conf['Timer'] = {"allTime": 3,      # minutes
                 "khTime": 3,
                 "erpTime": 3,
                 "hrTime": 15,
                 "checkTime": 3,
                 "cleanTime": 1,    # hours
                 "alarmTime": 3}

conf['######Send time and center code configuration######'] = {}
# # Send time
# # center code
conf['Clock'] = {"clock_erp": ["12:00:00", "20:30:00"],
                 "clock_kh": ['11:30:00', '16:00:00'],
                 "clock_order": ['08:00:00', '20:40:00'],
                 "clock_all_out":
                     {"(131, 107)": "21:00:00",
                      "(102)": "12:00:00"}}

conf['######Log backup quantity configuration######'] = {}
# # log
conf['logBackCount'] = {"count": 7}

conf['Grafana'] = {"FE_SH_SAVE_RECEIVER": [0, '@刘慧', '国药物流赛飞运维组'],
                   "FE_GX_SAVE_RECEIVER": [0, '@总部--蔡赟', '国药物流赛飞运维组'],
                   "FE_GZ_SAVE_RECEIVER": [0, '@总部--蔡赟', '国药物流赛飞运维组'],
                   "FE_YZ_SAVE_RECEIVER": [0, '@shy', '国药物流赛飞运维组'],
                   "FE_SHSN_SAVE_RECEIVER": [0, '@刘慧', '国药物流赛飞运维组'],
                   "FE_SZ_SAVE_RECEIVER": [0, '@总部--蔡赟', '国药物流赛飞运维组'],
                   "FE_XJ_SAVE_RECEIVER": [0, '@总部--蔡赟', '国药物流赛飞运维组'],
                   "FE_HN_SAVE_RECEIVER": [0, '@周俊', '国药物流赛飞运维组'],
                   "FE_HB_SAVE_RECEIVER": [0, '@shy', '国药物流赛飞运维组'],
                   "FE_HN3_SAVE_RECEIVER": [0, '@shy', '国药物流赛飞运维组'],
                   "FE_SY_SAVE_RECEIVER": [0, '@shy', '国药物流赛飞运维组'],
                   "FE_GYSX_SAVE_RECEIVER": [0, '@总部--蔡赟', '国药物流赛飞运维组'],
                   "FE_LY_SAVE_RECEIVER": [0, '@周俊', '国药物流赛飞运维组'],
                   "FE_LLYTH_SAVE_RECEIVER": [0, '@总部--蔡赟', '国药物流赛飞运维组'],
                   "FE_JN_SAVE_RECEIVER": [0, '@周俊', '国药物流赛飞运维组'],
                   "FE_WM_SAVE_RECEIVER": [0, '@all', '国药物流赛飞运维组'],
                   "FE_YN_SAVE_RECEIVER": [0, '@周俊', '国药物流赛飞运维组'],
                   "GYKG_BMS_SAVE_RECEIVER": [0, '@all', '国药物流赛飞运维组'],
                   "FE_FZ_SAVE_RECEIVER": [0, '@总部--蔡赟', '国药物流赛飞运维组'],
                   "FE_XA1_SAVE_RECEIVER": [0, '@shy', '国药物流赛飞运维组'],
                   "FE_SX1_SAVE_RECEIVER": [0, '@总部--蔡赟', '国药物流赛飞运维组'],
                   "FE_JL_SAVE_RECEIVER": [0, '@shy', '国药物流赛飞运维组'],
                   "FE_HN2_SAVE_RECEIVER": [0, '@shy', '国药物流赛飞运维组'],
                   "FE_XNCD_SAVE_RECEIVER": [0, '@周俊', '国药物流赛飞运维组'],
                   "FE_FJ1_SAVE_RECEIVER": [0, '@总部--蔡赟', '国药物流赛飞运维组'],
                   "FE_FJ_SAVE_RECEIVER": [0, '@总部--蔡赟', '国药物流赛飞运维组'],
                   "FE_NT_SAVE_RECEIVER": [0, '@shy', '国药物流赛飞运维组'],
                   "FE_TJ_SAVE_RECEIVER": [0, '@周俊', '国药物流赛飞运维组'],
                   "FE_TS_SAVE_RECEIVER": [0, '@周俊', '国药物流赛飞运维组'],
                   "FE_NX_SAVE_RECEIVER": [0, '@shy', '国药物流赛飞运维组'],
                   "FE_WZ_SAVE_RECEIVER": [0, '@周俊', '国药物流赛飞运维组'],
                   "FE_AH1_SAVE_RECEIVER": [0, '@周俊', '国药物流赛飞运维组']}

conf['#####Automatic inspection and message related configuration######'] = {}
# # inspection time
conf['ins'] = {"t1": "00:00:00",
               "t2": "00:00:30",
               "week": "Sunday",
               "url_mq_copy": "http://10.32.11.45:3000/d/6BEM_T5Zk/mq-api-copy",
               "url_mq": "http://10.32.11.45:3000/d/7RKOkRZWk/mq-api",
               "url_oa": "https://oa.sinopharmholding.com/seeyon/main.do?method=main",
               "mess": """Grafana可视化监控服务发现异常队列：
MQ异常队列：{}
MQ异常信息：{}
MQ异常时间：{}
""",
               "order_mess": """赛飞订单拦截第{}条：（请各地及时处理）
卡单原因：{}
订单组号：{}
货主名称：{}
仓库名称：{}
单据类型：{}
订单日期：{}
处理方式：{}
""",
               "sf_jd_mess": """赛飞当日截单统计：
货主名称：{}
截单时间：{}
入库单接受数量：{}
出库单接受数量：{}
入库单反馈数量：{}
出库单反馈数量：{}
具体订单组号请查看文件
""",
               "ef_jd_mess": """赛飞当日截单统计：
运营中心：{}
截单时间：{}
明细数量：{}
总单数量：{}
具体详情请查看文件
""",
               "sh_sn_mess": """对单时间：{}
上海出库：{}
枢纽出库：{}
""",
               "erp_mess": """ERP task：
Query time：{}
ERP入库总数：{}
ERP入库明细数：{}
ERP出库总数：{}
ERP出库明细数：{}

SAVE入库总数：{}
SAVE入库明细数：{}
SAVE出库总数：{}
SAVE出库明细数：{}
""",
               "ots1": """
ERP对单结果数量不一致，请{}同学开启电脑，开始工作吧~ ^.^""",
               "ots2": """ERP对单数量不一致，后续上海、枢纽对单将不再核对，
已通知SAVE平台相关对单同事，并请其它平台对单同事及时核对、处理异常单据，谢谢~""",
               "method_mess": "~（当前类型数据未在dict中）",
               "title": "AMQ和缓存巡检报告{}~{}",
               "test": '''各位领导：

赛飞UAP:AMQ和缓存巡检报告
时间:{}~{}
赛飞UAP:AMQ服务巡检情况
总体状况:无明显异常
问题:无

目前:无

暂无其他异常
缓存服务
总体状况:无明显异常
问题:无

详情见附件

                                                                                                    Test By Walker
                                                                                                    {}'''}

with open('DevopsConf.ini', 'w') as devopsFile:
    conf.write(devopsFile)
