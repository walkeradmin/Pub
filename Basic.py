"""
一、运算符
"""
# print(2**2%3//1/2*4-2+6)
# a=1
# b=2
# print('abc'*3)
#
# aa=1
# aa=aa+2
# print(aa)

"""
# 二
# 函数、数据类型
"""
# input()、print()、len()、
# str()、int()、float()、

# print('What is your age?')
# myage = input()
# print('You will be '+str(int(myage)+1)+' in a year')

# print('What is your name?')
# myname = input()
# print('Nice to meet you '+myname)
# print(len(myname))

# print('Please input a number!')
# num = input()
# print(int(num)*2)

# print(len('abc'))

"""
# 三
# 控制语句、(运算符)
"""
# print(1==1)
# print(1==2)
# print(1!=2)
# print(2!=2)
#
# print(False and False)
# print(not not not not True)

# print((1<2)and(2<3))
# print(3+3==6 and not 1+1==3 and 2*3==3+3 )

# name = 'walker'
# password = 'abc123'

# while True:
#     print('Please input name')
#     name = input()
#
#     if name == 'walker':
#         print('Hello walker')
#         print('Please input your password')
#         password = input()
#         if password == 'abc123':
#             print('Access granted')
#             break
#         else:
#             print('Wrong Password')
#     else:
#         print('Wrong name:',name)


# elif
# name = 'Dracula'
# age = 4000
# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 100:
#     print('You are not Alice, grannie.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')


# while
# i = 0
# while i < 3:
#     print('Input your name!')
#     name = input()
#     if name == 'walker':
#         print('Hello walker!')
#         print('Input your password')
#         password = input()
#         if password == 'abc':
#             print('Hi! walker,long time no see')
#             break
#     else:
#         print('Sorry!,wrong name',2-i,'choice')
#     i = i+1


"""无限循环 ERROR"""
# name = ''
# while name != 'you name':
#     print('Please input your name!')
#     name = input()
# print('Thank you')

"""break"""
# while True:
#     print('Input your name')
#     name = input()
#     if name == 'you name':
#         break
# print('Thank you')


# age = ''
# while age !='10':
#     print(age)
#     print('Input your age')
#     age = input()
# print('Thank you!')


"""continue、break"""
# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':       #(1)
#         continue              #(2)
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()      #(3)
#     if password == 'swordfish':
#         break                 #(4)
# print('Access granted.')  #(5)


# name = ''
# while not name: #(1)
#     print('Enter your name:')
#     name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests: #(2)
#     print('Be sure to have enough room for all your guests.') #(3)
# print('Done')


"""for"""
# print('My name is')
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')

# total = 0               #(1)
# for num in range(101):  #(2)
#     total = total + num  #(3)
# print(total)            #(4)

# i = 0
# toal = 0
# while i < 100:
#     i = i + 1
#     toal = toal + i
#     #continue
# print(toal)


"""random"""
# import random
# for i in range(5):
#     print(random.randint(1, 10))
#
#
# from random import *
# for i in range(5):
#     print(randint(1, 10))


"""sys"""
# import sys
# while True:
#         print('键入exit to exit')
#         response = input()
#         if response =='exit':
#             #break
#             sys.exit()
#         print('you typed '+ response +'.')

# continue、break、exit()
# for letter in 'python':
#     if letter == 'h':
#         continue
#     print('letter:',letter)

# for letter in 'python':
#     if letter == 'h':
#         break
#     print('letter:',letter)

# import random
#
# a = []
# b = '123'
# for i in range(3):
#     a.append(random.choice(b))
#     # js = ''.join(a)
#     # print(js)
#
#     print(a)

"""
function def
"""
# def hello(name):
#     print('Hello,' + name)
#
#
# print('Please input name')
# a = input()
# hello(a)

# import base64
# code = 'YWRtaW46YWRtaW4='
# print(base64.b64decode(code))
# Authorization: Basic YWRtaW46YWRtaW4=

