# -*- coding:utf-8 -*-
# author： walker
# time：2019-07-12/13/15/17/23

import cx_Oracle
import win32gui
import win32api
from win32.lib import win32con
import win32clipboard as w
import time
import datetime
import shelve
import os
import threading
from threading import Timer, Semaphore, Thread, Lock
import ctypes
from ctypes import wintypes
import pythoncom
import logformat
import requests
import json
import configparser
import ast
import traceback

# sem = Semaphore(1)
# Turn capital
# class MyConf(configparser.ConfigParser):
#     def __init__(self, defaults=None):
#         configparser.ConfigParser.__init__(self, defaults=None)
#
#     def optionxform(self, optionstr):
#         return optionstr


def deploy():
    conf_file = os.path.join(os.getcwd(), 'DevopsConf.ini')
    cp = configparser.ConfigParser()
    cp.read(conf_file)
    return cp


thread_handle, check_c, flag1, ia, fre = 0, 0, 0, 0, 0
d = deploy().get('Group', 'dic')
dic = ast.literal_eval(d)
Met = eval(deploy().get('Method', 'dic1'))
statistics = deploy().items('Statistics')
clean_time = eval(deploy().get('Timer', 'cleanTime'))
check_time = eval(deploy().get('Timer', 'checkTime'))
file = shelve.open('gywl')
user = file['devOps']['user']
password = file['devOps']['passwd']
ip = file['devOps']['ip']
name = file['devOps']['name']


