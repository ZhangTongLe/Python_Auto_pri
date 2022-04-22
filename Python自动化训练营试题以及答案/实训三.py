import pandas as pd
import os

excel_path = os.path.abspath('.') + "\\house.xlsx"
excel_path = r"D:\rd\PyJob\tongle\Python自动化训练营试题以及答案\house.xlsx"
houses = pd.read_excel(excel_path)
print(houses.shape)

# 1、 统计出面积小于60平米的房子有多少个
houses['面积'] = houses['面积'].str.split('㎡', expand=True)[0].astype("float")

smaller_60 = houses['面积'] < 60

area_60 = len(houses[smaller_60])
print('面积小于60的房子有:', area_60, '个')  # 2779个

# 2、 统计面积小于60平米的房子的平均租金
houses['房租'] = houses['房租'].str.split('元', expand=True)[0].astype("int")
avg_fz = houses['房租'][smaller_60].mean()

avg_fz_smaler_60 = round(avg_fz, 2)
print('面积小于60平米的房子的平均租金为:', avg_fz_smaler_60, '元')

# 3、统计出租金大于5千小于1万的房子有多少个？
more_5000 = houses['房租'] > 5000
less_10000 = houses['房租'] < 10000
house_5k_10k = houses[more_5000 & less_10000]
print('大于5千小于1万的房子有', len(house_5k_10k), '个')

# 4、统计标签中采光好并且 租金大于5千小于1万的房子有多少个？
cgh = houses['标签'].str.contains('采光好')
house_5k_10k = houses[more_5000 & less_10000 & cgh]
print('采光好并且 租金大于5千小于1万的房子有', len(house_5k_10k), '个')

# 5 、统计统计标签中采光好并且 租金大于5千小于1万的房子的平均租金是多少？
house_5k_10k_avg = house_5k_10k['房租'].mean()
print('采光好并且 租金大于5千小于1万的房子的平均租金为:', round(house_5k_10k_avg, 2), '元')

# 6、通过requests、bs4
# 获取http://www.ztloo.com/sum_number.html 网页中所有数字，
# 并计算出他们相加之后的总和.
import requests
from bs4 import BeautifulSoup

url = 'http://www.ztloo.com/sum_number.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
nums = soup.find_all('div', attrs={"class": "col-md-1"})  # 找到所有 数字
num_list = [int(i.text.strip()) for i in nums]
print(len(num_list), sum(num_list))

# 7、获取同乐学堂首页热门标签内容，装载在字典中，并打印输出。
# 例如：{‘mysql’:198,'python'：69}
import re

url_index = 'http://www.ztloo.com'
res = requests.get(url_index)
soup = BeautifulSoup(res.text, 'html.parser')
res = soup.find_all(href=re.compile("tag"))
dict_res = {}
for i in res:
    a = i.text.split('(')  #
    dict_tup = tuple(map(lambda x: x.strip().replace(')', ''), a))
    number_filter_V = list(filter(str.isdigit, dict_tup[1]))
    number_V = int(''.join(number_filter_V))
    dict_res.setdefault(dict_tup[0], number_V)

dict(sorted(dict_res.items(), key=lambda x: x[1], reverse=True))

# 8、获取标签为python 文章的，
# 前三篇文章的，发布日期装进列表，打印输出。
url_tag_py = 'http://www.ztloo.com/tag/python/'
res_date = requests.get(url_tag_py)
soup = BeautifulSoup(res_date.text, 'html.parser')
res = soup.find_all('time')
res_date_list = []
for i in range(3):
    res_date_list.append(res[i].text)
print(res_date_list)


