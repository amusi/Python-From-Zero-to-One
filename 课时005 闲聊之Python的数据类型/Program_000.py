#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:18:21 2017

@author: amusi
"""

# 条件分支
import random
secret = random.randint(1,10)
guessStr = input("请输入一个数值: ")
while not guessStr.isdigit():
    guessStr = input("输入类型不符，请重新输入数值: ")
guess= int(guessStr)
#counts = 0
while guess != secret:
    #if counts ==3: # 限制输入次数
    #    break
    #counts += 1
    guessStr = input("猜错啦，请重新输入一个数值: ")
    while not guessStr.isdigit():
        guessStr = input("输入类型不符，请重新输入数值: ")
    guess= int(guessStr)
    if guess == secret:
        print("好厉害，猜对咯!")
    else:
        if guess > secret:
            print("偏大了...")
        else:
            print("偏小了...")
print("游戏结束！")
