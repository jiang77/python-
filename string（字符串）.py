# 什么是字符串
'''
字符串是一串单引号或是双引号括起来的任意文本(引号不是数据)
'abc'     "def"
字符串不可变(指的是右侧的值，而不是左侧的变量)
'''


# 创建字符串
'''
str1 = "sunck is a good man!"
str3 = "sunck is a nice man!"
str3 = "sunck is a handsome man!"

'''


# 字符串运算

'''
字符串连接
'''
'''
str6 = "sunck is a "
str7 = "good man"
str8 = str6 + str7
print("str6 =", str6)
print("str7 =", str7)
print("str8 =", str8)
'''



# 输出重复字符串
str9 = "good"
str10 = str9 * 3
print("str10 =", str10)


# 访问字符串里面的某一个字符
# 通过索引下标查找字符，索引从0开始
# 字符串名[下标]
str11 = "sunck is a good man!"
print(str11[1])
# 思考：下面两条语句是否能成功执行
# 不能成功执行，因为字符串是不可改变的！
'''
str11[1] = "a"
print("str11 =",str11)  
'''

# 截取字符串中的一部分
str13 = "sunck is a good man!"
# 从给定下标处开始截取到给定下标之前
str15 = str13[6:15]
# 从头截取到给定下标之前
str16 = str13[:5]
# 从给定下标处开始截取到结尾
str17 = str13[16:]
print("str15 =", str15)
print("str16 =", str16)
print("str17 =", str17)



# 成员运算符in和not in
str18 = "sunck is a good man!"
print("good" in str18)
print("good1" in str18)
print("good1" not in str18)




# 格式化输出
print("sunck is a good man")
num = 10
str19 = "sunck is a good man!"
f = 10.1234
print("num =", num, "str19 =", str19)
print("num = %d, str19 = %s, f = %f" %(num, str19, f))     # %d  %s  %f 叫占位符，只是占一个位置，没有特殊含义。
# f = %.3f  表示：精确到小数点后三位，会四舍五入。当没有的时候默认精确到小数点后六位，也会四舍五入。