#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 17:35:33 2017

@author: amusi
"""

def discount(price, rate):
	final_price = price * rate
	return final_price

old_price = float(input("请输入原价： "))
rate = float(input("请输入折扣率: "))
new_price = discount(old_price, rate)
print("打折后价格为: ", new_price)