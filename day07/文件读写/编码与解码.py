# 编码
path = r"C:\User\xlg\文件读写\file3.txt"
with open(path, "wb", encoding="utf-8") as f1:
    str = "sunck is a good man"
    f1.write(str.encode("utf-8"))  # 将二进制编码写入文件


# 解码
with open(path, "rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8")  # 将读取出来的二进制数据解码
    print(newData)
    print(type(newData))