# Summary: 用EasyGui简单实现一个可交互界面小程序
# Author:  Fangjie Chen
# Data:    2017-11-11

# 导入EasyGui模块
import easygui as eg
import sys

while True:
    eg.msgbox("Hi，欢迎进入第一个界面小程序^_^")

    msg = "请问你希望打开哪个功能选项呢？"
    title = "EasyGuo小程序"
    choices = ["Python入门", "Python进阶", "Python实战", "Python－AI"]

    # 获得选择的结果
    choice = eg.choicebox(msg, title, choices)

    # 弹出对话框，显示选择的结果
    eg.msgbox("你的选择是: "+ str(choice), "结果")

    msg = "你希望重新开始小程序么？"
    title = "请选择"

    # 显示一个继续、取消对话框
    if eg.ccbox(msg, title):
        pass         # 用户选择继续
    else:
        sys.exit(0)  # 用户选择取消