#coding=utf-8
class Demo(object):
    """
        __slots__ 强制定义类属性信息
    """
    __slots__ = ('name','age')



if __name__=='__main__':
    de = Demo()
    de.name = 'aszhou'
    print de.name
    de.age = 100
    print de.age


    de.scope = 100
    print de.scope





