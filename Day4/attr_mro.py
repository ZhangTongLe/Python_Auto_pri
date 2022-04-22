#新式类
class D:
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B, C):
    pass


# 了解解类多继承顺序和原理
print(A.__mro__)
