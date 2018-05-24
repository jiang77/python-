'''
while  语句：

while 表达式：
    语句

逻辑：当程序执行到while语句时，首先计算“表达式”的值，如果“表达式“的值为假，
      那么结束整个while语句。继续向下执行。如果“表达式”的值为真，则执行“语句”，
      执行完“语句”，再去计算“表达式”的值。如果“表达式“的值为假，那么结束整个while语句，
      继续向下执行。如果“表达式”的值还为真，则执行“语句” ，如此循环往复，知道“表达式”
      的值为假才停止。

'''

'''
num = 1
while num <= 5:
    print(num)
    num += 1
'''

'''
sum = 0
num = 1
while num <= 100:
    num += 1
    sum += num
print("sum = %d" % (sum))
'''

'''
str = "sunck is a handsome man"
index = 0
while index < len(str):
    print("str[%d] = %s" % (index, str[index]))
    index += 1
'''



# 练习
'''
打印出所有三位数中的水仙花数
告诉我五位数中有多少个回文数
从控制台输入一个数，判断是否是质数。（只能被1和自身整除的数是质数，最小的质数从2开始，1不是质数）
从控制台输入一个数，分解质因数
从控制台输入一个字符串，返回这个字符串中有多少个单词     "sf sfe fewfw erfe"   4
从控制台输入一个字符串，打印出这个字符串中所有数字字符的和    "jsdfgh kjashd 45djfh45" 18
'''


# 第一题：打印出所有三位数中的水仙花数
num = 100
while num <= 999:
    numList = list(map(int, str(num)))
    if num == sum([i**len(numList) for i in numList]):
    #if num == num[0]**3+num[1]**3+num[2]**3:
        print(num)
    num += 1

