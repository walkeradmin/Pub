# -*- coding:utf-8 -*-
# author:walker

import cx_Oracle
import win32gui
from win32.lib import win32con
import win32clipboard as w
import time
import datetime
import pprint


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
                time.sleep(1)
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
                sched_time = sched_time + datetime.timedelta(minutes=1)
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
        change_time = now_time + datetime.timedelta(days=c)
        time_format = change_time.strftime('%Y-%m-%d')
        clock = time_format + ' ' + '00:00:01'
        # Add a weekend start, judge the push time module, this module will not be called normally.
    elif week == 'Saturday':
        print('Rest on Saturday, the next push time will be held at 8:00 am next Monday.')
        time1 = time.strftime("%Y-%m-%d %H:%M:%S")
        date1 = time.strftime("%Y-%m-%d 08:00:00")
        # print(date1)
        time2 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=2)
        sleep_time = int((time2 - datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")).total_seconds())
        time.sleep(sleep_time)
        timer_fun(datetime.datetime.now())
    elif week == 'Sunday':
        print('Rest on Sunday, the next push time will be held at 8:00 am next Monday.')
        time11 = time.strftime("%Y-%m-%d %H:%M:%S")
        date11 = time.strftime("%Y-%m-%d 08:00:00")
        time22 = datetime.datetime.strptime(date11, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=1)
        sleep_time = int((time22 - datetime.datetime.strptime(time11, "%Y-%m-%d %H:%M:%S")).total_seconds())
        time.sleep(sleep_time)
        timer_fun(datetime.datetime.now())
    return clock


def sendqq(result, name):
    # message format
    num = "".join(result[:1])
    cause = "".join(result[1:2])
    or_id = "".join(result[2:3])
    owner = "".join(result[3:4])
    depot = "".join(result[4:5])
    or_ty = "".join(result[5:])
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
    handle = win32gui.FindWindow(None, name)
    if 1 == 1:
        win32gui.SendMessage(handle, 770, 0, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


def query():
    a, a1, b, c, d, di, e, f, g, h, j, k, li, m, n = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    sql1 = ""
    cursor.execute(sql1)
    rows = cursor.fetchall()
    while True:
        global flag1
        if flag1 == 0:
            print('河南卡单:' + '\n')
            for i in range(len(rows)):
                tuple1 = rows[i]
                if '河南' in tuple1[3] and '葵花' not in tuple1[2]:
                    a += 1
                    hn = list(tuple1)
                    hn.insert(0, (str(a)))
                    result = tuple(hn)
                    print(result)
                    sendqq(result, 'group-name')
            print('')
            time.sleep(1)
            flag1 = 1
        else:
            print('Latest data volume：', len(rows), '\n')
            # print('')
            print('Number of historical data：', len(his_rows), '\n')
            # print(rows)
            # Message txt
            # f = open('log.txt', 'w+', encoding='utf-8')
            # f.write(str(his_rows))
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


def timer():
    global clock1
    if time.strftime("%A") == 'Sunday':
        clock1 = datetime.datetime.strptime(time.strftime("%Y-%m-%d 08:00:00"),
                                            "%Y-%m-%d %H:%M:%S") - datetime.timedelta(
            days=6)
    elif time.strftime("%A") == 'Saturday':
        clock1 = datetime.datetime.strptime(time.strftime("%Y-%m-%d 08:00:00"),
                                            "%Y-%m-%d %H:%M:%S") - datetime.timedelta(
            days=5)
    elif time.strftime("%A") == 'Friday':
        clock1 = datetime.datetime.strptime(time.strftime("%Y-%m-%d 08:00:00"),
                                            "%Y-%m-%d %H:%M:%S") - datetime.timedelta(
            days=4)
    elif time.strftime("%A") == 'Thursday':
        clock1 = datetime.datetime.strptime(time.strftime("%Y-%m-%d 08:00:00"),
                                            "%Y-%m-%d %H:%M:%S") - datetime.timedelta(
            days=3)
    elif time.strftime("%A") == 'Wednesday':
        clock1 = datetime.datetime.strptime(time.strftime("%Y-%m-%d 08:00:00"),
                                            "%Y-%m-%d %H:%M:%S") - datetime.timedelta(
            days=2)
    elif time.strftime("%A") == 'Tuesday':
        clock1 = datetime.datetime.strptime(time.strftime("%Y-%m-%d 08:00:00"),
                                            "%Y-%m-%d %H:%M:%S") - datetime.timedelta(
            days=1)
    elif time.strftime("%A") == 'Monday':
        clock1 = datetime.datetime.strptime(time.strftime("%Y-%m-%d 08:00:00"), "%Y-%m-%d %H:%M:%S")
    return clock1


flag1, ia = 0, 0
conn = cx_Oracle.connect('user/password@IP/实例')
cursor = conn.cursor()
sql = ""
cursor.execute(sql)
his_rows = cursor.fetchall()

if __name__ == '__main__':
    print('Sql query time :', start_time())
    sched_time = datetime.datetime.now()
    # print('Run the timer task at {0}'.format(sched_time))
    timer_fun(sched_time)
