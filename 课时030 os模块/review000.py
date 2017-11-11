# Summary: 编写一个程序，统计当前目录下每个文件类型的文件数
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
    # 将文件名和后缀分开
    for each in files:
        # 常规方法
        # f_name, f_extension = each.split(".", 1)
        # 使用os.path.split函数
        f_name, f_extension = os.path.splitext(each)
        if f_extension not in extens:
            extens[f_extension] = 0
        extens[f_extension] = extens[f_extension] + 1
    # 输出结果
    for extens_name, nums in extens.items():
        #print("该文件夹下共有类型为[" + extens_name +"]的文件" + str(nums) + "个")
        print("该文件夹下共有类型为[%s]的文件 %d 个" % (extens_name, nums))

file_cur_dir = os.getcwd()
count_files(file_cur_dir)

