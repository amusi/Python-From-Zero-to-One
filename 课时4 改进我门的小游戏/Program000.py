#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:32:30 2017

@author: amusi
"""
# 条件分支
import random
secret = random.randint(1,10)
guessStr = input("请输入一个数值: ")
guess= int(guessStr)
#counts = 0
while guess != secret:
    #if counts ==3: # 限制输入次数
    #    break
    #counts += 1
    guessStr = input("猜错啦，请重新输入一个数值: ")
    guess= int(guessStr)
    if guess == secret:
        print("好厉害，猜对咯!")
    else:
        if guess > secret:
            print("偏大了...")
        else:
            print("偏小了...")
print("游戏结束！")