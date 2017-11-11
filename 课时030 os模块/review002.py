# Summary: 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索
# Author:  Amusi
# Date:    2017-11-03
import os
def judge_exit(file_name, file_path):
    os.chdir(file_path)  # 改变工作目录
    flag_exit = 0        # 文件存在标志
    # 判断每层目录的同级文件
    for each_file in os.listdir(os.curdir):
        if each_file == file_name:
            flag_exit = 1
            print(os.getcwd() + os.sep + each_file) # 使用os.seq使程序更标准
        if os.path.isdir(each_file):
            judge_exit(file_name, each_file)    # 递归调用
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录

    if flag_exit == 0:
        print("很抱歉在[%s]下没有找到[%s]" % (file_path, file_name))

file_name = input("请输入您需要查询的文件名: ")
file_path = input("请输入您需要搜索的路径: ")
judge_exit(file_name, file_path)