# myCat = {'size': 'fat', 'color': 'grey', 'disposition': 'loud','fat':1}
# myCat1 = {'color': 'grey','size': 'fat', 'disposition': 'loud'}
#
# myCat['fat'] = myCat['fat'] + 1
# print(myCat)
# print('My cat color is ' + myCat['color'])
# print(myCat == myCat1)

# print(list(myCat.keys()))
# for k, v in myCat.items():
#     print('Key:', k, 'Value:', v)
#
# print('fat' in myCat.items())
# print(myCat)
# b = myCat.setdefault('fat', '88')
# print(b)
# a = myCat.setdefault('fat', '75')
# print(a)
# import pprint
#
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
#
# for i in message:
#     count.setdefault(i, 0)
#     #print(count)
#     count[i] = count[i] + 1
#
# # a = pprint.pprint(count)
# # print(a)
# #print(pprint.pformat(a))
# pprint.pprint(count)
# time = '2019-05-19 00:00:01'
# sql ="select * from name where maketime > '%s'" %time
#
# print(sql)

# spam = {'color': 'red', 'age': '40'}

# for i in spam.items():
#     #print(i)
#     print(type(i))

# for k in  spam.keys():
#     print(type(k))
# spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'
# print(spam)
# import copy
# a = [
#      ('a','b')]
#
# b = [('批号不允许为空', '2', '国药控股湖北江汉有限公司', '国控湖北江汉仓'),
#      ('送货地址不允许为空', 'XSGZDA00000008', '武汉驰启科技有限公司', '国控湖北武汉仓')]
#
# d = copy.copy(b)
# print(d)
# a.append('')
# print(a == b)
# c = [x for x in a if x not in b]
# print(c)

# import copy
#
# a = [('a','b')]
# while True:
#     b = copy.copy(a)
#     for i in range(2):
#         a.append(('c'))
#     print(b)
# import time
# print("Waiting", end="")
# while True:
#     for i in range(6):
#         print(".", end='', flush=True)
#         time.sleep(0.2)

# a = ['a', 'b', 'c']
# b = ['a', 'b']
# c = ['d']
# c.extend()

"""
a is different of b
"""
# check = list(set(tuple(a)).difference(set(tuple(b))))
# check1 = [x for x in a if x not in b]
#
# print(check)
# c.extend(check)
# print(c)


# if check != []:
#     #print(check)
#     print(check1)
# #     #print([x for x in a if x not in b])
# else:
#     print('空')


# def fixed_time():
#     global Ritnow
#     Ritnow = datetime.timedelta
#
#
# a = 0
# for i in range(0,101):
#     a = a + i
#     time.sleep(1)
#     fixed_time()
#     if Ritnow > '22:46:50':
#         break
# print(Ritnow)
# print(a)



"""
time
"""
# import time
# def Maketime():
#     a, b, c, d = -1, -2, -3, -4
#     week = 'F'
#     if week == 'Monday':
#         now_time = datetime.datetime.now()
#         time_format = now_time.strftime('%Y-%m-%d')
#     elif week == 'Tuesday':
#         now_time = datetime.datetime.now()
#         change_time = now_time + datetime.timedelta(days=a)
#         time_format = change_time.strftime('%Y-%m-%d')
#     elif week == 'Wednesday':
#         now_time = datetime.datetime.now()
#         change_time = now_time + datetime.timedelta(days=b)
#         time_format = change_time.strftime('%Y-%m-%d')
#     elif week == 'Thursday':
#         now_time = datetime.datetime.now()
#         change_time = now_time + datetime.timedelta(days=c)
#         time_format = change_time.strftime('%Y-%m-%d')
#     elif week == 'Friday':
#         now_time = datetime.datetime.now()
#         change_time = now_time + datetime.timedelta(days=c)
#         time_format = change_time.strftime('%Y-%m-%d')
#
#     clock = time_format + ' ' + '00:00:01'
#     return clock
#
#
# print('开始时间: %s'% Maketime())


