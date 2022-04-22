import numpy as np
import pandas as pd

'''
# 1、创建Series 
说明：Series是带有显示索引的一维数组。可以从列表或数组中创建它
'''
num_list =[0.25, 0.5, 0.75, 1.0]

# 创建Numpy 一维数组
num_data = np.array(num_list)
print(num_data)
#输出
# [0.25 0.5  0.75 1.  ]

# 通过列表创建Series数据结构
ser_data = pd.Series(num_list)
print(ser_data)
#输出
# 0    0.25
# 1    0.50
# 2    0.75
# 3    1.00
# dtype: float64

# 通过numpy一维数组创建Series数据结构
ser_num = pd.Series(num_data)
print(ser_num)
#输出
# 0    0.25
# 1    0.50
# 2    0.75
# 3    1.00
# dtype: float64

# 创建Series指定列表中每个元素的索引
num_list_si = pd.Series(num_list,index=['a','b','c','d'])
print(num_list_si)
# a    0.25
# b    0.50
# c    0.75
# d    1.00
# dtype: float64


# 通过字典创建Series
d = {"a": 0.0, "b": 1.0, "c": 2.0}
ds = pd.Series(d)
print(ds)

# 输出
'''
a    0.0
b    1.0
c    2.0
dtype: float64
'''

# 通过index 改变字典中key-value的顺序
# 通过添加字典中没有的key 会以NaN来占位。
dsi =pd.Series(d, index=["b", "c", "d", "a"])
print(dsi)
# b    1.0
# c    2.0
# d    NaN
# a    0.0
# dtype: float64

# 通过添加多个index ，对应一个固定值
pd.Series(5.0, index=["a", "b", "c", "d", "e"])
# a    5.0
# b    5.0
# c    5.0
# d    5.0
# e    5.0
# dtype: float64



# 也可以用非连续数字来作为索引
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=[2, 5, 3, 7])
print(data)
print(data[5])


# 只显示和构建设置了显示索引的数据
print(pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2]))
# 3    c
# 2    a
# dtype: object


'''
# 2、Series 重要属性 
'''

print(ser_data)
# 输出
# 0    0.25
# 1    0.50
# 2    0.75
# 3    1.00
# dtype: float64

# 通过values 返回numpy数组
print(ser_data.values)
# 输出
# [0.25 0.5  0.75 1.  ]

#Series 就是numpy 数字 + 显示索引


# 获取Series索引
print(ser_data.index)
# 输出
# RangeIndex(start=0, stop=4, step=1)

# 获取Series数据结构中元素的数量
ser_data.size

# 当元素都是唯一的返回ture
ser_data.is_unique

#访问Series 里面数据
# 通过索引访问它
print(ser_data[3])
#输出
# 0.5


# 通过切片来访问它
print(ser_data[1:3])
# 输出
# 1    0.50
# 2    0.75
# dtype: float64

print(ds)
# a    0.0
# b    1.0
# c    2.0
# dtype: float64


print(ds['b'])
#输出
# 1.0

# 字典创建的Series 也支持切片
print(ds['a':'b'])
# a    0.0
# b    1.0
# c    2.0
# dtype: float64




