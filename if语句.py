'''
if语句
格式：
if 表达式：
    语句

逻辑：当程序执行到if语句时，首先计算“表达式”的值，如果“表达式”的值为真，那么就执行if下的“语句。
如果”表达式“的值为假，则跳过整个if语句继续向下执行


何为真假？
假：0   0.0   ''    None    False
真：除了假就是真

'''

'''
num1 = 20
num2 = 20

if num1 == num2:
    num1 = 100

print("num1 =",num1)

'''

# 从控制台输入一个整数，判断是否是偶数

'''
num = int(input("请输入一个整数："))
if num % 2 == 0:
    print("这是一个偶数")
'''



'''
if-else语句
格式：
if 表达式：
    语句1
else：
    语句2
    
逻辑：当程序执行到if-else语句时，首先计算“表达式”的值，如果“表达式”的值为真，则则执行“语句1”。
执行完“语句1”跳出整个if-else语句。如果“表达式”的值为假，则执行“语句2”。执行完“语句2”跳出整个
if-else


'''

'''
num = int(input("请输入一个整数："))
if num % 2 == 0:
    print("这是一个偶数")
else:
    print("这是一个奇数")
'''



#练习
'''
第一题：从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
        153 = 1^3 + 5^3 + 3^3
第二题：从控制台输入一个五位数，如果是回文数，就打印“是回文数”，否则打印“不是回文数”
        11111      12321     12221          个位和万位一样，十位和千位一样。
第三题：从控制台输入两个数，输出较大的值

第四题：从控制台输入三个数，输出较大的值

'''

# 第一题
'''
自己写的

num = int(input(请输入一个三位数))
if num = num[0]^（num[2]） + num[1]^（num[2]） + num[2]^（num[2]）:
    print("这是是水仙花数")
else:
    print("不是水仙花数")

'''

'''
num = int(input("请输入一个三位数"))
a = num % 10   #（表示个位）
b = num // 10 % 10   #（表示十位：先对10取整，再取余）
c = num // 100   #（表示百位）
if num == c**3 + b**3 + a**3:
    print("是水仙花数")
else:
    print("不是水仙花数")
'''


# 第二题
'''
num = int(input("请输入一个五位数"))
a = num % 10   # 个位
b = num // 10 % 10 # 十位
c = num // 1000 % 10 # 千位
d = num // 10000 # 万位

if a == d:
    if b == c:
        print("是回文数")
else:
    print("不是回文数")
'''

# 第三题
'''
num1 = int(input("请输入一个数："))
num2 = int(input("请再输入一个数："))
if num1 > num2:
    print(num1)
else:
    print(num2)
'''

# 第四题
'''num1,num2,num3 = map(int,input("请输入3个数，用空格分隔\n").split())
# num1 = int(input("请输入一个数："))
# num2 = int(input("请再输入一个数："))
# num3 = int(input("请再次输入一个数："))
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)'''


num1,num2,num3 = map(int,input("请输入3个数，用逗号分隔\n").split(","))
max = num1
if num2 > num1:
    max = num2
if num3 > max:
    max = num3
print("max =", max)