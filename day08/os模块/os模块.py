'''
OS：包含了普遍的操作系统的功能

'''
import os
# 获取操作系统类型   nt--windows   posix--linux\unix或Mac OS
print(os.name)

# 打印操作系统详细的信息（windows系统不支持）
#print(os.uname())

# 获取操作系统的环境变量
print(os.environ)

#获取指定环境变量
print(os.environ.get("ALLUSERSPROFILE"))

# 修改环境变量（自己查找）

# 获取当前目录
print(os.curdir)

# 获取当前工作目录及当前python脚本所在的目录
print(os.getcwd())

# 以列表的形式返回指定目录下的所有的文件（包括目录）
print(os.listdir(r"C:\User\xlg\文件读写\file2.txt"))

# 在当前目录下创建新目录（可以是相对路径也可以是绝对路径）
os.mkdir("sunck")
os.mkdir(r"C:\User\xlg\文件读写\file6.txt")
# 删除当前目录（可以是相对路径也可以是绝对路径）
os.rmdir("sunck")
os.rmdir(r"C:\User\xlg\文件读写\file6.txt")