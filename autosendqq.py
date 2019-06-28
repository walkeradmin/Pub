# -*- coding:utf-8 -*-
# author: walker
# first： 2019-06-06
# second：2019-06-28

import cx_Oracle
import win32gui
from win32.lib import win32con
import win32clipboard as w
import time
import datetime
import pprint
import shelve

flag1, ia = 0, 0
shelFile = shelve.open('gywl')
user = shelFile['devOps']['user']
passWd = shelFile['devOps']['passwd']
ip = shelFile['devOps']['ip']
name = shelFile['devOps']['name']


def timer_fun(sched_time):
    flag = 0
    ii = 0
    while True:
        now = datetime.datetime.now()
        if sched_time < now < sched_time + datetime.timedelta(seconds=1):
            ii += 1
            if '08:00:00' <= time.strftime("%H:%M:%S") <= '20:00:00':
                print('Start pushing：', time.strftime("%Y-%m-%d %H:%M:%S %A"))
                print('')
                print('Start query for the' + ' ' + str(ii) + ' ' + 'time')
                print('')
                query()
                # time.sleep(1)
                flag = 1
            else:
                print('Current Time:', time.strftime("%H:%M:%S"), '\n',
                      'Time to stop pushing, the next query will start at 08:00 tomorrow morning\n\n\n')
                while True:
                    rit_now = time.strftime("%H:%M:%S")
                    if rit_now > '20:00:00' or ('00:00:00' <= rit_now < '08:00:00'):
                        pprint.pformat('')
                    else:
                        sched_time = datetime.datetime.now()
                        break
        else:
            if flag == 1:
                sched_time = sched_time + datetime.timedelta(minutes=3)
                flag = 0


