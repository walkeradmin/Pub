# -*- coding:utf-8 -*-
# author：walker
# time；2019-07-14/09-08

import time
import datetime
import shelve
import logformat
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import threading
from threading import Timer, Thread
import alterwet
import traceback
import configparser
import os
import sys
usual = os.getcwd()
py_name = os.path.basename(sys.argv[0])


def s_time():
    a, b, c, d, e = -6, -5, -4, -3, -2
    now = datetime.datetime.now()
    time_format1 = now + datetime.timedelta(days=a)
    time_format2 = now + datetime.timedelta(days=b)
    time_format3 = now + datetime.timedelta(days=c)
    time_format4 = now + datetime.timedelta(days=d)
    time_format5 = now + datetime.timedelta(days=e)
    mon = time_format1.strftime("%Y-%m-%d")
    tues = time_format2.strftime("%Y-%m-%d")
    wen = time_format3.strftime("%Y-%m-%d")
    thur = time_format4.strftime("%Y-%m-%d")
    fri = time_format5.strftime("%Y-%m-%d")
    return mon, tues, wen, thur, fri


def timer(t1, t2, chrome, url_mq, user, password, url_oa, oa_user, oa_password, title, test, week1):
    week = time.strftime("%A")
    clock = time.strftime("%H:%M:%S")
    if week == week1 and t1 <= clock < t2:
        log().info('Start the task：%s' % time.strftime("%Y-%m-%d %H:%M:%S"))
        day = time.strftime("%Y-%m-%d")
        filename = "%s\\formatLogs\\MQPic\\%s\\赛飞uap巡检报告%s~%s.xlsx" % (usual, day, s_time()[0], s_time()[4])
        path = "%s\\formatLogs\\MQPic\\%s\\" % (usual, day)
        title = title.format(s_time()[0], s_time()[4])
        element(chrome, url_mq, user, password, url_oa, oa_user, oa_password, title, test, filename, path)
        time.sleep(1)
    else:
        log().info('| TIMER FUNCTION | Message：'
                   'Do not perform automatic inspection tasks within the specified time range |')
    global timer1
    timer1 = Timer(inTime, timer, [t1, t2, chrome, url_mq, user, password, url_oa, oa_user, oa_password, title, test, week1])
    timer1.start()


def xpath_double_click(drive, element1):
    double_click_element = element1
    ActionChains(drive).double_click(double_click_element).perform()


# NoChromeBrowser
def no_browser():
    options = Options()
    options.add_argument('--headless')                               # No visual page available
    options.add_argument('--disable-gpu')                            # Avoid bugs
    options.add_argument('--log-level=3')                            # log level
    drive = webdriver.Chrome(executable_path="Chromedriver.exe", options=options)
    return drive


