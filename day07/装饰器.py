'''
概念：是一个闭包，把一个函数当做参数返回一个替代版的函数。本质上就是一个返回函数的函数。


'''

# 简单的装饰器
def func1():
    print("sunck is a good man")

# 需求：在不改变func1函数的情况下，在其前面减伤一串星号（*）

def outer(func):
    def inner():
        print("*************************")
        func()
    return inner
# f是函数func1的加强版本
f = outer(func1)  # 调用者用f去保存返回的函数inner，所以f就是个函数
f()
