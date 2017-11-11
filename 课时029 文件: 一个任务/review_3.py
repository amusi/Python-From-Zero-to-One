# Summary: 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上
# Author:  Amusi
# Date:    2017-11-02
def print_file_lines(file_name1, N):
    if N <= 0:
        print("请输入大于1的行数!")
        return
    f = open(file_name1)  # 按相对路径打开文件
    count = 0  # 计算不一样的数量
    differ = []  # 统计不一样的行数
    for line in f:
        count += 1
        if count <= N:
            print(line)
    f.close()


file_name = input("请输入文件名: ")
N = int(input("请输入需要打印的行数: "))

print_file_lines(file_name, N)
