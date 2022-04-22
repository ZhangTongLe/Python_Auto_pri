import pandas as pd
import numpy as np

'''
# 1、通过两个Series 创建DataFrame
'''

# 北京、上海、天津城市面积
area_dict = {'beijing': 16410, 'shanghai': 6340.5, 'tianjing': 11966.45}

# 北京、上海、天津城市人口数
population_dict = {'beijing': 2153.6,
                   'shanghai': 2428.14,
                   'tianjing': 1561.83}


population = pd.Series(population_dict)
area = pd.Series(area_dict)


# 通过两个Series 创建一个DataFrame. 每个Series 是一列。
city_info = pd.DataFrame({'population': population,
                          'area': area})
print(city_info)

# 输出
#         population      area
# beijing      2153.60  16410.00
# shanghai     2428.14   6340.50
# tianjing     1561.83  11966.45

print(city_info['area'])  # 访问某列就是返回Series数据
# beijing     16410.00
# shanghai     6340.50
# tianjing    11966.45
# Name: area, dtype: float64

# 自定义行索引（Y ）轴索引为 人口，面积
area_infos = pd.DataFrame(data=[population, area], index=['人口', '面积'])
print(area_infos)
#     beijing  shanghai  tianjing
# 人口   2153.6   2428.14   1561.83
# 面积  16410.0   6340.50  11966.45

# 行列索引交换，相当于把DataFram 垂直向右旋转90度。
print(area_infos.T)
#         人口        面积
# beijing   2153.60  16410.00
# shanghai  2428.14   6340.50
# tianjing  1561.83  11966.45


# 构建单列的DataFrame
print(pd.DataFrame(population, columns=['population']))


# 创建DataFrame
# 的时候，可以通过index
# 指定行索引的名称。也可以通过T，来转置行列索引，让数据看的更加清晰。

# 通过字典嵌套列表生成DataFrame
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

df
#    col1  col2
# 0     1     3
# 1     2     4



# 通过 numpy 二维数组创建DataFrame
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
df2

#    a  b  c
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

# Columns :指定列的索引。

'''
# 2、获取DataFrame重要属性，
通过index、columns、values

'''


# 获取行索引（Y轴）
print(city_info.index)
# Index(['beijing', 'shanghai', 'tianjing'], dtype='object')

# 获取列索引(X轴)
print(city_info.columns)
# Index(['population', 'area'], dtype='object')

# 获取numpy二维数组数据
print(city_info.values)
# [[ 2153.6  16410.  ]
#  [ 2428.14  6340.5 ]
#  [ 1561.83 11966.45]]

# 获取DataFrame 的形状（3行2列）
print(city_info.shape)
# (3, 2)


# 以列表形式返回Y轴索引、X轴索引
# 相当于访问index 和columns
print(city_info.axes)
# [Index(['beijing', 'shanghai', 'tianjing'], dtype='object'),
# Index(['population', 'area'], dtype='object')]

print(city_info)



'''
# 3、显示index索引类型操作

'''



ind = pd.Index([2, 3, 5, 7, 11])

print(ind)
# Int64Index([2, 3, 5, 7, 11], dtype='int64')

print(ind[1])  # 通过索引查询显示索引数据
# 3

print(ind[:3])  # 通过切片查询数据
# Int64Index([2, 3, 5], dtype='int64')


print(ind.size, ind.shape, ind.ndim, ind.dtype)  # 具有numpy一维数组的属性
# 5 (5,) 1 int64


ind[1] = 0  # 报错，索引是不支持可变操作
# 这种不变性使得多个DataFrame之间的共享数据索引而不会
# 产生无意间修改索引而产生副作用。

# 索引的逻辑处理
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])

print(indA & indB)  # 找出a，b 共同的索引
# Int64Index([3, 5, 7], dtype='int64')

print(indA | indB)  # 找出A,B总共的索引
# Int64Index([1, 2, 3, 5, 7, 9, 11], dtype='int64')

print(indA ^ indB)  # 找出a,b 不重复的索引
# Int64Index([1, 2, 9, 11], dtype='int64')