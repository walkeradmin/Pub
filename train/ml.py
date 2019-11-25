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

"""
Numpy
Numpy科学计算的基础包，主要用于多维数组计算（NumPy包的核心是ndarray对象，完全支持面向对象方法）


1、NumPy数组和原生Python Array（数组）区别？
  （1）NumPy 数组在创建时具有固定的大小，更改ndarry会创建新的数组同时删除原来数组。
  （2）NumPy 数组中的元素都需要具有相同的数据类型，因此在内存中的大小相同。
      例外情况：Python的原生数组里包含了NumPy的对象的时候，这种情况下就允许不同大小元素的数组。
  （3）NumPy 数组有助于对大量数据进行高级数学和其他类型的操作。操作效率 > python原生数组 代码数量 < python原生数组。

 
2、Numpy为何会速度快？优点？
  （1）矢量化描述了代码中没有任何显式的循环，索引等。
  （2）简洁并更适应阅读。
  （3）更少的代码更少的错误。
  （4）更加接近标准的数学符号。
  （5）矢量化导致产生更多 “Pythonic” 代码。


3、基础知识
 （1）NumPy的主要对象是同构多维数组。它是一个元素表（通常是数字），所有类型都相同，由非负整数元组索引。在NumPy维度中称为 轴 。
 （2）NumPy的数组类被调用ndarray，它也被别名所知array。
     请注意，numpy.array这与标准Python库类不同array.array，后者只处理一维数组并提供较少的功能。
 （3）ndarray.ndim - 数组的轴（维度）的个数。在Python世界中，维度的数量被称为rank。
 	 ndim = len(shape) (数组维度个数) 
     
     ndarray.shape - 数组的维度。这是一个整数的元组，表示每个维度中数组的大小。对于有 n 行和 m 列的矩阵，shape 将是 (n,m)。因此，shape 元组的长度就是rank或维度的个数 ndim。
     
     ndarray.size - 数组元素的总数。size = shape 的元素的乘积。
     
     ndarray.dtype - 一个描述数组中元素类型的对象。可以使用标准的Python类型创建或指定dtype。另外NumPy提供它自己的类型。例如numpy.int32、numpy.int16和numpy.float64。
     
     ndarray.itemsize - 数组中每个元素的字节大小。例如，元素为 float64 类型的数组的 itemsize 为8（=64/8），而 complex32 类型的数组的 itemsize 为4（=32/8）。它等于 ndarray.dtype.itemsize 。
     元素为 float64 类型的数组的 itemsize 为8（=64/8），而 complex32 类型的数组的 itemsize 为4（=32/8）
     
     ndarray.data - 该缓冲区包含数组的实际元素。通常，我们不需要使用此属性，因为我们将使用索引访问数组中的元素。


4、数组创建
 （1）a = np.narry([1, 3, 2])
 （2）可以将序列的序列转换成二维数组，将序列的序列的序列转换成三维数组
 （3）显式指定数组的类型d = np.array([[1, 2], [3, 4]], dtype=complex)
 （4）函数zeros创建一个由0组成的数组，
     函数ones创建一个完整的数组，
     函数empty 创建一个数组，其初始内容是随机的，取决于内存的状态。默认情况下，创建的数组的dtype是 float64 类型的。

 （5）NumPy提供了一个类似于range的函数，该函数返回数组而不是列表。
     当arange与浮点参数一起使用时，由于有限的浮点精度，通常不可能预测所获得的元素的数量。
     出于这个原因，通常最好使用linspace函数来接收我们想要的元素数量的函数，而不是步长（step)

5、打印数组
   当您打印数组时，NumPy以与嵌套列表类似的方式显示它，但具有以下布局：
  （1）c = np.arange(24).reshape(2,3,4)         # 3d array 从左到右打印
  （2）b = np.arange(12).reshape(4,3)           # 2d array 从上到下打印
  （3）a = np.arange(6)                         # 1d array 其余部分也从上到下打印，每个切片用空行分隔
  （4）如果数组太大而无法打印，NumPy会自动跳过数组的中心部分并仅打印角点
      要禁用此行为并强制NumPy打印整个数组，可以使用更改打印选项set_printoptions
      np.set_printoptions(threshold=sys.maxsize)       # sys module should be imported


6、数组运算（支持运算符）
  数组上的算术运算符会应用到 元素 级别。
  （1）+ - *
  （2）与许多矩阵语言不同，乘积运算符*在NumPy数组中按元素进行运算。
      矩阵乘积可以使用@运算符（在python> = 3.5中）或dot函数
  （3）某些操作（例如+=和 *=）会更直接更改被操作的矩阵数组而不会创建新矩阵数组
  （4）当使用不同类型的数组进行操作时，结果数组的类型对应于更一般或更精确的数组（称为向上转换的行为）
  
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
import numpy as np
import numpy as pi
import sys

a = np.array([[5, 3, 7, 8],
              [2, 4, 8, 2],
              [2, 4, 8, 2],
              [2, 4, 8, 2]])
b = np.array([(1, 2, 3), (3, 2, 1)])
c = np.array([[5, 3, 7, 8],
              [2, 4, 8, 2],
              [
                  [2, 4, 8, 2],
                  [2, 4, 8, 2],
                  [3, 5, 7, 4]]])

d = np.array([[1, 2], [3, 4]], dtype=complex)  # 指定数组类型

e = np.zeros((3, 4))
e1 = np.ones((2, 3, 4), dtype=np.int16)
e2 = np.empty((2, 3))
e3 = np.arange(10, 30, 5)
e4 = np.arange(0, 2, 0.3)  # it accepts float arguments
e5 = np.linspace(0, 2, 9)  # 9 numbers from 0 to 2
np.linspace(0, 2, 9)
# x = np.linspace(0, 2 * pi, 100)  # useful to evaluate function at lots of points
# f = np.sin(x)
e6 = np.arange(24).reshape(2, 3, 4)  # 3d array 从左到右打印
e7 = np.arange(12).reshape(4, 3)  # 2d array 从上到下打印
e8 = np.arange(6)  # 1d array 其余部分也从上到下打印，每个切片用空行分隔print("数组维度：", a.shape,)
e9 = np.arange(10000)  # 如果数组太大而无法打印，NumPy会自动跳过数组的中心部分并仅打印角点
# print("数组轴数[shape个数]：", a.ndim)
# print("数组元素和[shape乘积]：", a.size)
# print("数组元素类型：", a.dtype.name)
# print("数组元素字节大小：", a.itemsize)
# print("缓冲区包含数组的实际元素：", a.data)
# print("三位数组：", b)
# print(d)
# print(e6)
# print(e7)
# print(e8)
# print(e9)
np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported
# print(np.arange(10000).reshape(100, 100))
a1 = np.array([20, 30, 40, 50])
b1 = np.arange(4)
c1 = a1 - b1
d1 = b1 ** 2
d2 = 10 * np.sin(a1)
d3 = a1 < 35
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
# print(A * B)        # elementwise product
# print(A @ B)        # matrix product
# print(A.dot(B))     # matrix product

a2 = np.ones((2, 3), dtype=int)
b2 = np.random.random((2, 3))
a2 *= 3
b2 += a2
# a2 += b2              # b is not automatically converted to integer type
# print(a2)
# print(b2)
# print(a2)
aa = np.ones(3, dtype=np.int32)
bb = np.linspace(0, pi, 3)
cc = bb.dtype.name
print(cc)
