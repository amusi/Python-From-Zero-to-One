#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 22:15:33 2017

@author: amusi
"""
# version
x,y = 100, 99
if x < y:
    small = x
else:
    small = y
print("The smaller value: %d" % small)

# version2
small = x if x < y else y # 三元运算符
print("The smaller value: %d" % small)