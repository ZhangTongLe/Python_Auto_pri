
# 类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性

class Person:
    def __init__(self):
        self._age =  None

    @property
    def age(self): # 把函数降维成了公开的变量。
        """获取当前年龄."""
        return self._age

    @age.setter # 用来限定设设置变量值的时候，进行严格检查。
    def age(self,value):
        """修改当前年龄."""
        if not isinstance(value,int):
            raise ValueError('修改年龄值必须是整数类型')

        if not (0 <= value <=100):
            raise ValueError('年龄必须在0 到100 之间')

        self._age = value



if __name__ == '__main__':
    p = Person()
    p.age =101
    print(p.age)

