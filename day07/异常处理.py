'''





'''

# 需求：当程序遇到问题时，不让程序结束，而越过错误继续向下执行

'''
try……except……else
格式
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
except 错误码 as e:
    语句n
else:
    语句e
注意：else语句可有可无
    

作用：用来检测try语句块中（语句t）的错误，从而让except语句捕获错误信息并处理

逻辑：当程序执行到try-except-else语句时
1.如果当try“语句t”执行出现错误，会匹配第一个错误码，如果匹配上就执行对应的“语句”
2.如果当try“语句t”执行出现错误，但没有匹配的异常（没有一个正确的错误码来匹配），
  错误将会被提交到上一层的try语句或者到程序的最上层
3.如果当try“语句t”执行没有出现错误，不不会去匹配任何异常，而是执行else下的“语句e”
  但前提是你得有else语句

'''
# 1.每种错误码分着去匹配
try:
    print(3 / 1)
except NameError as e:
    print("没有该变量")
except ZeroDivisionError as e:
    print("除数为0了")
else:
    print("代码没有问题")
# 自己去百度错误码都有哪些



# 2.使用except而不使用任何的错误类型（不管什么错误码，只要错误就匹配）
try:
    print(4 / 0)
except:
    print("程序出现了异常")


# 使用带着多种异常（捕获多种异常）
# 3.一个except匹配多种错误码
try:
    pass
except (NameError, ZeroDivisionError):
    print("出现了NameError或ZeroDivisionError")