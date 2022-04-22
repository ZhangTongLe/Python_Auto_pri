# 迭代器（iterator）
# 实现了方法 __next__ 的对象是迭代器。

list

# 使用iter内置函数把字符串 转换成迭代器。
# 可以使用next 函数，来获取容器中的下一个值，也可以通过计算产生新值。
s = 'abc' # 字符串不是迭代器。
it = iter(s)

next(it)
next(it)
next(it)
next(it)  # StopIteration



# 了解了迭代器协议背后的机制后，很容易将迭代器行为添加 到您的类中。定义一个__iter__()方法，该方法返回一个带有__next__()方法的对象

class Reverse:
    """用于向后循环序列的迭代器。"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
next(rev)


# for 循环会自动处理StopIteration 这个异常，并退出循环。
for char in rev:
    print(char)



# list



from collections.abc import Iterator # 迭代器
from collections.abc import Iterable # 可迭代对象

isinstance(rev, Iterator) # True
m = map(lambda x: x **2, [1,2,3,4,5])
next(m)

isinstance(m, Iterator) # True

isinstance(m, Iterable) #

isinstance([1,2,3], Iterable) # 可迭代对象，只有__iter__ True

# 可迭代：可以理解为可遍历，可循环。


########################扩展#####################################

# 可迭代、不可迭代区分
# 可用于for in 的是可迭代对象，

# 不能用于for in 例如基本的数据类型是不可迭代对象，和没有定义iter函数的对象。

for i in 100:print(i) # TypeError: 'int' object is not iterable


# python中序列分为可变和不可变序列

# 可变序列：列表，字典，值变了，地址不一定变.

dict_stu = {'小红':98}


# 不可变序列：数字类型、元组，字符串，值变了，地址一定变.

# 不可变序列不允许变量的值发生变化，

# 如果改变了变量的值，相当于是新建了一个对象新开辟一个内存区来存放该值；
#
# 而对于相同值的对象，通过增加引用计数，来表示引用方式的增加而实际上在内存中则只有一个对象（一个地址），即这些引用都指向同一个地址。
#

a = ['张','同','乐']
print(id(a)) # 93060296

a[1] = '不'
a # ['张', '不', '乐']
print(id(a)) # 地址没变 # 93060296

b = ('同','乐')
print(id(b)) # 100264968
b = b + ('张','呵呵')
print(id(b)) # 81694056


str_test = '人生就像一场戏'
print(id(str_test)) #97215304

str_test = str_test.strip()
print(id(str_test)) #97215304


aa = '1'
aab = '1'

id(aa) == id(aab) # True


isinstance([1, 2, 3], Iterator)






