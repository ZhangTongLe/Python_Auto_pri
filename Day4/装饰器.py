# 装饰器(叫语法糖也叫注解)：把函数作为参数赋值给另一个函数
import requests
from retry import retry


def say_Chinese():
    return "我是say_Chinese"


def say_English():
    return "我是say_English"


def say(func):
    return func()


def say_middle(func):
    # 装饰函数
    def wrapFunction():
        print("说话之前，准备演讲稿")  #
        say_style = func()
        print(say_style)
        print("说话完毕，进行总结")

        return say_style

    return wrapFunction


def say_middle(func):
    # 装饰函数
    def wrapFunction():
        print("说话之前，准备演讲稿")  #
        say_style = func()
        print("说话完毕，进行总结")

        return say_style

        # 装饰函数

    def wrapFunction1():
        print("说话之前，准备演讲稿")  #
        say_style = func()
        print("说话完毕，进行总结")
        return say_style

    if func() == 12:
        return wrapFunction1

    return wrapFunction


#
#
@say_middle
def say_People():
    return "我是say_People"


#
#
from functools import wraps  # 为了不改变被装饰函数或类的性质,添加functools.wrap装饰器


def say_high(func):
    @wraps(func)
    def wrapFunction():
        print("说话之前，准备演讲稿")  #
        say_style = func()
        print(say_style)
        print("说话完毕，进行总结")
        return say_style

    return wrapFunction


@say_high
def say_Rap():
    return "我是say_Rap"


class Say_Super:

    def __call__(self, func):
        @wraps(func)
        def wrapFunction():
            print("说话之前，准备演讲稿")  #
            say_style = func()
            print(say_style)
            print("说话完毕，进行总结")
            return say_style

        return wrapFunction


#
#
@Say_Super()
def say_Code():
    return "我是say_Code"


#
#
import time


def timing(func):
    @wraps(func)
    def with_time(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        print('函数: {name} {param} 执行完毕, 花费时间: {time}s'.format(name=func.__name__, param=(args, kwargs), time=run_time))
        return res

    return with_time


#
#
#
@timing
def add(x, y):
    s = x + y
    time.sleep(5)
    print('the sum is: {0}'.format(s))
    return s


def to_uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        if not isinstance(text, str):
            raise TypeError('你传的参数不是字符串，请重新输入')
        return text.upper()

    return wrapper


@to_uppercase
@retry
def say_Language(say_str):
    return say_str


def retry_requests(retries=3, delay=5):
    def try_request(fun):
        @wraps(fun)
        def retry_decorators(*args, **kwargs):
            for _ in range(retries):
                res = fun(*args, **kwargs)
                print(res)
                time.sleep(delay)

        return retry_decorators

    return try_request


class ApiRequest:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    @retry_requests(retries=5, delay=1)
    def create_request(self):
        res = requests.get(url=self.url, headers=self.headers)

        return res


if __name__ == '__main__':
    ##########简单装饰函数###############
    # print(say(say_Chinese))

    ##########自定义装饰函数#############
    # say_English =say_middle(say_English)
    # say_English()

    #########注解型装饰器函数############
    # say_People()
    # print(say_People.__name__) #wrapFunction

    #########优化过的装饰器函数##########
    # say_Rap()
    # print(say_Rap.__name__)

    #########装饰器类####################
    # say_Code()

    ###__call__：把Say_Super当函数来用###
    # ss = Say_Super()
    # say_Chinese = ss(say_Chinese)
    # say_Chinese()

    ###########函数计时########################
    # add(6,7)

    ###########传参########################
    # language = say_Language('speak chinese')
    # print(language)

    aq = ApiRequest('http://www.ztloo.com', headers=None)
    aq.create_request()