def element(chrome, url, user, password, url_oa, oa_user, oa_password, title, test, filename, path):
    try:
        tt = time.strftime("%Y-%m-%d")
        # drive = webdriver.Chrome(chrome)    # browser
        # drive.maximize_window()             # my window size: {'width': 1514, 'height': 974}!!!
        drive = no_browser()
        drive.set_window_size(1920, 1080)
        # w_size = drive.get_window_size()
        drive.get(url)
        drive.implicitly_wait(10)
        drive.find_element_by_name('username').send_keys(user)
        drive.find_element_by_name('password').send_keys(password)
        drive.find_element_by_xpath('//*[@id="login-view"]/form/div[3]/button').click()  # login
        drive.switch_to.window(drive.window_handles[0])  # Crawl the current page element
        button = drive.find_element_by_xpath(
            '/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[5]/div/div[1]/div/div/div/button/div/span/span').text  # Crawl button clock

        if button == 'Previous week':
            log().info('| ELEMENT FUNCTION | Message：The grafana query condition has been set to "Previous week" |')
        drive.find_element_by_xpath(
            '//*[@id="panel-84"]/div/div/div/plugin-component/panel-plugin-natel-discrete-panel/grafana-panel/div/div[1]/panel-header/span/span[2]').click()
        drive.find_element_by_xpath('//*[@id="panel-84"]/div/div/div/plugin-component/panel-plugin-natel-discrete-panel/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[1]').click()
        if not os.path.exists(path):
            os.makedirs(path)
        time.sleep(3)
        drive.save_screenshot('%s\\MQ_Status_%s.png' % (path, tt))   # MQ Status
        drive.find_element_by_xpath('/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[1]/button').click()  # back

        element1 = drive.find_element_by_xpath('//*[@id="panel-62"]')
        ActionChains(drive).move_to_element(element1).perform()
        drive.find_element_by_xpath('//*[@id="panel-62"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[2]').click()   # Load
        drive.find_element_by_xpath('//*[@id="panel-62"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[1]').click()  # View
        time.sleep(3)
        drive.save_screenshot('%s\\Load_%s.png' % (path, tt))    # MQ Load
        drive.find_element_by_xpath('/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[1]/button').click()  # back

        element2 = drive.find_element_by_xpath('//*[@id="panel-52"]')
        ActionChains(drive).move_to_element(element2).perform()     # move to disk grafana panel-plugin-briangann-datatable-panel
        time.sleep(1)
        drive.save_screenshot('%s\\Disk_%s.png' % (path, tt))        # MQ Disk

        element3 = drive.find_element_by_xpath('//*[@id="panel-16"]')
        ActionChains(drive).move_to_element(element3).perform()
        drive.find_element_by_xpath('//*[@id="panel-16"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[2]').click()   # Mem
        drive.find_element_by_xpath('//*[@id="panel-16"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[1]').click()  # View
        time.sleep(1)
        drive.save_screenshot('%s\\Mem_%s.png' % (path, tt))         # MQ Mem
        drive.find_element_by_xpath('/html/body/grafana-app/div/div/div/react-container/div/div[1]/div[1]/button').click()  # back

        drive.find_element_by_xpath('//*[@id="panel-28"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[2]').click()   # CPU
        drive.find_element_by_xpath('//*[@id="panel-28"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[2]').click()   # CPU
        time.sleep(1)
        drive.save_screenshot('%s\\Cpu_%s.png' % (path, tt))        # MQ CPU

        drive.find_element_by_xpath('//*[@id="panel-12"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[2]').click()   # Network
        drive.find_element_by_xpath('//*[@id="panel-12"]/div/div/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[1]/panel-header/span/span[3]/ul/li[1]').click()  # View
        time.sleep(3)
        drive.save_screenshot('%s\\Network_%s.png' % (path, tt))    # MQ Networ
        log().info('View current directory：' + os.getcwd())
        list_dir = os.listdir(path)
        image = list()
        for name in list_dir:
            if name.endswith('.png'):
                image.append(name)
        str_name = '，'.join(image)
        if 'MQ_Status' in str_name and 'Load' in str_name and 'Disk' in str_name and 'Mem' in str_name and 'Cpu' in str_name and 'Network' in str_name:
            log().info('| ELEMENT FUNCTION | Message：All images have been saved |')
            log().info('| ELEMENT FUNCTION | Message：Image path：%s |' % os.getcwd())
            for i in range(len(image)):
                log().info(image[i])
            log().info('| ELEMENT FUNCTION | Message：Close driver，Execute the excel generation task |')
            drive.quit()
            excel(chrome, url_oa, oa_user, oa_password, title, test, filename, path)  # send oa task
        else:
            error().error('''| ELEMENT FUNCTION | Message：Individual images are not saved |''')
            error().error('| ELEMENT FUNCTION | Message：File path: |' + os.getcwd())
            for i in range(len(image)):
                error().error(image[i])
            error().error('| ELEMENT FUNCTION | Message：Close driver，please check the task |')
            drive.quit()
    except Exception as e:
        alter = alterwet.Comp('@all', mess().format(str(e)), 'Inspection')
        alter.post()
        error().error(traceback.format_exc())


