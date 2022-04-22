for i  in  range(6): # 通过range函数会生成索引从0 到5.
    print(i)


# 2 :step
for i in range(1,5,2): # 生成从索引1开始3结束。 5是边界不被包含。
    print(i)

for i in range(1,-10,-1): # 生成从索引1 逆序 步长为1, 从1 到-9
    print(i)


# for正常执行完，else也会跟着执行。
# for没有正常执行完，中间异常退出，则else也不会执行
for n in range(1,10):
    if n == 11:
        break
else:
    print("Didn't find it!")




list(range(0, 30, 5)) # [0, 5, 10, 15, 20, 25]



# 总结：range类型表示不可变的数字序列，通常用于在 for 循环中循环指定的次数。
#       放在list函数中，生成数字序列。


# range(start, stop[, step])
# 最多可包含三个参数
# start开始参数，如果缺省，则从0开始
# stop结束参数，这个是必须的
# step步进值，如果缺省，则为1


# 遍历列表时候，获取列表的索引
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for k,v in enumerate(seasons,start=1):
    print(k,v)


