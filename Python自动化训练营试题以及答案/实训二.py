"""
# 1、使用Python  将下列四个变量year、month、day 、many_year
# 拼接到不完整text的字符串当中，实现输出完整形式为：“2021年7月1号是中国共产党成立100周年。”
# year = 2021、month =7 、day = 1 、many_year = 100
# text = "年月号是中国共产党成立周年。"
"""

year = 2021
month = 7
day = 1
many_year = 100
text = "年月号是中国共产党成立周年。"

# 按照课程大纲学习进度的解题方式
# res = str(year) + '年'+str(month)+'月' + str(day)+'号是中国共产党成立'+str(many_year)+'周年。'
# print(res)

# 学完了按照高级的思维方式
text_List = [word for word in text]
text_gen = enumerate(text_List)

for i, word in text_gen:
    if word == '年' and str(year) not in text_List:
        text_List.insert(i, str(year))
        next(text_gen)

    elif word == '月' and str(month) not in text_List:
        text_List.insert(i, str(month))
        next(text_gen)

    elif word == '号' and str(day) not in text_List:
        text_List.insert(i, str(day))
        next(text_gen)

    elif word == '周' and str(many_year) not in text_List:
        text_List.insert(i, str(many_year))
        next(text_gen)

print(''.join(text_List))

# n = 0  # 控制循环一次
# while True:
#     if text_List[n] == '年' and str(year) not in text_List:
#         text_List.insert(n, str(year))
#         n += 2
#     if text_List[n] == '月' and str(month) not in text_List:
#         text_List.insert(n, str(month))
#         n += 2
#     if text_List[n] == '号' and str(day) not in text_List:
#         text_List.insert(n, str(day))
#         n += 2
#
#     if text_List[n] == '周' and str(many_year) not in text_List:
#         text_List.insert(n, str(many_year))
#
#     elif text_List[n] == '。':
#         break
#
#     else:
#         n += 1
#
# print(''.join(text_List))


"""
# 2、来找出 a 列表中 [0,-1,2,-10,9,5] 
列表中小于5的数字，并装进b 列表，并把b 列表排好序进行打印输出。
"""

a = [0, -1, 2, -10, 9, 5]
#
# b = []
# for num in a:
#     if num < 5:
#         b.append(num)
# print(b)
#
# # 高级
# b = [num for num in a if num < 5]
# print(b)

list(filter(lambda x: x < 5, a))




"""
# 3、使用Python 的While 循环技术计算出投资的年利率为7.8%，
试求从2万块增长到8万块，需要花费多少年 以及打印出投资两年后的收益。。
"""
# money = 20000
# year = 0
# while money <= 100000:
#     money = money + (money * 0.25)
#     year += 1
#     if year == 2:
#         print(money)
#
# print(year)

"""
4、现有同乐学堂博客中2021年07月10号的 web系统访问日志（apache_byu4034710001_20210710.log），需要读取log日志文件，并且过滤出里面的IP地址。把文件中的所有ip装载到列表中，对列表中的ip 进行去重, 并统计出7月10号有多少个用户访问同乐学堂。
去重提示：可以使用set 数据结构，例如 ：set([1,2,3,4,5,3])  的功能是去除列表中的重复数字3
# 提取IP地址正则：regex = r'\d+\.\d+\.\d+\.\d+'
获取列表的长度函数：len
"""
import os
import re
import ipaddress

regex = r'\d+\.\d+\.\d+\.\d+'
path = os.path.abspath('.') + '\\apache_byu4034710001_20210710.log'


# 验证是否有效IP
def check_ip_valid(ip):
    try:
        ipaddress.ip_address(ip.strip())
        return True
    except ValueError as e:
        return False


# 方式1： 通过列表装载有效IP。
ip_list_one = []
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        ipadd = line.split('- -')[0].strip()
        if check_ip_valid(ipadd):
            ip_list_one.append(ipadd)

print('第一种方式：列表装有效IP', len(set(ip_list_one)))  # 1400 个有效不重复IP


# 方式2： 通过生成器模式来计算有效IP
def read_file(path_name):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            ipadd = line.split('- -')[0].strip()
            if check_ip_valid(ipadd):
                yield ipadd


ip_gen = read_file(path)
print('第二种方式：生成器模式来计算有效IP', len(set(ip_gen)))  # 1400 个有效不重复IP

# 方式3： 通过正则表达式全文匹配，装进列表
with open(path, 'r', encoding='utf-8') as f:
    log_content = f.read()
#
ip_find_list = re.findall(regex, log_content)
fil_ip_list = list(filter(check_ip_valid, ip_find_list))

print('第三种方式；正则表达加过滤', len(set(fil_ip_list)))  # 1403个有效IP

# {'12.19.0.11', '12.18.5.10', '12.19.0.0'}
print('方式一与方式三，异同', set(fil_ip_list) - set(ip_list_one))
