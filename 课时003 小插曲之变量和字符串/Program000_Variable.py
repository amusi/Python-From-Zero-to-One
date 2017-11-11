#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 23:51:15 2017

@author: amusi
"""
# string variable
teacher = "Amusi"
print(teacher)
teacher = "Lucy"
print(teacher)
# int variable
first = 3
second = 8
third = first + second
print(third)
#
myteacher = "Amusi"
yourteacher = "Lucy"
ourteacher  = myteacher + yourteacher
print(ourteacher)
# 长字符串
longStr = """Amusi love Lucy，
as same as Lucy love Amusi,
Forever love..."""
print(longStr)

year_days = 365
day_hours = 24
hour_mins = 60
min_second = 60
year_seconds = year_days * day_hours * hour_mins * min_second
print("一年有 %d 秒"% (year_seconds))