class ORDER:
    def __init__(self):
        self._clock_order = eval(deploy().get('Clock', 'clock_order'))
        self._allTime = eval(deploy().get('Timer', 'allTime'))
        # self._folderAll = deploy().get('Path', 'folderAll')
        self._folderAll = os.getcwd() + "\\formatLogs\\allFileLog\\"
        self._a, self._b, self._c, self._d, self._e, self._f = -1, -2, -3, -4, -5, -6
        self._mutex = Lock()
        self._sql_all_1 = deploy().get('SQL', 'order_all')
        self._sql_ma_1 = deploy().get('SQL', 'order_ma')

    def timer_all(self):
        now = time.strftime("%H:%M:%S")
        week = time.strftime("%a")
        if self._clock_order[0] <= now <= self._clock_order[1] and week != 'Sat' and week != 'Sun':
            self.query()
        else:
            log().info('Order：Time to stop pushing, the next query will start at 08:00 tomorrow morning')
        global timer1
        timer1 = Timer(self._allTime, self.timer_all)
        timer1.start()

    def start_time(self):
        global clock
        week = time.strftime("%A")
        if week == 'Monday':
            now_time = datetime.datetime.now()
            time_format = now_time.strftime('%Y-%m-%d')
            clock = time_format + ' ' + '00:00:00'
        elif week == 'Tuesday':
            now_time = datetime.datetime.now()
            change_time = now_time + datetime.timedelta(days=self._a)
            time_format = change_time.strftime('%Y-%m-%d')
            clock = time_format + ' ' + '00:00:00'
        elif week == 'Wednesday':
            now_time = datetime.datetime.now()
            change_time = now_time + datetime.timedelta(days=self._b)
            time_format = change_time.strftime('%Y-%m-%d')
            clock = time_format + ' ' + '00:00:00'
        elif week == 'Thursday':
            now_time = datetime.datetime.now()
            change_time = now_time + datetime.timedelta(days=self._c)
            time_format = change_time.strftime('%Y-%m-%d')
            clock = time_format + ' ' + '00:00:00'
        elif week == 'Friday':
            now_time = datetime.datetime.now()
            change_time = now_time + datetime.timedelta(days=self._d)
            time_format = change_time.strftime('%Y-%m-%d')
            clock = time_format + ' ' + '00:00:00'
        elif week == 'Saturday':
            now_time = datetime.datetime.now()
            change_time = now_time + datetime.timedelta(days=self._e)
            time_format = change_time.strftime('%Y-%m-%d')
            clock = time_format + ' ' + '00:00:00'
        elif week == 'Sunday':
            now_time = datetime.datetime.now()
            change_time = now_time + datetime.timedelta(days=self._f)
            time_format = change_time.strftime('%Y-%m-%d')
            clock = time_format + ' ' + '00:00:00'
        return clock

    def send(self, send_mess, group_name):
        self._mutex.acquire()
        # log().info('The clipboard is locked')
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, send_mess)
        w.CloseClipboard()
        # time wait 防止报错 pywintypes.error: (1418, 'GetClipboardData',线程没有打开的剪贴板)
        time.sleep(1)
        # TXGuiFoundation None
        handle = win32gui.FindWindow('TXGuiFoundation', group_name)
        win32gui.SendMessage(handle, 770, 0, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        log().info('Group {} successfully sent the task'.format(group_name))
        self._mutex.release()
        # log().info('Clipboard is unlocked')

    def format_mess_all(self, result, group_name):
        num = "".join(result[:1])       # index + 1
        cause = "".join(result[1:2])
        or_id = "".join(result[2:3])
        ow = "".join(result[3:4])
        depot = "".join(result[4:5])
        or_ty = "".join(result[5:6])
        or_time = "".join(result[7:8])
        global method
        if any(i in cause for i in Met.keys()):
            for k, v in Met.items():
                if k in cause:
                    method = v
        else:
            method = '~（当前类型数据未在dict中）'
        send_mess = '赛飞订单拦截第' + num + '条：（请各地及时处理）' + '''
卡单原因：''' + cause + '''
订单组号：''' + or_id + '''
货主名称：''' + ow + '''
仓库名称：''' + depot + '''
单据类型：''' + or_ty + '''
订单日期：''' + or_time + '''
处理方式：{}
'''.format(method)
        self.send(send_mess, group_name)

    def query(self):
        global fre
        fre += 1
        push_time = time.strftime("%Y-%m-%d %H:%M:%S %A")
        day = time.strftime("%Y-%m-%d 00:00:00")
        log().info('Sql query time：' + self.start_time())
        log().info('Start pushing：' + push_time)
        log().info('Start query for the：' + str(fre) + ' time')
        obj5 = Oracle()
        try:
            rows_all = obj5.execute_sql(self._sql_all_1.format(self.start_time(), self.start_time(), self.start_time()))
            rows_ma = obj5.execute_sql(self._sql_ma_1.format(day))
        except Exception as e:
            log().info('Check query，MSG{}'.format(str(e)))
        else:
            obj5.close()
            rows_all.extend(rows_ma)
        while True:
            global flag1
            if flag1 == 0:
                for k, v in dic.items():
                    count1, count2, count3 = 0, 0, 0
                    for i in rows_all:
                        tuple1 = i
                        if k in tuple1[7] and v[0] == '0' and v[1] == '1' and v[2] == '1' and '委托入库' not in tuple1[5] and '物流调整' not in tuple1[5]:  # only out order
                            count1 += 1
                            order1 = list(tuple1)
                            order1.insert(0, str(count1))
                            result1 = tuple(order1)
                            log().info(k + '卡单')
                            log().info(result1)
                            self.format_mess_all(result1, v[3])
                        if k in tuple1[7] and v[0] == '0' and v[1] == '0' and v[2] == '1'and '物流调整' not in tuple1[5]:  # oder out in
                            count2 += 1
                            order2 = list(tuple1)
                            order2.insert(0, str(count2))
                            result2 = tuple(order2)
                            log().info(k + '卡单')
                            log().info(result2)
                            self.format_mess_all(result2, v[3])
                        if k in tuple1[7] and v[0] == '0' and v[1] == '0' and v[2] == '0':  # out in adj
                            count3 += 1
                            order3 = list(tuple1)
                            order3.insert(0, str(count3))
                            result3 = tuple(order3)
                            log().info(k + '卡单')
                            log().info(result3)
                            self.format_mess_all(result3, v[3])
                flag1 = 1
            else:
                log().info('Order：Latest data volume：' + str(len(rows_all)))
                log().info('Order：Number of historical data：' + str(len(his_rows_all)))
                if not os.path.exists(self._folderAll):
                    os.makedirs(self._folderAll)
                # os.chdir(self._folderAll)
                day = time.strftime("%Y-%m-%d")
                f = open(self._folderAll + 'log_all_%s.txt' % day, 'w+', encoding='utf-8')
                f.write(str(his_rows_all))
                f.close()
                check = list(set(tuple(rows_all)).difference(set(tuple(his_rows_all))))
                if check:
                    his_rows_all.extend(check)
                    rows_all = check
                    flag1 = 0
                else:
                    global ia
                    ia += 1
                    if ia == 1:  # first query
                        break
                    else:
                        log().info(
                            'Order；The query results are the same as the previous result, '
                            'eliminating the need to perform a send task and preparing for a new round of queries')
                        break

    def query_his(self):
        global his_rows_all
        global his_rows_ma
        obj4 = Oracle()
        his_rows_all = obj4.execute_sql(self._sql_all_1.format(self.start_time(), self.start_time(), self.start_time()))
        his_rows_ma = obj4.execute_sql(self._sql_ma_1.format(self.start_time()))
        his_rows_all.extend(his_rows_ma)    # merge
        obj4.close()


class DROP(ctypes.Structure):
    _fields_ = (('pFiles', wintypes.DWORD),
                ('pt',     wintypes.POINT),
                ('fNC',    wintypes.BOOL),
                ('fWide',  wintypes.BOOL))


class FILE:
    def __init__(self):
        self._clock_kh = eval(deploy().get('Clock', 'clock_kh'))
        # self._folderKh = deploy().get('Path', 'folderKh')
        self._folderKh = os.getcwd() + "\\formatLogs\\khFileLog\\"
        self._khTime = eval(deploy().get('Timer', 'khTime'))
        self._info1 = 'Copying to clipboard, filename：'
        self._info2 = 'CLIP_FILE task perform succeed'
        self._info3 = 'KH：Run send file task'
        self._sql1 = deploy().get('SQL', 'sql1')
        self._sql2 = deploy().get('SQL', 'sql2')
        self._sql3 = deploy().get('SQL', 'sql3')
        self._sql4 = deploy().get('SQL', 'sql4')

    def clip_files(self, file_list):
        offset = ctypes.sizeof(DROP)
        length = sum(len(p) + 1 for p in file_list) + 1
        size = offset + length * ctypes.sizeof(ctypes.c_wchar)
        buf = (ctypes.c_char * size)()
        df = DROP.from_buffer(buf)
        df.pFiles, df.fWide = offset, True
        for path in file_list:
            log().info(self._info1 + path)
            array_t = ctypes.c_wchar * (len(path) + 1)
            path_buf = array_t.from_buffer(buf, offset)
            path_buf.value = path
            offset += ctypes.sizeof(path_buf)
        stg = pythoncom.STGMEDIUM()
        stg.set(pythoncom.TYMED_HGLOBAL, buf)
        w.OpenClipboard()
        w.EmptyClipboard()
        try:
            w.SetClipboardData(w.CF_HDROP, stg.data)
            log().info(self._info2)
        finally:
            w.CloseClipboard()

    def copy_file_to_clipboard(self, filename):
        self.clip_files([os.path.abspath(filename)])

    def format_mess_file(self, out_rec, out_feed, in_rec, in_feed, group_name, cut_name):
        global tup_out_rec, feed_num_out, feed_id_out, rec_num_in, feed_num_in, rec_id_in, feed_id_in
        if out_rec:
            rec_out = list()
            for i1 in out_rec:
                tup_out_rec = i1
                rec_out.extend(tup_out_rec[1:2])
            rec_num_out = len(rec_out)
            rec_id_out = ','.join(rec_out)
        else:
            rec_num_out = 0
            rec_id_out = '未收到出库订单'
        if out_feed:
            feed_out = list()
            for i2 in out_feed:
                tup_out_feed = i2
                feed_out.extend(tup_out_feed[1:2])
                # filename = tup_out_feed[2:3]
            feed_num_out = len(feed_out)
            feed_id_out = ','.join(feed_out)
        else:
            feed_num_out = 0
            feed_id_out = '未收到wms出库关单反馈'
        if in_rec:
            rec_in = list()
            for i3 in in_rec:
                tup_in_rec = i3
                rec_in.extend(tup_in_rec[1:2])
            rec_num_in = len(rec_in)
            rec_id_in = ','.join(rec_in)
        else:
            rec_num_in = 0
            rec_id_in = '未收到入库订单'
        if in_feed:
            feed_in = list()
            for i4 in in_feed:
                tup_in_feed = i4
                feed_in.extend(tup_in_feed[1:2])
            feed_num_in = len(feed_in)
            feed_id_in = ','.join(feed_in)
        else:
            feed_num_in = 0
            feed_id_in = '未收到wms入库关单反馈'
        s_time = time.strftime("%Y-%m-%d %H:%M:%S")
        send_mess = '''赛飞当日截单统计:''' + '''
货主名称：''' + cut_name + '''
截止时间：''' + s_time + '''

出库截单统计：''' + '''
已收订单数量：''' + str(rec_num_out) + '''
反馈订单数量：''' + str(feed_num_out) + '''
已收订单组号：''' + rec_id_out + '''
反馈订单组号：''' + feed_id_out + '''

入库截单统计：''' + '''
已收订单数量：''' + str(rec_num_in) + '''
反馈订单数量：''' + str(feed_num_in) + '''
已收订单组号：''' + rec_id_in + '''
反馈订单组号：''' + feed_id_in + '''


'''
        if not os.path.exists(self._folderKh):
            os.makedirs(self._folderKh)
        # os.chdir(self._folderKh)
        day = time.strftime("%Y-%m-%d")
        f = open(self._folderKh + 'KH_JD_%s.txt' % day, 'a+', encoding='utf-8')
        f.write(send_mess)
        f.close()
        log().info(send_mess)
        send = ORDER()
        send.send(send_mess, group_name)
        log().info('Send messages to groups：{}'.format(group_name))

    def send_file(self, group_name):
        log().info(self._info3)
        win = win32gui.FindWindow('TXGuiFoundation', group_name)
        time.sleep(1)
        win32api.PostMessage(win, win32con.WM_PASTE, 0, 0)
        time.sleep(1)
        win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    def query_kh(self):
        try:
            log().info('KH：Run query task')
            create_time = time.strftime("%Y-%m-%d 00:00:01")
            obj4 = Oracle()
            out_rec = obj4.execute_sql(self._sql1.format(create_time))
            out_feed = obj4.execute_sql(self._sql2.format(create_time))
            in_rec = obj4.execute_sql(self._sql3.format(create_time))
            in_feed = obj4.execute_sql(self._sql4.format(create_time))
            obj4.close()
            # This function can also be refined into a flexible configuration
            global owner_name, group1
            if out_rec:
                owner_name = statistics[0][0]
                group1 = statistics[0][1]
            elif out_feed:
                owner_name = statistics[0][0]
                group1 = statistics[0][1]
            elif in_rec:
                owner_name = statistics[0][0]
                group1 = statistics[0][1]
            elif in_feed:
                owner_name = statistics[0][0]
                group1 = statistics[0][1]
            log().info('[{}] [{}] [{}] [{}] [{}] [{}]'.format(out_rec, out_feed, in_rec, in_feed, group1, owner_name))
            self.format_mess_file(out_rec, out_feed, in_rec, in_feed, group1, owner_name)
            day = time.strftime("%Y-%m-%d")
            file_name = self._folderKh + 'KH_JD_%s.txt' % day
            self.copy_file_to_clipboard(file_name)
            check = []
            if in_rec == check and in_feed == check and out_rec == check and out_feed == check:
                log().info('KH：Did not query any data,no need to perform a send task')
            else:
                self.send_file(group1)
        except:
            log().error(str(traceback.format_exc()))

    def timer_kh(self):
        date = time.strftime("%A")
        now = datetime.datetime.now()
        if date == 'Saturday' or date == 'Sunday':
            log().info('KH：Do not perform tasks on weekends')
        else:
            for i in self._clock_kh:
                send_time = time.strftime("%Y-%m-%d {}".format(i))
                of_time = datetime.datetime.strptime(send_time, "%Y-%m-%d %H:%M:%S")
                # 11:30:00.xx < x < 11:31:00.xx
                # 16:00:00.xx < x < 16:01:00.xx
                if of_time < now < of_time + datetime.timedelta(minutes=1):
                    self.query_kh()
                else:
                    log().info('KH：Do not perform tasks during non-working hours')
        global timer2
        timer2 = Timer(self._khTime, self.timer_kh)
        timer2.start()


class SH:
    def __init__(self):
        self._clock_erp = deploy().get('Clock', 'clock_erp')
        self._erpTime = eval(deploy().get('Timer', 'erpTime'))
        self._hrTime = eval(deploy().get('Timer', 'hrTime'))
        # self._folderErp = deploy().get('Path', 'folderErp')
        self._folderErp = os.getcwd() + "\\formatLogs\\erpLog\\"
        self._mess = '辉瑞卡单，请及时处理'
        self._sql_sh = deploy().get('SQL', 'sql_sh')
        self._sql_sn = deploy().get('SQL', 'sql_sn')
        self._db_link = deploy().get('SQL', 'db_link')
        self._sql_erp = deploy().get('SQL', 'sql_erp')
        self._sql_feed = deploy().get('SQL', 'sql_feed')
        self._name = deploy().get('Name', '上海SAVE运维主管')

    def timer_erp(self):
        date = time.strftime("%A")  # %a
        if date == 'Saturday' or date == 'Sunday':
            log().info('ERP：Do not perform tasks on weekends')
        else:
            now = datetime.datetime.now()
            send_time = time.strftime("%Y-%m-%d " + self._clock_erp)
            range_time = datetime.datetime.strptime(send_time, "%Y-%m-%d %H:%M:%S")
            # 08:30:00.xx < x < 08:31:00.xx
            if range_time < now < range_time + datetime.timedelta(minutes=1):
                self.erp()
            else:
                log().info('ERP：Do not perform send task(08:30:00)')
        global timer3
        timer3 = Timer(self._erpTime, self.timer_erp)
        timer3.start()

    def timer_hr(self):
        range_time1 = datetime.datetime.now()
        date = time.strftime("%A")  # %a
        if date == 'Saturday' or date == 'Sunday':
            log().info('HR：Do not perform tasks on weekends')
        else:
            now = datetime.datetime.now()
            if range_time1 <= now < range_time1 + datetime.timedelta(seconds=1):
                self.check_feed()
        global timer4
        timer4 = Timer(self._hrTime, self.timer_hr)
        timer4.start()

    def format_sh_sn(self, sh_num, sn_num):
        mess = '''对单时间：''' + time.strftime("%Y-%m-%d %H:%M:%S") + '''
    
上海出库：''' + str(sh_num) + '''
枢纽出库：''' + str(sn_num) + '''

'''
        send = ORDER()
        send.send(mess, statistics[1][1])
        log().info('SH-SN ORDER RESULT---上海出库：' + str(sh_num) + '枢纽出库：' + str(sn_num))
        if not os.path.exists(self._folderErp):
            os.makedirs(self._folderErp)
        # os.chdir(self._folderErp)
        file_now = time.strftime("%Y-%m-%d")
        f = open(self._folderErp + 'Check_Order%s.txt' % file_now, 'w+', encoding='utf-8')
        f.write(mess)
        f.close()

    def format_erp(self, result):
        erp_quantity = result[0]
        erp_in = erp_quantity[1]
        erp_in_del = erp_quantity[2]
        erp_out = erp_quantity[3]
        erp_out_del = erp_quantity[4]
        save_quantity = result[1]
        save_in = save_quantity[1]
        save_in_del = save_quantity[2]
        save_out = save_quantity[3]
        save_out_del = save_quantity[4]
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        mess = '''ERP task：
Query time：''' + now + '''
Query Result：{}
ERP入库总数：''' + str(erp_in) + '''
ERP入库明细数：''' + str(erp_in_del) + '''
ERP出库总数：''' + str(erp_out) + '''
ERP出库明细数：''' + str(erp_out_del) + '''

SAVE入库总数：''' + str(save_in) + '''
SAVE入库明细数：''' + str(save_in_del) + '''
SAVE出库总数：''' + str(save_out) + '''
SAVE出库明细数：''' + str(save_out_del)
        if erp_in == save_in and erp_in_del == save_in_del and erp_out == save_out and erp_out_del == save_out_del:
            log().info(mess)
            if not os.path.exists(self._folderErp):
                os.makedirs(self._folderErp)
            # os.chdir(self._folderErp)
            file_now = time.strftime("%Y-%m-%d")
            f = open(self._folderErp + 'ERP_SH_SN%s.txt' % file_now, 'w+', encoding='utf-8')
            f.write(mess.format('ERP == SAVE'))
            f.close()
            self.order_sh_sn()
        else:
            mess1 = mess.format('ERP != SAVE') + '''

哎呀!真是不走运呢~ ERP对单结果数量存在不一致，请xxx同学开启电脑，开始工作吧~ ^.^
'''
            log().info('ERP != SAVE---Send data results to LiuHui')
            log().info(mess)
            send = ORDER()
            send.send(mess1, self._name)  # 上海SAVE运维主管
            if not os.path.exists(self._folderErp):
                os.makedirs(self._folderErp)
            file_now = time.strftime("%Y-%m-%d")
            f = open(self._folderErp + 'ERP_SH_SN%s.txt' % file_now, 'w+', encoding='utf-8')
            f.write(mess)
            f.close()

    def format_hr(self, feed_rows):
        if feed_rows:
            send = ORDER()
            send.send(self._mess, self._name)    # 上海SAVE运维主管
            log().info(
                'HR task result：' + str(feed_rows) + 'Query the data, please handle it in time,re-query after one hour')
        else:
            log().info('HR task result：' + str(feed_rows) + 'No data was found, re-query after one hour')

    def order_sh_sn(self):
        make_time = time.strftime("%Y-%m-%d 00:00:00")
        obj3 = Oracle()
        sh_rows = obj3.execute_sql(self._sql_sh.format(make_time))
        sh_num = (sh_rows[0])[0]
        sn_rows = obj3.execute_sql(self._sql_sn.format(make_time))
        sn_num = (sn_rows[0])[0]
        obj3.close()
        self.format_sh_sn(sh_num, sn_num)

    def erp(self):
        obj2 = Oracle()
        obj2.execute_sql(self._db_link)
        erp_rows = obj2.execute_sql(self._sql_erp)
        obj2.close()
        self.format_erp(erp_rows)

    def check_feed(self):
        obj1 = Oracle()
        feed_rows = obj1.execute_sql(self._sql_feed)
        obj1.close()
        self.format_hr(feed_rows)


class Oracle:
    def __init__(self):
        self.user = user
        self.password = password
        self.ip = ip
        self.name = name
        self.conn = None
        self.cursor = None
        self.isClose = True

    def connect(self):          # connect
        try:
            self.conn = cx_Oracle.connect(self.user+'/'+self.password+'@'+self.ip+'/'+self.name)
            self.cursor = self.conn.cursor()
            self.isClose = False
        except Exception as e:
            log().error(
                "Oracle connect error![MSG={},USER={},PASSWORD={},IP={},NAME={}]".format(str(e), self.user,
                                                                                         self.password, self.ip,
                                                                                         self.name))
            self.cursor = None
            self.isClose = True
        return self.cursor

    def is_connect(self):           # connected or not
        if self.cursor is not None:
            return True
        else:
            return False

    def close(self):                # close oracle connect
        self.cursor.close()
        self.conn.close()
        self.isClose = True

    def execute_sql(self, sql):     # execute fetchall
        if not self.is_connect():
            self.connect()          # True = Not False
            num = 0
            for i in range(3):      # judge 3 time
                num += 1
                if not self.is_connect():
                    self.connect()
                    log().info('Try to reconnect to the database for the {} time'.format(str(num)))
                    time.sleep(1)
                else:
                    break
        else:                       # False = Not True
            pass
        try:
            self.cursor.execute(sql)
            if 'declare begin' in sql:
                pass
            else:
                global sql_rows
                sql_rows = self.cursor.fetchall()
        except Exception as e:
            log().error("Execute sql error![MSG={},SQL={}]".format(str(e), sql))
            # check_thread(str(e))
            return ''
            # return None
        else:
            return sql_rows


# Do not use
class EXEC(object):
    def __init__(self, thread):
        self.thread_handle = thread_handle
        print('thread_handle----', self.thread_handle)
        self.thread_handle = thread

    def __del__(self):
        global gfa
        gfa = 0
        log().info('Thread termination{}'.format(gfa))
        self.thread_handle.cancel()


def log():
    lg = logformat.Logger(logger='AutoThread', filename='AutoThread')
    return lg


class Comp(object):
    def __init__(self, touser, message):
        self._comp_id = "wwca9e177a69dcdecc"
        self._secret = "x8G9ve4HZr3EDUjz8NfX5xZUCsDpwuo3E_KV_MDz27g"
        self._agent_id = 1000003
        self._token = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + self._comp_id + '&corpsecret=' + self._secret
        self._touser = touser
        self._message = message

    def conn(self):
        try:
            request = requests.get(self._token)
            access_token = request.json()['access_token']
        except Exception as e:
            log().info(str(e))
        else:
            global msg_url
            msg_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
        return msg_url

    def format(self):

        params = {"touser": self._touser,
                  # "toparty": toparty,
                  "msgtype": "text",
                  "agentid": self._agent_id,
                  "text": {"content": self._message},
                  "safe": 0
                  }
        return params

    def post(self):
        try:
            requests.post(self.conn(), data=json.dumps(self.format()))
        except Exception as e:
            log().info(str(e))
        else:
            log().info(
                'Sending a successful company WeChat' + 'sendto：' + self._touser + ';;message：' + self._message)


def restore(msg, thread_count):
    log().info('Restore MSG [{}]'.format(msg))
    # thread_count = threading.active_count()
    now = datetime.datetime.now()
    sendto = '@all'
    mess0 = '''Error：autoThread.py 
Mess：Thread stopped abnormally
Current：number of threads {}
Actually：number of threads 7
Details：{}
Time：{}'''
    mess1 = '''Mess：Start executing thread recovery tasks
Time：{}'''
    mess2 = '''Mess：Thread recovery succeeded
Time：{}'''
    mess3 = '''Error：Thread recovery failed
Time：{}'''
    if thread_count < 7 and 'ORA-' in msg:
        log().info('Determine that the thread is in an abnormal situation and start performing the recovery task.')
        obj0 = Comp(sendto, mess0.format(thread_count, msg, now))
        obj0.post()
        time.sleep(1)
        obj1 = Comp(sendto, mess1.format(datetime.datetime.now()))
        obj1.post()
        try:
            order = ORDER()
            thread1 = Thread(target=order.timer_all, name='OrderAll')
            thread1.start()
            thread1.join()
        except Exception as e:
            log().error('重启线程异常情况：{}'.format(str(e)))
        else:
            count = threading.active_count()
            if count == 7:
                obj2 = Comp(sendto, mess2.format(datetime.datetime.now()))
                obj2.post()
            else:
                obj3 = Comp(sendto, mess3.format(datetime.datetime.now()))
                obj3.post()


def check_thread():
    global check_c
    check_c += 1
    thread_enu = threading.enumerate()
    thread_count = threading.active_count()
    log().info('Check Thread：{}'.format(thread_enu))
    log().info('Check Thread alive count：{}'.format(thread_count))
    mess = '''Error：autoThread.py 
Mess：Thread stopped abnormally
Current：number of threads {}
Actually：number of threads 7
Time：{}'''
    if thread_count < 7 and check_c != 1:
        log().error('The program thread has an exception, now the number of threads is {}'.format(thread_count))
        mess1 = mess.format(thread_count, datetime.datetime.now())
        obj1 = Comp('@all', mess1)
        obj1.post()
        # restore(thread_count)
    else:
        if thread_count > 7:
            mess2 = mess.format(thread_count, datetime.datetime.now())
            obj2 = Comp('@all', mess2)
            obj2.post()
    global timer5
    timer5 = Timer(check_time, check_thread)
    timer5.start()


def clean_screen():
    os.system('cls')
    log().info('Clear screen task execution completed')
    global timer6
    timer6 = Timer(clean_time, check_thread)
    timer6.start()


def main():
    # sem.acquire()
    order = ORDER()
    file_kh = FILE()
    sh_save = SH()
    order.query_his()
    thread_list = list()
    thread1 = Thread(target=order.timer_all, name='OrderAll')
    thread2 = Thread(target=file_kh.timer_kh, name='KuaHua')
    thread3 = Thread(target=sh_save.timer_erp, name='ERP')
    thread4 = Thread(target=sh_save.timer_hr, name='HuiRui')
    thread5 = Thread(target=check_thread, name='CheckThread')
    thread6 = Thread(target=clean_screen, name='CleanScreen')
    thread_list.append(thread1)
    thread_list.append(thread2)
    thread_list.append(thread3)
    thread_list.append(thread4)
    thread_list.append(thread5)
    thread_list.append(thread6)
    for s in thread_list:
        s.start()
        s.join()


if __name__ == '__main__':
    print('''
-------------------------------------------------------------------------------------------------
|The task starts executing and is checking whether the current time meets the task requirements.|
|1.The All owner mission is performed from 8:00 to 20:00.                                       | 
|2.The HeNan MA  mission is performed from 8:00 to 20:00.                                       |
|3.The KH task first push time on 11:30:00 and the second push time on 16:00:00.                |
|4.The erp|sh|sn mission is performed at 8 o'clock every night.                                 |
|5.The HuiRui mission is performed every seconds.                                               |                
-------------------------------------------------------------------------------------------------''')
    main()
