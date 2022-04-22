
# 1题解析，看instance 里面最外层的函数int.
# int 类型并不属于str 和float
# 数字加点，代表浮点数ininstance 的第二个参数类型是个元组，可以同时对多个类型进行判断。
isinstance(int(123.+ float(1.23)), (str,float,))


# 2题解析，对sorted 函数的掌握
list_students = ['小明', '小红', 1, 2, '小乐', '小刚', 1, '小乐', '小明', 2]
sorted(set(list_students), key=list_students.index)

x = [3, 5, 7]
x[4:]


type(eval('111344'))

sorted()

a = [1,2,]
a.sort()