def excel(chrome, url_oa, oa_user, oa_password, title, test, filename, path):
    try:
        day = time.strftime("%Y-%m-%d")
        wb = load_workbook("%s\\tem\\template.xlsx" % usual)
        ws1 = wb['MQ']
        img_status = Image(path + 'MQ_Status_%s.png' % day)
        ws1.add_image(img_status, 'C10')
        img_load = Image(path + 'Load_%s.png' % day)
        ws1.add_image(img_load, 'C117')
        img_disk = Image(path + 'Disk_%s.png' % day)
        ws1.add_image(img_disk, 'C227')
        img_mem = Image(path + 'Mem_%s.png' % day)
        ws1.add_image(img_mem, 'C337')
        img_cpu = Image(path + 'Cpu_%s.png' % day)
        ws1.add_image(img_cpu, 'C446')
        img_net = Image(path + 'Network_%s.png' % day)
        ws1.add_image(img_net, 'C555')
        ws2 = wb['AMQ巡检报告']
        ws2['A3'] = s_time()[0]
        ws2['A20'] = s_time()[1]
        ws2['A37'] = s_time()[2]
        ws2['A54'] = s_time()[3]
        ws2['A71'] = s_time()[4]
        ws3 = wb['汇总视图']
        ws3['D5'] = s_time()[0]
        ws3['E5'] = s_time()[4]
        ws3['E9'] = '%s至%s' % (s_time()[0], s_time()[4])
        ws3['E10'] = '%s至%s' % (s_time()[0], s_time()[4])
        wb.save(path + '赛飞uap巡检报告%s~%s.xlsx' % (s_time()[0], s_time()[4]))
        log().info('''| EXCEL FUNCTION | Message：Excel inspection document has been generated |''')
        log().info('''| EXCEL FUNCTION | Message：File path：|''' + filename + '\n')
        log().info('''| EXCEL FUNCTION | Message：Start performing OA send task |''')
        oa_window(chrome, url_oa, oa_user, oa_password, title, test, filename)
    except Exception as e:
        alter = alterwet.Comp('@all', mess().format(str(e)), 'Inspection')
        alter.post()
        error().error(traceback.format_exc())


def oa_window(chrome, url, user, password, title, test, filename):
    try:
        # drive = webdriver.Chrome(chrome)
        # drive.maximize_window()
        drive = no_browser()
        drive.set_window_size(1514, 974)
        drive.get(url)
        drive.implicitly_wait(10)
        drive.find_element_by_xpath('//*[@id="login_username"]').send_keys(user)
        drive.find_element_by_xpath('//*[@id="login_password"]').send_keys(password)
        drive.find_element_by_id('login_button').click()
        how = drive.find_element_by_css_selector("[class='lev1Title navTitleName']")
        ActionChains(drive).move_to_element(how).perform()
        cli = drive.find_element_by_xpath('//*[@id="lev2_-4140425781984149261"]/div/div[2]')
        drive.execute_script("$(arguments[0]).click()", cli)
        drive.switch_to.window(drive.window_handles[1])                                              # Switch to a new page
        drive.find_element_by_css_selector('[class="w100b color_gray"]').send_keys(title)            # determine class=space
        drive.find_element_by_xpath('//*[@id="colMainData"]/div[1]/span[1]/span[1]').click()         # upload file
        drive.switch_to.frame(drive.find_element_by_xpath(
            "//iframe[contains(@src,'/seeyon/fileUpload.do?type=0&inputId=attFileDomain&applicationCategory=1&extensions=&maxSize=&isEncrypt=&popupTitleKey=&attachmentTrId=Att&callMethod=insertAtt_AttCallback&takeOver=false')]"))  # switch to file frame
        drive.find_element_by_name('file1').send_keys(filename)
        drive.find_element_by_id('b1').click()  # Enter File
        drive.find_element_by_id('process_info_select_people').click()
        drive.switch_to.frame(drive.find_element_by_xpath("//iframe[contains(@src,'/seeyon/selectpeople.do?onlyShowChildrenAccount=undefined')]"))  # switch to lc frame
        drive.find_element_by_xpath('//*[@id="li_Team"]/a').click()
        xpath_double_click(drive, drive.find_element_by_xpath('//*[@id="TeamDataBody"]/option[8]')) # customize choose group
        drive.switch_to.default_content()                                                  # Jump back to the outermost page
        determine = drive.find_element_by_css_selector("[class='layui-layer-btn0 margin_r_10 common_button common_button_emphasize  ']")
        drive.execute_script("$(arguments[0]).click()", determine)                         # determine class=space
        drive.switch_to.frame('zwIframe')                                                  # switch to Superior frame id
        drive.switch_to.frame(0)                                                           # switch first frame
        drive.find_element_by_tag_name('body').send_keys(test.format(s_time()[0], s_time()[4], time.strftime("%Y-%m-%d %H:%M:%S")))      # iframe editor send keys
        drive.switch_to.default_content()
        drive.find_element_by_id('sendId').click()                                          # send
        drive.switch_to.window(drive.window_handles[0])
        drive.find_element_by_id('spaceLi_6940425807421655422').click()                     # flush page
        time.sleep(6)
        li = drive.find_elements_by_css_selector('[class="cellContentText titleText"]')     # check list
        track = list()
        for i in range(len(li)):
            active = li[i].text
            track.append(active)
        string = '|'.join(track)
        check = 'AMQ和缓存巡检报告%s~%s' % (s_time()[0], s_time()[4])
        if check in string:
            log().info('''| OA WINDOW FUNCTION | Message：
            The inspection weekly report OA has been sent successfully. |''')
            act = drive.find_element_by_css_selector('[class="vportal vp-setting"]')        # Hover window
            ActionChains(drive).move_to_element(act).perform()
            drive.find_element_by_xpath('//*[@id="logout"]').click()
            drive.find_element_by_css_selector('[class="common_button common_button_emphasize margin_r_10 hand"]').click()  # exit
            log().info('''| OA WINDOW FUNCTION | Message：Exit OA，continue to execute the inspection task |''')
            drive.quit()
        else:
            error().error('| OA WINDOW FUNCTION | Message：'
                          'The inspection week was not sent successfully, please stop the task. |')
            drive.quit()
    except Exception as e:
        alter = alterwet.Comp('@all', mess().format(str(e)), 'Inspection')
        alter.post()
        error().error(traceback.format_exc())


