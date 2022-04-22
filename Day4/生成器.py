# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 生成器 是一个用于创建迭代器的简单而强大的工具。

# 生成迭代器。

# 生成迭代器 ,缩写：生成器。
import random


def reverse(data):
    print('开始')
    for index in range(len(data) - 1, -1, -1):
        print('for开始')

        yield data[index]  # 调用next停止的地方 ，

        print('for结束')  # 生成器从它停止的地方恢复

    print('结束')


rev = reverse('golf')
next(rev)

for char in reverse('golf'):
    print(char)

from collections.abc import Iterator  # 迭代器

isinstance(rev, Iterator)  # True


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


g = sample()

isinstance(g, Iterator)  # True

next(g)

for gs in g:
    print(gs)

# list(range(0.5,0.8,0.2))

range()


# 生产某个范围内浮点数的生成器：
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


range(0.5, 6.5, 0.2)
# TypeError: 'float' object cannot be interpreted as an integer

fr = frange(0.5,6.5,0.2)
next(fr)


# Generator 表达式

a = [i * i for i in range(10)]

a = (i * i for i in range(10))
print(a)

sum(a)
isinstance(a, Iterator)  # True

# 等价,简写
sum(i * i for i in range(10))


def read_file_line(file_name):
    """读取文件并返回文件的每一行.
    @param file_name:文件的绝对路径.
    @return: yiled line.
    """

    with open(file_name, encoding='utf-8', errors='ignore') as fread:
        for line in fread:
            yield line


file_path = 'F:\Python自动化办公训练营\Day4\装饰器.py'

file_gen = read_file_line(file_path)
# next(file_gen)

for i in file_gen:
    if 'say(func)' in i:
        print(i)
        break  # #def say(func):