"""datetime"""
# import datetime
#
#
# if 'Saturday' in time.strftime("%Y-%m-%d %H:%M:%S %A"):
#     # 当前时间
#     time1 = time.strftime("%Y-%m-%d %H:%M:%S")
#     # 当前日期
#     date1 = time.strftime("%Y-%m-%d 08:00:00")
#     print(date1)
#     # 累加天数
#     time2 = datetime.datetime.strptime(date1,"%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=2)
#     # 差值,秒化,并转换成int
#     sleeptime = int((time2 - datetime.datetime.strptime(time1,"%Y-%m-%d %H:%M:%S")).total_seconds())
#     print(sleeptime)
# elif 'Sunday' in time.strftime("%Y-%m-%d %H:%M:%S %A"):
#     time11 = time.strftime("%Y-%m-%d %H:%M:%S")
#     date11 = time.strftime("%Y-%m-%d 08:00:00")
#     time22 = datetime.datetime.strptime(date11,"%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=1)
#     sleeptime = int((time22 - datetime.datetime.strptime(time11,"%Y-%m-%d %H:%M:%S")).total_seconds())





"""
"".join() tuple to str   list to str
"""
# hisrows = [('批号', '1', '丹东', '丹东仓'),('批号', '2', '河南', '郑州')]
# num = 0
# for i in range(len(hisrows)):
#     num += 1
#     #tuple
#     tu = hisrows[i]
#     reson = "".join(tu[:1])
#     billid = "".join(tu[1:2])
#     owner = "".join(tu[2:3])
#     stroge = "".join(tu[3:])
#     result = '卡单原因：' + reson + '''
# 订单组号：''' + billid + '''
# 货主名称：''' + owner + '''
# 仓库名称：''' + stroge + '''
# '''
#     print(result)



"""数据结构化成嵌套式字典"""
# import time
# dic = {}
# dic2 = {}
# a = 0
# list1 = [('批号', '3', '沈阳', '沈阳仓'), ('批号', '4', '沈阳', '沈阳仓')]
# for i in list1:
#     if '沈阳' in i:
#         a +=1
#         id_num = i[1]
#         dic2.setdefault(time.strftime("%Y-%m-%d"), [id_num])
#         #print(dic2)
#         dic.setdefault('沈阳', dic2)
#         #print(dic)
#         list2 = (dic['沈阳'])[time.strftime("%Y-%m-%d")]
#         if a != 1:
#             list2.append(id_num)
# print(dic)


"""pprint"""
# import pprint
# a ={'沈阳': {'2019-05-30': ['11190530000310','1','3','4','5','6']}, '河南': {'2019-05-30': ['0006655205','1','3']}}
# a = {'HB': {'2019-05-31': {'销售': ['P0237176', '123']}},
#      'SX': {'2019-05-31': {'采退': ['BSD308041905000001']}}}
#     {'HB': {'2019-05-31': ['ASN1']}}
#
# his_rows = list1 = [('批号', 'ASN1', '黄石', '湖北仓', '采退'),
#                     ('批号', 'ASN2', '沈阳', '湖北仓', '销售'),
#                     ('批号', 'ASN3', '沈阳', '湖北仓', '销售')]
# dic = {}
# hn = {}
# hn_type = {}
# for i in his_rows:
#     if '葵花' in i[3]:
#         id_hn = i[1]
#         ow_name = i[2]
#         op_type = i[4]
#         name_id = ow_name + '-' + id_hn
#         hn_type.setdefault(op_type, [name_id])
#         hn.setdefault(time.strftime("%Y-%m-%d"), hn_type)
#         dic.setdefault('HB', hn)
#         list_hn = dic['HB'][time.strftime("%Y-%m-%d")][op_type]
#         if name_id not in list_hn:
#             list_hn.append(name_id)
# pprint.pprint(dic, width=30)
#
# old = {'HB': {'2019-05-31': {'销售': ['P0237176', '123']}}}
# new = {'HB': {'2019-05-31': {'采退': ['BSD308041905000001']}}}
#
# old.setdefault('HB', new['HB'])
# ow_id_new = ((new['HB'])['2019-05-31'])['采退']
# ow_op_new = (old['HB'])['2019-05-31']
# ow_op_new.setdefault('采退', ow_id_new)
# print(old)
# f = open('first.txt', 'w+', encoding='utf-8')
# f.write(str(old))


