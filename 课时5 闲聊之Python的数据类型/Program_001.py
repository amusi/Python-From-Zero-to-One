#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:46:02 2017

@author: amusi
"""

#1. 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活运用）
# 注：这样定义闰年的:能被4整除但不能被100整除,或者能被400整除都是闰年。
numsStr = input("请输入一个年份（整数）： ")
while not numsStr.isdigit():
    numsStr = input("输入的类型错误，请再重新输入一个年份（整数）：")
nums = int(numsStr)
if ((nums % 2 == 0) and (nums % 100 !=0)) or (nums % 400 == 0):
    print("恭喜!该年份是闰年!")
else:
    print("抱歉!该年份不是闰年!")
