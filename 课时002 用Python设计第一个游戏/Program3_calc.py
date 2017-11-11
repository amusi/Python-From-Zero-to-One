#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

numsStr = input("请您输入0~100之间的数字: ")
nums = int(numsStr)
if 0 <= nums <= 100:
    print("厉害了, Word哥")
else:
    print("你走吧~")