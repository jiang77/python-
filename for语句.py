'''
for语句
格式：
for 变量名 in 集合：
    语句
逻辑：按顺序取“集合”中的每个元素赋值给“变量”，再去执行语句，如此循环往复，
      直到取完“集合”中的元素截止
'''


for i in [1,2,3,4,5]:
    print(i)

'''
range([start,] end [, step])函数     被称为“列表生成器”
start默认是0，step默认是1
作用：生成数列（列表）

'''

a = range(10)
print(a)
for x in range(10):
    print(x)


for y in range(2,20,2):
    print(y)

# 同时遍历下标和元素
'''
for index，m in enumerate([1,2,3,4,5]):    # index, m = 下标，元素
    print(index, m)
'''
# enumerate能把下标和元素都拿出来，枚举遍历器。相当于拿出一个list，这个list前面是下标，后面是元素，分别给index和m赋值


# 使用for实现1加到100的和
sum = 0
for i in range(1,101):
    sum += i
print(sum)
