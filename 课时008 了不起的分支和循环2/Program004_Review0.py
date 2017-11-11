#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 23:04:14 2017

@author: amusi
"""

score = int(input("Please input a score: "))
if 80 > score >= 60:
    print("C")
elif 100 >= score >= 90:
    print("A")
elif 90 > score >= 80:
    print("B")
elif 60 > score >= 0:
    print("D")
else:
    print("Error input")