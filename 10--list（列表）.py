# 存储五个人的年龄，求他们的平均年龄
age1 = 18
age2 = 19
age3 = 27
age4 = 36
age5 = 45
print((age1 + age2 + age3 + age4 + age5) / 5)

# 思考：要存储100个人的年龄
# 解决：使用列表
# 列表的本质：是一种有序的集合


# 创建列表
'''
格式：列表名 = [列表选项1，列表选项2，列表选项3，……，列表选项n ]

'''
# 创建一个空列表
list1 = []
print(list1)
# 创建一个带有元素的列表
list2 = [12, 34, 45, 45, 78]
'''
嵌套最好不要超过3层
index = 0
sum = 0
while index < 5:
    sum += list2[index]
    index += 1
    if index == 5:
        print("平均年龄 = %d" % (sum / 5))
        
'''
# 注意：列表中的元素数据可以是不同类型的
list3 = [1, 2, "sunck", "good", True]
print(list3)

# 列表元素的访问
# 取值    格式：列表名[下标]
# 注意不要越界：下标超出了可表示的范围：indexError
list4 = [1, 2, 3, 4, 5]
print(list4[2])

# 替换
list4[2] = 123
print(list4)
#list4[5] = 300
#print(list4)  # 会提示indexError

# 列表操作
# 列表组合
list5 = [1,2,3]
list6 = [4,5,6]
list7 = list5 + list6
print(list7)    # 注意：list5和list6的值不会变，只是生成了一个新的列表list7

# 列表的重复
list8 = [1,2,3]
print(list8 * 3)  # 结果：[1, 2, 3, 1, 2, 3, 1, 2, 3]

# 判断元素是否在列表中
list9 = [1,2,3,4,5]
print(3 in list9)  # 结果：True
print(6 in list9)  # 结果：False

# 列表截取
list10 = [1,2,3,4,5,6,7,8,9]
print(list10[2:6])
print(list10[3:])
print(list10[:5])

# 二维列表
list11 = [[1,2,3],[4,5,6],[7,8,9]]
print(list11[1][1])


# 列表方法

# 1.append方法：在列表中末尾添加新的元素
# 注意：不是简单地返回一个修改过的新列表，而是直接修改原来的列表
list12 = [1,2,3,4,5]
list12.append(6)
print(list12)
list12.append([7,8,9])
print(list12)

# 2.extend方法：在末尾一次性追加另一个列表中的多个值
# 注意：修改了被扩展的列表,即下方的list13
list13 = [1,2,3,4,5]
list13.extend([6,7,8])
print(list13)

# 3.insert方法：在下标出添加一个元素，不覆盖原数据，原数据向后顺延
list14 = [1,2,3,4,5]
list14.insert(1, 100)
print(list14)
list14.insert(1, [12,35])
print(list14)  # 结果：[1, [12, 35], 100, 2, 3, 4, 5]

# 4.pop方法：移除列表中指定下标处的元素，默认移除最后一个元素，并返回删除的数据
list15 = [1,2,3,4,5]
list15.pop()
print(list15) #[1, 2, 3, 4]
list15.pop(2)
print(list15) #[1, 2, 4]
print(list15.pop(1)) # 结果：2    返回了删除的数据
print(list15)

# 5.remove方法：移除列表中的某个元素第一个匹配的结果
list16 = [1,3,4,5,6,43,6]
list16.remove(4)  # 移除列表中的第一个4
print(list16)

# 6.clear方法：清除列表中所有的数据
list17 = [1,3,4,5,6,7]
list17.clear()
print(list17)

# 7.index方法：从列表中找出某个值的第一个匹配的索引值
list18 = [1,2,3,4,5]
index18 = list18.index(3)
index19 = list18.index(3, 1, 4) # 1和4是范围
print(index18, index19)

# 8.count方法：
list20 = [1,2,3,4,5,6,7,8]
print(len(list20))

# 9.max方法：获取列表中的最大值
list21 = [1,2,3,4,5,6]
print(max(list21))

# 10.min方法：获取列表中的最小值
list22 = [1,2,3,4,5,6]
print(min(list22))

# 11.count方法：查看元素在列表中出现的次数
list23 = [12,4,6,7,65,6,6,6,4,3,6]
print(list23.count(6))

# 删除所有的某一个元素
num24 = 0
all = list23.count(6)
while num24 < all:
    list23.remove(6)
    num24 += 1
print(list23)


# 12.reverse方法：倒序
list25 = [1,2,3,4,5]
list25.reverse()
print(list25)

# 13.sort方法：排序，升序
list26 = [2,1,3,5,4]
list26.sort()
print(list26)

# 拷贝：浅拷贝，一般叫引用拷贝，把地址拷贝了。
list27 = [1,2,3,4,5]
list28 = list27
list28[1] = 200
print(list28)      # [1, 200, 3, 4, 5]
print(list27)      # [1, 200, 3, 4, 5]
print(id(list28))
print(id(list27))  # list28和list27的id一样

'''
内存分为：堆区一个栈区。   
栈区：一般我们开辟的普通变量都存在栈区，在栈区开辟一个内存空间。栈区特点：程序结束,释放内存空间。
      空间是系统自动分配。。
堆区：特点是程序员手动开辟，手动释放。对象都是存在堆区。

'''

# 14.深拷贝：内存的拷贝   （内存、内存地址、变量）
list29 = [1,2,3,4,5]
list30 = list29.copy()
list30[1] = 200
print(list29)    # [1, 2, 3, 4, 5]
print(list30)    # [1, 200, 3, 4, 5]
print(id(list29))
print(id(list30))  # list29和list30的地址不一样，说明list29和list30不是一个变量

# 15.将元组转成列表
list31 = list((1,2,3,4,5))
print(list31)

# 练习：从控制台输入十个数，找出其中第二大的值。
listNum = []

num = 0
while num < 10:
    val = int(input())
    listNum.append(val)
    num += 1
print(listNum)