def start_time():
    a, b, c, d = -1, -2, -3, -4
    global clock
    week = time.strftime("%A")
    if week == 'Monday':
        now_time = datetime.datetime.now()
        time_format = now_time.strftime('%Y-%m-%d')
        clock = time_format + ' ' + '00:00:01'
    elif week == 'Tuesday':
        now_time = datetime.datetime.now()
        change_time = now_time + datetime.timedelta(days=a)
        time_format = change_time.strftime('%Y-%m-%d')
        clock = time_format + ' ' + '00:00:01'
    elif week == 'Wednesday':
        now_time = datetime.datetime.now()
        change_time = now_time + datetime.timedelta(days=b)
        time_format = change_time.strftime('%Y-%m-%d')
        clock = time_format + ' ' + '00:00:01'
    elif week == 'Thursday':
        now_time = datetime.datetime.now()
        change_time = now_time + datetime.timedelta(days=c)
        time_format = change_time.strftime('%Y-%m-%d')
        clock = time_format + ' ' + '00:00:01'
    elif week == 'Friday':
        now_time = datetime.datetime.now()
        change_time = now_time + datetime.timedelta(days=d)
        time_format = change_time.strftime('%Y-%m-%d')
        clock = time_format + ' ' + '00:00:01'
        # Add a weekend start, judge the push time module, this module will not be called normally.
    elif week == 'Saturday':
        print('Rest on Saturday, the next push time will be held at 8:00 am next Monday.')
        clock = datetime.datetime.strptime(time.strftime("%Y-%m-%d 08:00:00"),
                                           "%Y-%m-%d %H:%M:%S") - datetime.timedelta(
            days=5)
        time1 = time.strftime("%Y-%m-%d %H:%M:%S")
        date1 = time.strftime("%Y-%m-%d 08:00:00")
        # print(date1)
        time2 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=2)
        sleep_time = int((time2 - datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")).total_seconds())
        time.sleep(sleep_time)
        timer_fun(datetime.datetime.now())
    elif week == 'Sunday':
        print('Rest on Sunday, the next push time will be held at 8:00 am next Monday.')
        clock = datetime.datetime.strptime(time.strftime("%Y-%m-%d 08:00:00"),
                                           "%Y-%m-%d %H:%M:%S") - datetime.timedelta(
            days=6)
        time11 = time.strftime("%Y-%m-%d %H:%M:%S")
        date11 = time.strftime("%Y-%m-%d 08:00:00")
        time22 = datetime.datetime.strptime(date11, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=1)
        sleep_time = int((time22 - datetime.datetime.strptime(time11, "%Y-%m-%d %H:%M:%S")).total_seconds())
        time.sleep(sleep_time)
        timer_fun(datetime.datetime.now())
    return clock


def send_qq(result, name):
    # message format
    num = "".join(result[:1])
    cause = "".join(result[1:2])
    or_id = "".join(result[2:3])
    owner = "".join(result[3:4])
    depot = "".join(result[4:5])
    or_ty = "".join(result[5:6])
    send_mess = '赛飞订单拦截第' + num + '条：' + '''
卡单原因：''' + cause + '''
订单组号：''' + or_id + '''
货主名称：''' + owner + '''
仓库名称：''' + depot + '''
单据类型：''' + or_ty + '''
'''
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, send_mess)
    w.CloseClipboard()
    # time wait pywintypes.error: (1418, 'GetClipboardData',线程没有打开的剪贴板)
    time.sleep(1)
    handle = win32gui.FindWindow(None, name)
    if 1 == 1:
        win32gui.SendMessage(handle, 770, 0, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


def query():
    a, a1, b, c, d, di, e, fn, g, h, j, k, li, m, n, ed, ex, eh, ej, ez, ef, ez1, eb, et, em, ec = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ehn, yk, ewz, esd, e_lrt, etj, eln, ejf, ejn, exn, eyg, ety, eyn, eyt, ehd = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    sql1 = ""
    cursor.execute(sql1)
    rows = cursor.fetchall()
    while True:
        global flag1
        if flag1 == 0:
            # For example
            print('河南卡单:' + '\n')
            for i in range(len(rows)):
                tuple1 = rows[i]
                if '河南' in tuple1[3] and '葵花' not in tuple1[2] and '入库' not in tuple1[5]:
                    a += 1
                    hn = list(tuple1)
                    hn.insert(0, (str(a)))
                    result = tuple(hn)
                    print(result)
                    # sendqq(result, 'test1')
                    send_qq(result, '河南TMS-SAVE-WMS运维')
            print('')
            # time.sleep(1)
            print('葵花卡单:' + '\n')
            for i in range(len(rows)):
                tuple1 = rows[i]
                if '葵花' in tuple1[2] and '入库' not in tuple1[5]:
                    a1 += 1
                    kh = list(tuple1)
                    kh.insert(0, (str(a1)))
                    result = tuple(kh)
                    print(result)
                    # sendqq(result, '芯')
                    send_qq(result, '葵花接口')
            print('')
            # time.sleep(1)
            flag1 = 1
        else:
            print('Latest data volume：', len(rows), '\n')
            print('Number of historical data：', len(his_rows), '\n')
            f = open('log.txt', 'w+', encoding='utf-8')
            f.write(str(his_rows))
            f.close()
            check = list(set(tuple(rows)).difference(set(tuple(his_rows))))
            if check:
                his_rows.extend(check)
                rows = check
                flag1 = 0
            else:
                global ia
                ia += 1
                if ia == 1:
                    print('')
                    break
                else:
                    print('')
                    print(
                        'Result：The query results are the same as the previous result, '
                        'eliminating the need to perform a send task and preparing for a new round of queries\n\n\n')
                    break


conn = cx_Oracle.connect(user+'/'+passWd+'@'+ip+'/'+name)
cursor = conn.cursor()
sql = ""
cursor.execute(sql)
his_rows = cursor.fetchall()


if __name__ == '__main__':
    print('Sql query time :', start_time())
    sched_time = datetime.datetime.now()
    timer_fun(sched_time)
