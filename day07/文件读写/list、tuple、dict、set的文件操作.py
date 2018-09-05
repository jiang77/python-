import pickle     # 数据持久性模块

myList = [1,2,3,4,5,"sunck is a good man"]
# 将myList写到一个文件里去(写入)
path = r"C:\User\xlg\文件读写\file4.txt"
f = open(path, "wb")

pickle.dump(myList, f)
f.close()


#将写进去的myList打开（读取）
f1 = open(path, "rb")
tempList = pickle.load(f1)
print(tempList)
f1.close()
