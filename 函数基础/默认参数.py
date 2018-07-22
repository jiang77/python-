'''
概念：调用函数时，如果没有传递参数，则使用默认参数




'''
# 以后要用默认参数最好在定义函数时将默认参数放到最后（例如str是默认参数，age不是默认参数，在调用时，只写一个18，
# 则函数会默认将18赋值给str）
def myPrint(str = "sunck is a good man",age = 18):
    print(str,age)
myPrint()