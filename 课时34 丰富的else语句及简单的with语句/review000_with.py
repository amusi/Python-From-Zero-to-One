# Summary:  使用with语句改写源代码，让Python去关心文件的打开和关闭吧
# Author:   Fangjie Chen
# Date:     2017-11-11

# 源代码
# def file_compare(file1, file2):
#     f1 = open(file1)
#     f2 = open(file2)
#     count = 0 #　统计行数
#     differ = [] # 统计不一样的数量
#
#     for line1 in f1:
#         line2 = f2.readline()
#         count += 1
#         if line1 != line2:
#             differ.append(count)
#     f1.close()
#     f2.close()
#     return differ
#
# file1 = input("请输入需要比较的头一个文件名: ")
# file2 = input("请输入需要比较的另一个文件名: ")
#
# differ = file_compare(file1, file2)
#
# if len(differ) == 0:
#     print("两个文件完全一样!")
# else:
#     print("两个文件共有[%d]处不同" % len(differ))
#     for each in differ:
#         print("第 %d 行不一样" % each)

# 修改版
def file_compare(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        count = 0 #　统计行数
        differ = [] # 统计不一样的数量

        for line1 in f1:
            line2 = f2.readline()
            count += 1
            if line1 != line2:
                differ.append(count)
    return differ

file1 = input("请输入需要比较的头一个文件名: ")
file2 = input("请输入需要比较的另一个文件名: ")

differ = file_compare(file1, file2)

if len(differ) == 0:
    print("两个文件完全一样!")
else:
    print("两个文件共有[%d]处不同" % len(differ))
    for each in differ:
        print("第 %d 行不一样" % each)