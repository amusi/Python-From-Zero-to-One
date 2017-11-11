#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:32:02 2017

@author: amusi
"""

numStr = input("请输入需要查询的数值： ")
num = int(numStr)
if (num % 2) == 0:
    print("Even")
else:
    print("Odd")