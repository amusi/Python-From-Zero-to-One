# Summary: 猜数字小游戏，用户输入１~10之间的数字，若与随机生成的数值相等，则退出程序，反正一直循环
# Author:  Fangjie Chen
# Date:    2017-11-11

# 导入EasyGui模块
import easygui as eg
import random

# 初始化
eg.msgbox("欢迎进入猜数字小游戏")
secret = random.randint(1,10)
title = "猜数字小游戏"
msg = "不妨猜一下数字（1~10）:"
guess = eg.integerbox(msg, title, lowerbound=1, upperbound=10)

while True:
    if guess == secret:
        eg.msgbox("好厉害猜对了！")
        break
    else:
        if guess > secret:
            eg.msgbox("您输入的数值[偏大]")
        else:
            eg.msgbox("您输入的数值[偏小]")
        guess = eg.integerbox(msg, title, lowerbound=1, upperbound=10)

print("游戏结束！")