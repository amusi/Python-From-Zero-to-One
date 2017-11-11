#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 22:01:56 2017

@author: amusi
"""

score = int(input("Please input a score: "))
if 100 >= score >= 90:
    print("A")
elif 90 > score >= 80:
    print("B")
elif 80 > score >= 60:
    print("C")
elif 60 > score >= 0:
    print("D")
else:
    print("Error input")