"""
# eval函数的作用:无视形参接收的实参中的引号，并将剩余内容看做表达式或命令
# 用来执行一个字符串表达式，并返回表达式的值
"""
# eval
# f = open("first.txt", "r", encoding='utf-8')
# res = f.read()
# res = eval(res)
# f.close()
# # print(tures)
# old = {'SX': {'2019-06-03': {'11-销售':
# ['国药控股陕西有限公司-SFXS21101906000162',
# '国药控股陕西有限公司-SFXS21101906000160',
# '国药控股陕西有限公司-SFXS21101906000159']}}}
#
# for i in old.keys():
#     print(i)
#
#
# new = {}
# if new == {}:
#     print('kong')
# else:
#     print('you')
# global a
# global new_op
# for k in old.keys():
#     a = k
#
# op_dic = (old[a])['2019-05-31']
# for k1 in op_dic:
#     new_op = k1
#
# print(new_op)
# message = {'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.':'1'}
# a = eval(str(message))
# print(type(a))

# str2 = 'print("你好")'
# eval(str2)


"""re"""
# import re
#
# new = 'phonenumber is +86-13211472564'
#
# regex1 = re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d\d')
# mo = regex1.search(new)
# print('my phone number is：', mo.group())




"""
# 正则匹配
# 1.引入模块import re
# 2.调用re.compile函数创建对象Regex
# 3.将需要搜索的字符串传递给Regex对象的search方法。返回一个mach对象
# 4.调用mach对象的group方法以返回实际匹配文本的字符串
# import re
"""

'''1、'''
# ()分组匹配 \d 匹配number
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# # 第一组
# mo.group(1)
# # 第二组
# mo.group(2)
# # 相同
# # mo.group(0) == mo.group()


'''2、'''
# ?字符标记其前面的组作为模式的可选部分
# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegex.search('My number is 415-555-4242')
# print(mo1.group())


'''3、'''
# *的意思是匹配的零个或多个
# batRegex = re.compile(r'bat(wo)*man')
# mo = batRegex.search('The adventures of batwowoman')
# print(mo.group())


'''4、'''
# +（或加号）表示匹配一个或多个,加号前面的组必须至少出现一次。它不是可选
# import re
#
# batRegex = re.compile(r'bat(wo)+man')
# mo = batRegex.search('The adventures of batman')
#
# print(mo == None)


'''5、'''
# {}匹配重复特定次数的组,正则表达式中使用大括号中的数字跟随该组
# {,5} 逗号分隔最小和最大边接值
# import re
#
# batRegex = re.compile(r'(ha){,5}')
# mo = batRegex.search('hahahahahaha')
#
# print(mo.group())


'''6、'''
# {}后跟问号：贪婪和不合适的匹配,与最短的字符串匹配.

# import re
#
# batRegex = re.compile(r'(ha){2,5}?')
# mo = batRegex.search('hahahahahaha')
#
# print(mo.group())


'''7、'''
# findall() 该方法将返回搜索到的字符串中每个匹配项的字符串

# import re
#
# # 1.不分组
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# # 返回字符串列表
# print(mo)
#
#
# # 2.分组
# phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# mo1 = phoneNumRegex1.findall('Cell: 415-555-9999 Work: 212-555-0000')
# # 返回元组列表
# print(mo1)


'''8、'''
# 常用字符类的简写代码
# \d 从0到9的任何数字。

# \D 任何不是0到9之间的数字的字符。

# \w 任何字母，数字或下划线字符。（把它想象成匹配的“单词”字符。）

# \W 任何不是字母，数字或下划线字符的字符。

# \s 任何空格，制表符或换行符。（把它想象成匹配的“空格”字符。）

# \S 任何不是空格，制表符或换行符的字符。

# \b : 空白字符 (只在某个字的开头或结尾)

# \B : 空白字符 (不在某个字的开头或结尾)

# \\ : 匹配 \

