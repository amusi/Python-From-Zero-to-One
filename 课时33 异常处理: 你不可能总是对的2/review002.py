# Summary: 把文件关闭放在finally语句块中执行还是会出现问题，像下边这个源代码，当前文件夹中并不存在”My_File.txt”这个文件，那么程序执行起来会发生什么事情呢？你有办法解决这个问题么？
# Author:  Fangjie Chen
# Date:    2017-11-11

# -*- coding:utf-8 -*-

# 源代码

try:
    f = open("My_File.txt") # 当前文件夹下并不存在"My_File.txt"文件
    print(f.read())
except OSError as reason:
    print("出错啦: " + str(reason))
finally:
    if f in locals():   # 如果文件对象变量存在当前局部变量符号表的话，说明文件打开成功
        f.close()
