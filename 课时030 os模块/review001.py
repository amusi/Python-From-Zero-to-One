# Summary: 编写一个程序，计算当前文件夹下所有文件的大小
# Author:  Amusi
# Date:    2017-11-03
import os
def count_files(file_cur_dir):
    files = []
    extens = {}
    for root, dirs, files in os.walk(file_cur_dir):
        print(root)    # 当前目录
        print(dirs)    # 当前路径下的所有子目录
        print(files)   # 当前路径下所有非目录子文件
    #
    for each_file in files:
        f_size = os.path.getsize(each_file)
        print("%s [%dBytes]" % (each_file, f_size))

file_cur_dir = os.getcwd()
count_files(file_cur_dir)