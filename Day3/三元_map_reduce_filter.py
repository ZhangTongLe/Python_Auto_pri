# 三元运算符
is_fat = False
state = "123" if is_fat else "456"
print(state)




##########1、map 函数使用############################
# 把map 第一个参数的规则，映射到第二个列表里的每一个元素

list( map(lambda x: x **2, [1,2,3,4,5]))

a =[i **2 for i in [1,2,3,4,5]]
print(a)


##########2、filter 函数使用############################
# 过滤器
less_than_zero = filter(lambda x: x < 0, [-5,1,3,-2,5,7])
print(list(less_than_zero))
#輸出結果
#[-5, -2]

b =[i for i in [-5,1,3,-2,5,7] if i<0 ]
print(b)




############### map 结合filter##################################

a = [6,9,10,4,5,8,2,1]



res = map(lambda x:x**2,filter(lambda x:x%2==0,a))
print(list(res))





# 一行代码实现对列表a中的偶数位置的元素进行加3后求和(阿里校招)


a = [6,9,10,4,5,8,2,1]
# 一行代码实现对列表a中的奇数的元素进行加5后求和
9, 5, 1

[ a_v for a_k,a_v in enumerate(a) if a_v%2 != 0]  # [9, 5, 1]









# oushu =  list(filter(lambda x:x%2==0,a)) #[6, 10, 4, 8, 2]


# oushu_3 =  list(map(lambda x:x+3,oushu)) # [9, 13, 7, 11, 5]
# sum(oushu_3)
# sum(list(map(lambda x:x+3,filter(lambda x:x%2==0,a))))

# [a[a_k]+3 for a_k,a_v in enumerate(a) if a_v%2==0]



sum([a[a_k]+5 for a_k,a_v in enumerate(a) if a_v%2 != 0]) # 30




from functools import reduce
# 如果map 和  filter ，不够优雅，可以使用推导式、

product = reduce( (lambda x, y: x * y), [1, 2, 3, 5] ) #30

print(product)
#輸出結果：30



#自定义函数
x=[3,4,6,8,8]

def fun(x,y):
    return x+y

print(reduce(fun,x))


reduce(lambda x, y : x + y, map( lambda i: i+3, filter( lambda y:y%2 == 0, a) ) )

a = [6,9,10,4,5,8,2,1,7,12]

reduce(lambda x, y : x + y, map( lambda i: i+0, filter( lambda y:y%2 == 0, a) ) )

'''
计算原理：
先计算头两个元素：f(3,4),结果为7；
再把结果和第三个元素6计算：f(7,6),结果为13；
再把结果和第四个元素8计算：f(13,8),结果为21;
再把结果和第四个元素8计算：f(21,8),结果为29;
'''













