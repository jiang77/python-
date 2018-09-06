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

# 获取文件属性
print(os.stat("sunck"))

# 重命名(第一个旧名，第二个是新名)
os.rename("sunck", "kaige")

# 删除普通文件
os.remove("file1.txt")

# 运行shell命令
os.system()
os.system("notepad")                         # 打开notepad（一个记事本软件）
os.system("write")                           #  打开写字板
os.system("mspaint")                         #  打开画板
os.system("msconfig")                        #  打开系统设置
os.system("shutdown -s -t 500")              # 多少时间后自动关机
os.system("shutdown -a")                     #  取消自动关机
os.system("taskkill /f /im notepad.exe")     # 关闭notepad（一个记事本软件）






# 有些方法存在os模块里，还有些存在于os.path
# 查看当前的绝对路径
print(os.path.abspath("./kaige"))

# 拼接路径
p1 = r"C:\User\xlg\文件读写\day08"
p2 = r"sunck\abc\d"
# 注意：参数2里开始不要有斜杠（即p2）
# r"C:\User\xlg\文件读写\day08\sunck"
print(os.path.join(p1, p2))

# 拆分路径
path2 = r"C:\User\xlg\文件读写\day08""
print(os.path.split(path2))   # 拆分成一个元组。只拆最后的。day08是一个，day08前面的是一个

# 获取扩展名，没有扩展名就为空。（扩展名例如.txt、.py等）
print(os.path.splittext(path2))

# 判断是否是目录
print(os.path.isdir(path2))

# 判断文件是否存在(返回的是true/false)
path3 = r"C:\User\xlg\文件读写\day08\函数也是一种数据类型.py"
print(os.path.isfile(path3))

# 判断目录是否存在
path4 = r"C:\User\xlg\文件读写\day081"
print(os.path.exists(path4))

# 获得文件大小(字节数)
print(os.path.getsize(path3))

# 获得文件的目录(不包含文件名)
print(os.path.dirname(path3))  # C:\User\xlg\文件读写\day08

# 获得文件名
print(os.path.basename(path))  # 函数也是一种数据类型.py