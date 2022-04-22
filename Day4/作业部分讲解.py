
import pandas as pd

excel_path = 'E:\\Python_Office_Auto\\Day7\\house.xlsx'
houses = pd.read_excel(excel_path)


houses['房租'] = houses['房租'].str.split('元',expand=True)[0].astype("int")

houses['面积'].isnull().sum() # 8

houses['面积'].dropna(inplace=True)
houses['面积'].isnull().sum() # 8


houses['面积'] = houses['面积'].str.split('㎡',expand=True)[0].astype("int")



# 面积小于60的房子有多少个
# len(houses[houses['面积'] < 60])
houses[houses['面积'] < 60]['面积'].count() # 2779


# 把house 标签为空的异常数据，填充为暂无标签
houses['标签'] = houses['标签'].fillna('暂无')


# house_5k =houses[ houses['房租'] > 5000]



house_5k_10k =  houses[(houses['房租'] > 5000) & (houses['房租'] <10000) & houses['标签'].str.contains('采光好') ]

len(house_5k_10k) # 584


# 统计标签中采光好并且 租金大于5千小于1万的房子的平均租金是多少
round(house_5k_10k['房租'].mean(),2) # 平均价格

