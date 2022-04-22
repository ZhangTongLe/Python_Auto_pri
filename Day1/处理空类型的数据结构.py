# 1、去除空格、None
none_list = ['a','','b','',None,'c','',' ',None, 56, "    ",'   ',"nihao",'\\']


# 列表生成式：把简单的代码，放到列表里面，直接过滤好想好的数据
mytest = [i for i in none_list if len(str(i).strip()) != 0 and i is not None ]
# ['a', 'b', 'c', 56, 'nihao', '\\']


print(mytest)

# 2、删除列表中的nan
import pandas as pd
import numpy as np

excel_path = 'F:\Python自动化办公训练营\Day1\house.xlsx'
houses = pd.read_excel(excel_path)
print(houses.shape)


# 取出 朝向列中，唯一不重复的值
listType = houses['朝向'].unique()

print(type(listType))  # class 'numpy.ndarray'>
listType

list_res = list(listType)

print('带有nan的列表',list_res) # ['朝南', '朝西', '朝东', '朝北', nan]

list_res.remove(np.nan)

while np.nan in list_res :
    list_res.remove(np.nan)
print('处理好的列表',list_res)

dict.update()


######面积列有空数据，有nan ####

houses.isna().sum() # 统计NA数据

houses['面积'].isna().sum() #8


# notna() notnull()

# 数据清理
df = houses.loc[houses['面积'].notna(), ['楼盘名称', '面积', '房租']].reindex()

df.shape # (889, 4)


df.isna().sum()




