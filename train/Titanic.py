# -*- coding:utf-8 -*-
# import pandas as pd  # 数据分析
# import matplotlib.pyplot as plt
# import matplotlib
# import numpy as np  # 科学计算
# from pandas import Series, DataFrame
#
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']     # 制定字体
# # matplotlib.rcParams['font.family'] = 'sans-serif'
# matplotlib.rcParams['axes.unicode_minus'] = False       # 解决负号'-'显示为方块的问题
#
# data_train = pd.read_csv("Train.csv")
# data_df = pd.DataFrame(data_train)
# # print(data_train.head())
# # data_df.info()  # 数据汇总
# # data_df.describe()  # 汇总统计
# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
#
# plt.subplot2grid((2, 3), (0, 0))  # 在一张大图里分列几个小图
# data_train.Survived.value_counts().plot(kind='bar')  # 柱状图
# plt.title(u"获救情况 (1为获救)")  # 标题
# plt.ylabel(u"人数")
#
# plt.subplot2grid((2, 3), (0, 1))
# data_train.Pclass.value_counts().plot(kind="bar")
# plt.ylabel(u"人数")
# plt.title(u"乘客等级分布")
#
# plt.subplot2grid((2, 3), (0, 2))
# plt.scatter(data_train.Survived, data_train.Age)
# plt.ylabel(u"年龄")  # 设定纵坐标名称
# plt.grid(b=True, which='major', axis='y')
# plt.title(u"按年龄看获救分布 (1为获救)")
#
# plt.subplot2grid((2, 3), (1, 0), colspan=2)
# data_train.Age[data_train.Pclass == 1].plot(kind='kde')
# data_train.Age[data_train.Pclass == 2].plot(kind='kde')
# data_train.Age[data_train.Pclass == 3].plot(kind='kde')
# plt.xlabel(u"年龄")  # plots an axis lable
# plt.ylabel(u"密度")
# plt.title(u"各等级的乘客年龄分布")
# plt.legend((u'头等舱', u'2等舱', u'3等舱'), loc='best')  # sets our legend for our graph.
#
# plt.subplot2grid((2, 3), (1, 2))
# data_train.Embarked.value_counts().plot(kind='bar')
# plt.title(u"各登船口岸上船人数")
# plt.ylabel(u"人数")
# plt.show()

