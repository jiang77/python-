'''
元组
定义：元组与列表一样，也是一种序列。唯一的不同是元组不能修改。本质是一种有序集合。
创建元组的语法很简单：如果你用逗号分隔了一些值，那么你就自动创建了元组。
特点：1.与列表非常相似   2.一旦初始化就不能修改   3.使用小括号
创建tuple格式：  元组名 = （元组元素1， 元组元素2， 元组元素3， ……， 元组元素n）

'''

# 创建空的元组:可以用没有包含内容的两个圆括号来表示
tuple1 = ()
print(tuple1)

# 创建带有元素的元组
tuple2 = (1,2,3,4,5)
print(tuple2)

# 元组中的元素的类型可以不同
tuple3 = (1,2,3,"good",True)
print(tuple3)

# 定义只有一个元素的元组
tuple4 = (1,)
print(tuple4)
print(type(tuple4))


# 元组元素的访问
# 格式：元组名[下标]
# 下标从0开始
# 取值
tuple5 = (1,2,3,4,5)
print(tuple5[0])
print(tuple5[1])
print(tuple5[2])
print(tuple5[3])
print(tuple5[4])
# print(tuple5[5])  # 下标超过范围（越界），会报错
# 获取最后一个元素
print(tuple5[-1])
print(tuple5[-2])
print(tuple5[-5])
# print(tuple5[-6])   # 下标超过范围（越界），会报错


# 修改元组        会报错，因为元组不能变
tuple6 = (1,2,3,4,5)
# tuple6[0] = 100
# print(tuple6)   # 结果报错：TypeError: 'tuple' object does not support item assignment

# 是思考：元组真的不能变？
tuple7 = (1,2,3,4,[5,6,7])
tuple7[-1][0] = 500
print(tuple7)      # 结果：(1, 2, 3, 4, [500, 6, 7])  改变的是list
# tuple7[-1] = [7,8,9]
# print(tuple7)    # 结果报错：TypeError: 'tuple' object does not support item assignment
# 注意：元组不能变说的是元组中的元素不能变。如果里面的元素是可变的，那么该元素就可变。


# 删除元组
tuple8 = (1,2,3,4,5)
del tuple8
# print(tuple8)    # 结果报错：NameError: name 'tuple8' is not defined



# 元组的操作
t7 = (1,2,3)
t8 = (4,5,6)
print(t7 + t8)     # 结果：(1, 2, 3, 4, 5, 6)，生成了一个新的元组

# 元组重复
t10 = (1,2,3)
print(t10 * 3)     # 结果：(1, 2, 3, 1, 2, 3, 1, 2, 3)

# 判断元素是否在元组中
t11 = (1,2,3)
print(4 in t11)

# 元组的截取
# 格式：元组名[开始下标:结束下标]       从开始下标开始截取，截取到结束下标之前
t12 = (1,2,3,4,5,6,7,8,9)
print(t12[3:7])
print(t12[3:])
print(t12[:7])


# 二维元组:元素为一维元组的元组
t13 = ((1,2,3),(4,5,6),(7,8,9))
print(t13[1][1])   # 结果：5


#元组的方法
t14 = (1,2,3,4,5)

#1 len()   返回元组中元素的个数
print(len(t14))

#2 max()   返回元组中的最大值
#3 min()   返回元组中的最小值
print(max((1,2,3,4,5,6)))
print(min((1,2,3,4,5,6)))


#4 将列表转成元组
list = [1,2,3]
t15 = tuple(list)
print(t15)

# 元组的遍历
for i in (1,2,3,4,5):
    print(i)