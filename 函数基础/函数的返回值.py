# 需求：编写函数，实现功能，给函数两个数，返回这两个数的和

def mySum(num1,num2):
    sum = num1 + num2
    # 将结果返回给了函数的调用者
    return sum
    # 执行完return语句，该函数就结束了，return后面的代码不执行
    print("#######")   #所以该条语句时不执行的
res = mySum(23,5)
print(res)