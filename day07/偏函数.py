# 举例引入：
print(int("1010", base = 2))   # 将字符串按base进制转换，即字符串是个base进制的。将字符串当做一个二进制来计算，
                               # 结果还是一个十进制
                               # base如果不传，则默认为10

# 自己定义偏函数
# 都按base=2来传
def int2(str,base = 2):
    return int(str, base)
print(int2("1011"))



# 引入一个functolls模块，帮助我们生成一个偏函数，不用像上面自己去定义。
# 把一个参数固定住，形成一个新的函数
# functools.partial会返回一个函数，返回的函数用int3去保存。
# 把int函数中的base参数固定住
import functools
int3 = functools.partial(int, base = 2)
print(int3("111"))