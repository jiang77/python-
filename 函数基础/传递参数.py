'''
值传递：传递的不可变类型
string、tuple、number是不可变的
'''
def func1(num):
    num = 10
temp = 20
func1(temp)    # num = temp，将temp的值给num，此时num值等于20，其实可以将num和temp看做两个变量，
               # 仅仅只改了num这个变量，没有改temp这个变量。所以执行完函数之后，temp打印出来的
               # 值不变
print(temp)  # 结果：20


'''
引用传递：传递的可变类型
list、dict、set是可变的

'''

def func2(list):
    list[0] = 100
li = [1,2,3,4,5]
func2(li)
print(li)   # 结果：[100, 2, 3, 4, 5]