rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]



from operator import itemgetter

# 按照fname 排序
rows_by_fname = sorted(rows, key=itemgetter('fname'))

rows_by_fname



# 按照uid 排序
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_uid




# itemgetter函数同时也支持多个 key 进行排序，代码如下

# 按照lname 和fname 多个key 进行排序
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))

rows_by_lfname



# 同样内置函数max,min 函数
print(min(rows, key=itemgetter('uid')))
#输出结果： {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
