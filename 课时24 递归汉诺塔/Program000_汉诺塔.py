#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:29:57 2017

@author: amusi
"""

'''
汉诺塔：汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。
大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。
大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。
'''
def hanoi(n, x, y, z):
    if n == 1:
        print(x, " --> ", z)
    else:
        hanoi(n-1, x, z, y)    # 将前n-1个盘从移动到y上
        print(x, " -->", z)    # 将最底下的最后一个盘子从x移动到z上
        hanoi(n-1, y, x, z)    # 将y上的n-1盒子移动到z上

n = int(input("请输入hanoi层数: "))
hanoi(n, "x", "y", "z")


