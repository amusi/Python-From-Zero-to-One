#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 21:15:09 2017

@author: amusi
"""

# 爱因斯坦曾出过这样一道有趣的数学题：
# 有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；
# 若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩
# 题目：请编程求解该阶梯至少有多少阶？
for nums in range(0, 100000):
    if (nums % 2 == 1) and (nums % 3 == 2) and (nums % 5 == 4) \
    and (nums % 6 == 5) and( nums % 7 == 0):
        print(nums)
        break
