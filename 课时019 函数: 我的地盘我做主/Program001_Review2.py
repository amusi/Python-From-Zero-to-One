#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:02:57 2017

@author: amusi
"""

var = " Hi "

def fun1():
    global var
    var = " Baby "
    return fun2(var)

def fun2(var):
    var += "I love you"
    fun3(var)
    return var

def fun3(var):
    var = " Amusi "
    
print(fun1())