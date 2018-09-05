path = r"C:\User\xlg\文件读写\file2.txt"
f = open(path, "w")


# 写文件
# 1.将信息写入缓冲区（内存的一片区域）
f.write("sunck is a good man")
# 2.刷新缓冲区（直接把内部缓冲区的数据立即写入文件，而不是被动的等待，自动刷新缓冲区写入）
f.flush()
#  注意，只写f.write("sunck is a good man")也可以将数据写入文件，但是不同的是在关闭文件的时候
#  刷新缓冲区，再把数据写进去
#  当缓存区满了和遇到“\n”时，也会自动刷新
while True:
    pass
f.close()


# 写文件的简写
with open(path, "a") as f2:
    f2.write("good man")

