#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:36:38 2017

@author: amusi
"""
print(".............Amusi...........")
temp = input("Can you guess which number I am thinking?")
guess = int(temp)
if guess == 8:
    print("Congratulations!")
else:
    print("Sorry")
print("Game Over...")