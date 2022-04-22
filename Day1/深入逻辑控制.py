
'''
例如 a < b == c 审核是否 :a 小于 b 并且 b 等于 c。
not 具有最高的优先级，and 次之、 or 优先级最低.
所以 A and not B or C 等于 (A and (notB)) or C。
括号也可以用于比较表达式。

'''

# not and or

# if xx
#     if xxx
#         if xxx
#


import pandas

a = 2
b = 3
c = 4

#是否 :a 小于 b 并且 b 等于 c。

if  a < b == c :
    print('haha')

else:
    print('hehe')


# 所以 A and not B or C 等于 (A and (notB)) or C。
# not 具有最高的优先级，and 次之、 or 优先级最低.
# 所以 A and not B or C 等于 (A and (notB)) or C。
# 括号也可以用于比较表达式。


if  a ==2 and not b ==3  or c ==b:
    print(1)
else:
    print(2)

# 逻辑操作符 and 和 or 也称作短路操作符：它们的参数从左向右解析，
# 一旦结果可以确定就停止

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null # 'Trondheim'





