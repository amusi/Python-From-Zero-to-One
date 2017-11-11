#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:06:05 2017

@author: amusi
"""

#三色球问题
#有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。
#先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。
print("red\tyellow\tblur")
for red in range(1,4):
    for yellow in range(1, 4):
        for green in range(1, 7):
            if 8 == red + yellow + green:
                print(red,"\t",yellow,"\t",green)
    