#  . : 匹配任何字符 (除了 \n)

# ^ : 匹配开头

# $ : 匹配结尾

# ? : 前面的字符可有可无


'''9、'''
# Making Your Own Character Classes
# []中加入自己定义字符类
# 字符类[a-zA-Z0-9]将匹配所有小写字母，大写字母和数字
# import re
#
# # vowelRegex = re.compile(r'[aeiouAEIOU]')
# # mo = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
# # print(mo)
#
# # []字符类不需要加转义符\
# .匹配任意字符
# vome = re.compile(r'5.a')
# mo = vome.findall('5[a')
# print(mo)


'''10、'''
# 插入符号：^ 美元符号字符：$
# ^制定固定开头 $制定固定结尾
# import re
#
# beginsWithHello = re.compile(r'^Hello')
# mo = beginsWithHello.search('Hello world!')
# print(mo)
#
# endsWithNumber = re.compile(r'\d$')
# mo1 = endsWithNumber.search('Your number is 42')
# print(mo1)


'''11、'''
# 通配符.将匹配除换行符之外的任何字符
# import re
#
# atRegex = re.compile(r'.at')
# mo = atRegex.findall('The cat in the hat sat on the flat mat.')
# print(mo)



'''12、'''
# 点星（.*）代表“任何东西”

import re

# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# print(mo.group(1))
# print(mo.group(2))


# 请使用点，星号和问号（.*?）。与大括号一样
# ?指匹配第一组
# nongreedyRegex = re.compile(r'<.*?>')
# mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())
#
# # 匹配更多
# greedyRegex = re.compile(r'<.*>')
# mo = greedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())



'''13、'''

# 通过传递re.DOTALL第二个参数re.compile()，
# 可以使点字符匹配所有字符，包括换行符
# import re
#
# # 不包含换行符
# newlineRegex = re.compile('.*')
# mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
# print(mo.group())
#
# # 包含换行符
# newlineRegex = re.compile('.*', re.DOTALL)
# mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
# print(mo.group())



'''14、'''
# 正则表达式符号
# The ? matches zero or one of the preceding group.
#
# The * matches zero or more of the preceding group.
#
# The + matches one or more of the preceding group.
#
# The {n} matches exactly n of the preceding group.
#
# The {n,} matches n or more of the preceding group.
#
# The {,m} matches 0 to m of the preceding group.
#
# The {n,m} matches at least n and at most m of the preceding group.
#
# {n,m}? or *? or +? performs a nongreedy match of the preceding group.
#
# ^spam means the string must begin with spam.
#
# spam$ means the string must end with spam.
#
# The . matches any character, except newline characters.
#
# \d, \w, and \s match a digit, word, or space character, respectively.
#
# \D, \W, and \S match anything except a digit, word, or space character, respectively.
#
# [abc] matches any character between the brackets (such as a, b, or c).
#
# [^abc] matches any character that isn’t between the brackets.



'''15、'''
# 不区分大小写

# robocop = re.compile(r'robocop', re.I)
# mo = robocop.search('Robocop is part man, part machine, all cop.')
# print(mo.group())
#
# mo1 = robocop.search('ROBOCOP protects the innocent.')
# print(mo1.group())
#
# mo2 = robocop.search('Al, why does your programming book talk about robocop so much?')
# print(mo2.group())



'''16、'''
# sub（）方法替换字符串
# import re
# namesRegex = re.compile(r'Agent \w+')
# mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'CENSORED gave the secret documents to CENSORED.'
# print(mo)
#
# # 以头字幕****显示
# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# mo1 = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that AgentEve knew Agent Bob was a double agent.')
# print(mo1)


'''17、'''
# 复杂的正则表达式
# import re
# mo = phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
# print(mo)
#
# mo1 = phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?            # area code
#     (\s|-|\.)?                    # separator
#     \d{3}                         # first 3 digits
#     (\s|-|\.)                     # separator
#     \d{4}                         # last 4 digits
#     (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
#     )''', re.VERBOSE)
# print(mo1)



