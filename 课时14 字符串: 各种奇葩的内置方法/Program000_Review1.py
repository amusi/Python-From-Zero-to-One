#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:35:54 2017

@author: amusi
"""

# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码只能由数字开头
#   3. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

str1 = input("please input passward: ")
if str1.isalnum() and len(str1) <= 8:
    print("低级密码")
elif str1.isalnum() and str1[0].isdigit() and len(str1) >= 8:
    print("中级密码")
elif str1.isalnum() and str1[0].isalpha() and len(str1) >= 16:
    print("高级密码")
else:
    print("Not sure!")