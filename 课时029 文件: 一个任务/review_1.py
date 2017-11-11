# Summary: 编写一个程序，接受用户的输入并保存为新的文件：
# Author:  Amusi
# Date:    2017-11-02
def create_file(fileName):
        f = open(fileName, "w")  # 按相对路径打开文件
        print("请输入内容[单独输入\":w\"保存退出]:\n")
        while True:
                writeLine = input()
                if writeLine != "w:":
                        f.write("%s\n" % writeLine)
                else:
                        break
        f.close()

fileName = input("请输入文件名: ")
create_file(fileName)
