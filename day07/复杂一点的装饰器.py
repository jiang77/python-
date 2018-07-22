def say(age):
    print("sunck is %d years old" % (age))
# 需求，不改变say函数本身，如果传-10，则打印0
say(-10)

def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner
say = outer(say)
say(-10)