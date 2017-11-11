#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:18:58 2017

@author: amusi
"""

"""
有5个人坐在一起，问第5个人多少岁？他说比第4个大2岁。问第4个人岁数，他说比第3个人大2岁。
问第3个人，又说比第2个人大2岁。问第2个人，说比第一个人大2岁。最后问第一个人，他说是10岁。请问第5个人多少岁？
"""

def age(n):
    if n == 1:
        return 10
    else:
        
        return 2 + age(n-1)
    
print("第5个人 %d 岁" % age(5))