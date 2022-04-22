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

# for i, word in text_gen:
#     if word == '年' and str(year) not in text_List:
#         text_List.insert(i, str(year))
#         next(text_gen)
#
#     elif word == '月' and str(month) not in text_List:
#         text_List.insert(i, str(month))
#         next(text_gen)
#
#     elif word == '号' and str(day) not in text_List:
#         text_List.insert(i, str(day))
#         next(text_gen)
#
#     elif word == '周' and str(many_year) not in text_List:
#         text_List.insert(i, str(many_year))
#         next(text_gen)

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

abc = [1,23,'haha',None,'  ','']

d = []
for i in abc:
    if i:
        d.append(i)

print(d)







