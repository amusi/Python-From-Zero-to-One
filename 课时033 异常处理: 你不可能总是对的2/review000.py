# Summary: 尝试一个新的函数int_input()，当用户输入整数的时候正常返回，否则提示出错并要求重新输入。
# Author:  Fangjie Chen
# Date:    2017-11-11

def int_input(input_str=""):
    while True:
        try:
            int(input(input_str))
            break
        except ValueError:
            print("类型出错，请重新输入!")

int_input("请输入整数: ")