'''18、'''
# 结合re.IGNORECASE，re.DOTALL和re.VERBOSE
# 利用管道符| 分割参数
# import re
# someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
# someRegexValue1 = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# a = '<urlopen error timed out>'
# b = a.strip('<>')
# print(b)
# f = open('DataClean.txt', 'r', encoding='utf-8')
# data_clean = f.read()
# # print(data_clean)
# for i in data_clean.split(','):
#     print(i)


"""os"""
# import os

# file_name = ['1.txt', '2.txt', '3.txt']
# # 连接路径
# print(os.path.join("d:\\work", file_name[0]))
# # 获取路径
# path = os.getcwd()
# # 改变路径
# os.chdir('D:\\Work\\AIops')
# print(os.getcwd())
# # 创建路径
# os.makedirs('')
# # 绝对路径、相对路径
# # 把相对路径转换为绝对路径
# os.path.abspath(path)
# # 判断当前路径，若为绝对路径则反馈True 若为相对路径则反馈False
# os.path.isabs(path)
# D:\Work\AIops\python-back
# totalSize = 0
# for i in os.listdir('D:\\Work'):
#     totalSize = totalSize + os.path.getsize(os.path.join('D:\\Work', i))
# print(os.path.getsize('D:\\Work'))
# f = open('123.txt', 'r', encoding='ANSI')
# a = f.readlines()
# print(a)
# a = 'Hello world\nHello world'
# f = open('ces.txt', 'w+', encoding='utf-8')
# f.write(a)


"""shutil os zipfile"""
# import shutil
# import os
# import zipfile
# 复制
# shutil.copy('1.txt', '11.txt')
# 复制所有文件夹和文件
# shutil.copytree('path', 'path')
# 移动
# shutil.move('11.txt', 'D:\\abc\\acd')
# 删除单个文件
# os.unlink('11.txt')
# 删除单个文件夹
# os.rmdir('测试')
# 删除所有文件夹以及文件
# shutil.rmtree('path')
import send2trash
# r 读 报错 -
# r+ 读写 报错 覆盖
# w 写 创建 覆盖
# w+ 读写 创建 覆盖
# a 写 创建 追加
# a+ 读写 创建 追加
# f = open('ceShi.txt', 'w+')
# f.write('This is a test\n')
# f.close()
# send2trash.send2trash('ceShi.txt')

# 遍历目录树
# for folderName, subfolders, fileName in os.walk(os.path.abspath('.')):
#     print(folderName)
#     print(subfolders)
#     print(fileName)

# os.chdir('D:\\Work\\AIops\\python-back\\Picture')
# for foldername, sbufolders, filename in os.walk(os.path.abspath('.')):
#     print('')
# 压缩文件  w 将擦除已有文件, a 为追加
# # exampleZip = zipfile.ZipFile('txt.zip', 'w', zipfile.ZIP_DEFLATED)
# # for i in filename:
# #     exampleZip.write(i)
# # exampleZip.close()
# exampleZip = zipfile.ZipFile('txt.zip')

# 获取压缩文件名 list
# nameList = exampleZip.namelist()
# print(nameList)
# 读取
# exampleInfo = exampleZip.getinfo('g1.gif')
# 获取压缩前大小
# fileSize = exampleInfo.file_size
# 获取压缩后大小
# compressSize = exampleInfo.compress_size
# print(fileSize)
# print(compressSize)
# print(round(fileSize / compressSize, 2))

# or 压缩文件
# newZip = zipfile.ZipFile('new.zip', 'w')
# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()

# extractall 解压文件
# 如果传递给extractall()方法的文件夹不存在，则会创建该文件夹
# exampleFile = zipfile.ZipFile('txt.zip')
# os.chdir("D:\\Work\\AIops\\python-back\\Picture\\txt")
# exampleFile.extractall()
# exampleFile.close()

# extract()方法ZipFile将从ZIP文件中提取单个文件
# exampleZip.extract('spam.txt')
# 'C:\\spam.txt'
# exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
# 'C:\\some\\new\\folders\\spam.txt'
# exampleZip.close()





