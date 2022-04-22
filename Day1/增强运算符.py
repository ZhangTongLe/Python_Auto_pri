a=[1,3,5,6]
b=[1,2,3]


# 相当于a -b的差值。
# 这种事复杂和不允许的，一定要先找通用技巧，一行代码的解决，千万不要乱用for 和if。
for i in a:
   if i not in b:
        print(i)


set(a) - set(b)



# if 和关系符结合
def luoji4():
    i =3
    if i is not None:  # 如果i 不是空值
        print(i)
    i = None

    if i is None:
        print('1')
    a = 6
    b = 3
    c = 4


# if data is None or "&" not in data:
#     return data
#
#
# if repl is not None:


if not len('hello') <3:
    print(True)
else:
    print(False)




# 身份运算符:  【is】、【is not】
# 成员运算符:  【in】、【not in】

# 逻辑运算符:【and】 【or】【not】
