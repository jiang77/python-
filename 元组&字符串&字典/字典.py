'''
概述：使用键-值（key-value）存储，具有极快的查找速度
注意：字典是无序的
key的特性：
1.字典中的key必须唯一
2.key必须是不可变对象
3.字符串、整数等都是不可变的，可以作为key
4.list是可变的，不能作为key

思考：保存呢多为学生的姓名和成绩
使用字典，学生姓名作为key，成绩作为值

'''

dict1 = {"tom":60,"lilei":70}

# 元素的访问
# 获取：字典名[key]
print(dict1["lilei"])
# print(dict1["sunck"])   如果没有对应的key值时会报错
print(dict1.get("sunck"))  # 这样不会报错，会返回None
ret = dict1.get("sunck")
if ret == None:
    print("没有")
else:
    print("有")

# 添加
dict1["hanmeimei"] = 90

# 因为一个key对应一个value，所以，多次对一个key的value赋值，其实就是修改值
dict1["lilei"] = 80
print(dict1)

# 删除
dict1.pop("tom")
print(dict1)


# 遍历
# 遍历出key
for key in dict1:
    print(key,dict1[key])

# 遍历出value
# print(dict1.values())    结果是：dict_values([80, 90])，一个列表
for value in dict1.values():
    print(value)

# 遍历出key和value
# print(dict1.items())   结果是：dict_items([('lilei', 80), ('hanmeimei', 90)])，是一个列表，
# 但是列表的每个元素是个元组
for k,v in dict1.items():
    print(k,v)


for i,v2 in enumerate(dict1):
    print(i,v2)
'''
结果：0 lilei
      1 hanmeimei
字典是无序的，这个排序是指我们往里存的顺序
'''

# 和list比较
# 1.查找和插入的速度极快，不会随着key-value的增加而变慢
# 2.需要占用大量的内存，内存浪费多。多存了key

# list
# 1.查找和插入的速度会随着数据量的增多而减慢
# 2.占用空间小，浪费的内存少



