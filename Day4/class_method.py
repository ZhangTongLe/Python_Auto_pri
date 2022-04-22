"""

Python 有 3 个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法。
类方法，类可以直接调用。
静态方法：脱离类存在的，使用工具类的时候，不要跟谁进行绑定。
实例方法：实例对象可以操作的方法，可以操作实例变量。

"""


class Person:
    score = 99

    def __init__(self, age):
        self.age = age

    def add_age(self):
        self.age += 1

    @staticmethod
    def add_age_static():
        print('我是静态函数')

    @classmethod
    def add_age_class(cls, age_dict):  # self 代表的是类实例，cls 代表未被实例的类，指类名。

        # 业务逻辑的处理
        age = age_dict['小红']

        print(cls(age).age)

        age = cls(age).age + 100

        return age


if __name__ == "__main__":
    # pass

    """普通方法使用方式"""
    # p = Person(65)
    # p.add_age()
    # print('普通函数年龄加1',p.age)
    #
    # p.age = p.age+1
    # print(p.age)

    """静态函数使用方式"""
    # Person.add_age_static()

    """类函数使用方式"""
    p = Person.add_age_class({'小红': 28})
    print('类函数调整分数', p)

'''
区别
1、普通函数 ，它只能被类的实例调用。
   静态函数与类函数，可以通过类名直接调用

2、静态函数与类函数的区别,@注解修饰符不同
   类函数有cls参数，而静态函数没有cls参数。

'''
