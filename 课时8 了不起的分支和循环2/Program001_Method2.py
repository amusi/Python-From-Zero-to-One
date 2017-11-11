#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 22:01:45 2017

@author: amusi
"""

score = int(input("Please input a score: "))
if 100 >= score >= 90:
    print("A")
else:
    if 90 > score >= 80:
        print("B")
    else:
        if 80 > score >= 60:
            print("C")
        else:
            if 60 > score >= 0:
                print("D")
            else:
                if score > 100 or score < 0:
                    print("Error input")
