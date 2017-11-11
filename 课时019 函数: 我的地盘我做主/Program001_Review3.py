#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:11:09 2017

@author: amusi
"""
# 编写一个函数，判断传入的字符串参数是否为“回文联”
# （回文联即用回文形式写的对联，即可顺读，也可倒读，例如：上海自来水来自海上）

def palindrome(string):
    length = len(string)
    string2 = string
    flag = 1
    for i in range(length // 2):
        if string[i] != string2[length -(i+1)]:
            flag = 0
            break
    if flag == 1:
        print("输入的字符串是回文联！")
    else:
        print("输入的字符串不是回文联！")
palindrome("上海自来水来自海上")
palindrome("我爱你因为你爱我")
