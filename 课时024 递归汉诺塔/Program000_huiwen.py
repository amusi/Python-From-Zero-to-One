#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:10:52 2017

@author: amusi
"""

# 使用递归的方式求解“回文字符串”
def is_palindrome(n, start, end):
    if start > end:
        return 1
    else:
		#return is_palindrome(n, start+1, end-1)  if n[start] == n[end] else 0
        if n[start] == n[end]:
            return is_palindrome(n, start+1, end-1)
        else:
            return 0
        
string = input("请输入一串字符串: ")
length = len(string)-1
if is_palindrome(string, 0, length):
	print("%s 是回文字符串！" % string)
else:
	print("%s 不是回文字符串！" % string)