def clean_screen():
    os.system('cls')
    log().info('| CLEAN SCREEN FUNCTION | Message：[Clear screen] task execution completed |')
    global timer2
    timer2 = threading.Timer(cleanTime, clean_screen)
    timer2.start()


def check_thread():
    log().info('| CHECK THREAD FUNCTION | Message：Check Thread：{} |'.format(threading.enumerate()))
    log().info('| CHECK THREAD FUNCTION | Message：Check Thread alive count：{} |'.format(threading.active_count()))
    global timer3
    timer3 = threading.Timer(checkTime, check_thread)
    timer3.start()


def mess():
    mess1 = '''Script：Inspection.py
message：{}
    '''
    return mess1


def error():
    lg = logformat.Logger(logger=py_name + '(error)', filename='Inspection_error', level='error')
    return lg


def log():
    try:
        log1 = logformat.Logger(logger=py_name + '(debug)', filename='Inspection_info', level='debug')
        return log1
    except Exception as e:
        alter = alterwet.Comp('@all', mess().format(str(e)), 'Inspection')
        alter.post()
        error().error(traceback.format_exc())


def deploy():
    conf_file = os.path.join(os.getcwd(), 'DevopsConf.ini')
    cp = configparser.ConfigParser()
    cp.read(conf_file)
    return cp


def main():
    global cleanTime, inTime, checkTime
    inTime = 30
    cleanTime = 7200
    checkTime = 3600
    chrome = ".\\Chromedriver.exe"
    url_mq = deploy().get('ins', 'url_mq_copy')
    url_oa = deploy().get('ins', 'url_oa')
    title = deploy().get('ins', 'title')
    test = deploy().get('ins', 'test')
    file = shelve.open('gywl')
    user = file['grafana']['user1']
    password = file['grafana']['passwd1']
    oa_user = file['oa']['user']
    oa_password = file['oa']['passwd']
    file.close()
    t1 = deploy().get('ins', 't1')
    t2 = deploy().get('ins', 't2')
    week1 = deploy().get('ins', 'week')
    thread_list = list()
    thread1 = Timer(1, timer, [t1, t2, chrome, url_mq, user, password, url_oa, oa_user, oa_password, title, test, week1])
    thread2 = Thread(target=clean_screen, name='cleanScreenThread')
    thread3 = Thread(target=check_thread, name='CheckThread')
    thread_list.append(thread1)
    thread_list.append(thread2)
    thread_list.append(thread3)
    for i in thread_list:
        i.start()
        i.join()
    thread1.cancel()
    log().info('Kill thread1')


if __name__ == '__main__':
    main()
