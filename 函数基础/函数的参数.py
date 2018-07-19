# 需求：编写一个函数，给函数一个字符串和一个年龄，在函数内部打印出来

# 形参（形式参数）：定义函数时，小括号中的变量，本质是变量
# 参数必须按顺序传递，个数目前要对应
'''
def myPrint(str,age,hoby):
    print(str,age)
myPrint("sunck",18)   结果会报错，实参和形参个数不对应

'''

def myPrint(str,age):
    print(str,age)

# 实参（实际参数）：调用函数时给函数传递的数据，本质是值
myPrint("sunck",18)