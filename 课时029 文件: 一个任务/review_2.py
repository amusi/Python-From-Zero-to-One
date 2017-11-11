# Summary: 编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置
# Author:  Amusi
# Date:    2017-11-02
def compare_file(file_name1, file_name2):
        f1 = open(file_name1)  # 按相对路径打开文件
        f2 = open(file_name2)  # 按相对路径打开文件
        count = 0       # 计算不一样的数量
        differ = []     # 统计不一样的行数
        for line1 in f1:
                line2 = f2.readline()
                count += 1
                if line1 != line2:
                        differ.append(count)
        f1.close()
        f2.close()

        if len(differ) == 0:
                print("两个文件完全一样")
        else:
                print("两个文件共有[%d]处不同:" % len(differ))
                for each in differ:
                        print("第 %d 行不一样" % each)

file_name1 = input("请输入需要比较的第一个文件名: ")
file_name2 = input("请输入需要比较的第二个文件名: ")


compare_file(file_name1, file_name2)
