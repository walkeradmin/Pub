"""
NumPy是一个功能强大的Python库，主要用于对多维数组执行计算。NumPy这个词来源于两个单词-- Numerical和Python。
NumPy提供了大量的库函数和操作，可以帮助程序员轻松地进行数值计算。这类数值计算广泛用于以下任务：

(1)机器学习模型：在编写机器学习算法时，需要对矩阵进行各种数值计算。例如矩阵乘法、换位、加法等。
NumPy提供了一个非常好的库，用于简单(在编写代码方面)和快速(在速度方面)计算。
NumPy数组用于存储训练数据和机器学习模型的参数。

(2)图像处理和计算机图形学：计算机中的图像表示为多维数字数组。
NumPy成为同样情况下最自然的选择。实际上，NumPy提供了一些优秀的库函数来快速处理图像。
例如，镜像图像、按特定角度旋转图像等。

(3)数学任务：NumPy对于执行各种数学任务非常有用，如数值积分、微分、内插、外推等。
因此，当涉及到数学任务时，它形成了一种基于Python的MATLAB的快速替代
"""
# -*- coding:utf-8 -*-
import numpy as np

# 一、BASIC #
# np.zeros()
# np.ones()                                         # numpy 支持 zero one定义
# np.random.random()                                # 随机函数，它为每个元素分配0到1之间的随机值
my_array = np.array([[4, 5, 7], [6, 1, 3]])         # define array
# my_array[0][1]                                    # index 取出第0行第1列元素
my_column = my_array[:, 2]                          # index 取出第二列所有元素

# 对数组进行数值计算
a = np.array([[5, 3, 7, 8], [2, 4, 8, 2], [2, 4, 8, 2], [2, 4, 8, 2]])
b = np.array([[1, 2, 3, 4], [2, 3, 1, 4], [2, 3, 1, 4], [2, 3, 1, 4]])
sum1 = a + b
difference = a - b
multiply = a * b
quotient = a / b
matrix_multiply = a.dot(b)                          # 矩阵运算与矩阵数值计算不相同
print('''sum = 
''', sum1)
print('''difference = 
''', difference)
print('''multiply = 
''', multiply)
print('''quotient = 
''', quotient)
print('matrix multiply \n', matrix_multiply)

# 二、#
