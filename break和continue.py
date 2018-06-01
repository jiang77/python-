'''
break语句
作用：跳出for和while的循环。
注意：只能跳出距离它最近的那一层循环
'''


'''
for i in range(10):
    print(i)
    if i == 5:
        break
'''

'''
num = 1
while num <= 10:
    print(num)
    num += 1
    if num == 3:
        break
# 注意：循环语句可以有else语句，break导致循环截止，不会执行else下面的语句
else:
    print("sunck is a good man")
'''



'''
continue语句
作用：跳过当前循环中的剩余语句，然后继续下一次循环
注意：只跳过距离最近的循环
'''


'''
for i in range(10):
    print(i)
    if i == 3:
        i += 1
        continue
    print("*")
    print("&")
'''

'''
num = 0
while num < 10:
    print(num)
    if num == 3:
        num += 1
        continue
    print("*")
    print("&")
'''



# 练习一：打印99乘法表
# 练习二：输入两个数，求这两个数的最大公约数
# 练习三：输入一个字符串，将字符串中的大写字母转小写，小写字母转大写
# 练习四：随机生成一个6位数的验证（验证码包括大小写字母和数字）

