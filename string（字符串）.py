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


# 转义字符 \       将一些字符转换成有特殊含义的字符


# \n
print("num = %d\nstr19 = %s\nf = %f" %(num, str19, f))

# \\
print("sunck \\n is")

# \'   \"
print('tom is a \'good \'man')  # tom is a 'good' man
print("tom is a \"good \"man")  # tom is a "good" man

# 如果字符串内有很多换行，用\n写在一行不好阅读
print("good\nnice\nhandsome")
print('''
good
nice
handsome
''')

# \t  制表符
print("sunck\tgood")      # sunck   good       中间有四个空格（tab）

# 如果字符串中有很多字符都需要转义，就需要加入好多的\，为了简化，python允许用r表示内部的字符串默认不转义。r有时候会用到windows路径中。
'''
D:\Python27\Lib\json
'''
print(r"D:\Python27\Lib\json")
# 就想打印一个这个： \\\t\\
print(r"\\\t\\")



# 字符串方法

#1  eval(str)      功能：将字符串str当成有效的表达式来求值并返回计算结果。
num1 = eval("123")
print(num1)
print(eval("+123"))
print(eval("-123"))
print(eval("12+3"))
print(eval("12-3"))

#2 len(str)      功能：返回字符串长度（长度是字符个数而不是字节数）
print(len("sunck is a good man"))

#3 lower()      功能：转换字符串中大写字母为小写字母
str20 = "SUNCK is a Good Man"
print(str20.lower())
print("str20 = %s" % (str20))     # 注意：其实是新生成了一个字符串，并没有改变str20，字符串不可变

#4 upper()      功能：转换字符串中的小写字母为大写字母
str21 = "SUNCK is a Good Man"
print(str21.upper())
print("SUNCK is a Good Man".upper())

#5 swapcase()     功能：转换字符串中小写字母变为大写字母，大写字母变为小写字母
str22 = "SUNCK is a gOOd mAn"
print(str22.swapcase())

#6 capitalize()     功能：字符串首字母大写，其他小写
str23 = "SUNCK is a gOOd mAn"
print(str23.capitalize())

#7 title()       功能：每个单词的首字母大写
str24 = "SUNCK is a gOOd mAn"
print(str24.title())

#8 center(width,fillchar)    功能：返回一个指定宽度的居中字符串，fillchar为填充的字符，默认是空格填充
str25 = "kaige is a nice man"
print(str25.center(40,"*"))

#9 ljust(width[, fillchar])   功能：返回一个指定宽度的左对齐字符串，fillchar为填充的字符，默认是空格填充。
str26 = "kaige is a nice man"
print(str26.ljust(40,"*"))

#10 rjust(width[, fillchar])   功能：返回一个指定宽度的右对齐字符串，fillchar为填充的字符，默认是空格填充。
str27 = "kaige is a nice man"
print(str27.rjust(40,"*"))

#11 zfill(width)    功能：返回一个长度为width的字符串，原字符串右对齐，前面补0
str28 = "kaige is a nice man"
print(str28.zfill(40))

#12 count(str[, start][, end])  功能：返回字符串中str出现的次数。可以指定一个范围，默认从头到尾
str29 = "kaige is a nice nice man"
print(str29.count("nice", 15, len(str29)))

#13 find(str[,start][,end])    功能：从左向右检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾，得到的是第一次出现的开始下标,没有返回-1
str30 = "kaige is a nice  nice man"
print(str30.find("nice"))
print(str30.find("good"))
print(str30.find("nice", 15, len(str30)))

#14 rfind(str[,start][,end])    功能：从右向左检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾，得到的是第一次出现的开始下标,没有返回-1
str31 = "kaige is a nice  nice man"
print(str31.rfind("nice"))
print(str31.rfind("good"))
print(str31.rfind("nice", 15, len(str31)))

#15 index(str[, start=0][, end=len(str)])    功能：默认从左向右检测str字符串。跟find（）一样，只不过如果str不存在的时候回报一个异常
str32 = "kaige is a nice  nice man"
print(str32.index("nice"))
#print(str32.index("good"))

#16 rindex(str[, start=0][, end=len(str)])    功能：默认从右向左检测str字符串。跟find（）一样，只不过如果str不存在的时候回报一个异常
str33 = "kaige is a nice  nice man"
print(str33.index("nice"))
#print(str33.index("good"))

#17 lstrip()     功能：截掉字符串左侧指定的字符。默认为空格
str34 = "*********kaige is a nice  nice man"
print(str34.lstrip("*"))

#18 rstrip()     功能：截掉字符串右侧指定的字符。默认为空格
str35 = "*********kaige is a nice  nice man ****"
print(str35.rstrip("*"))

#19 strip()    功能：截掉字符串两侧指定的字符。默认为空格
str36 = "*********kaige is a nice  nice man ****"
print(str36.strip("*"))

# 字符串也可以比较大小
'''
print("a" == "a")   # 结果为true

'''

#20 split(str=""[,num])   功能：以str为分隔符截取字符串，将截出来的放入列表
# 指定num，则仅截取num个字符串
str38 = "sunck**is***a**good*man"
print(str38.split("*"))  # 结果：['sunck', '', 'is', '', '', 'a', '', 'good', 'man']
print(str38.split("*",3))  # 结果：['sunck', '', 'is', '**a**good*man']
# 练习：输出单词个数
list39 = str38.split("*")
c = 0
for s in list39:
    if len(s) > 0:   #单词的长度肯定大于0
        c += 1
print(c)

#21 splitlines([keepends])   按照（'\r', '\r\n', '\n'）分隔
# keepends == True  会保留换行符。keepends默认为False
str40 = '''sunck is a good man!
sunck is a nice man!
sunck is a handsome man!
'''
print(str40.splitlines())  # 结果：['sunck is a good man!', 'sunck is a nice man!', 'sunck is a handsome man!']
print(str40.splitlines(True))  # 结果：['sunck is a good man!\n', 'sunck is a nice man!\n', 'sunck is a handsome man!\n']

# 将list组合成字符串
#22 join()  以指定的字符串分隔符，将seq中的所有元素组合成一个字符串
list41 = ['sunck', 'is', 'a', 'good', 'man']
str42 = " ".join(list41)   # 字符串之间用空格分隔，可以有任意多的分隔符（#@%￥等都可以）
print(str42)

#23 max()  min()
str43 = "sunck is a good man!z"
print(max(str43))
print(min(str43))  # 结果是个空格

#24  replace(oldstr, newstr, count)
#用newstr替换oldstr，默认是全部替换。如果指定了count，那么只替换前count个
str44 = "sunck is a good  good good man"
str45 = str44.replace("good","nice", 1)
print(str44)
print(str45)

# 创建一个字符串映射表
t46 =str. maketrans("good", "nice")  #将"good" 映射成 "nice"
# 注意：这种映射是将g--n  o--i  o--c  d--e
str47 = "sunck is a good good good man"
str48 = str47.translate(t46)
print(str48)  #结果:sunck is a ncce ncce ncce man

str49 = "sunck is a good man"
print(str49.startswith())