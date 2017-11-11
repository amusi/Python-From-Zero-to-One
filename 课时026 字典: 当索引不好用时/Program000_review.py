#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 23:16:57 2017

@author: amusi
"""

def PrintInfo():
    print("""|--- 欢迎进入通讯录程序 ---|
             |--- 1:查询联系人资料  ---|
             |--- 2:插入新的联系人  ---|
             |--- 3:删除已有联系人  ---|
             |--- 4:退出通讯录程序  ---|
            """)

def Process(n):
    contacts = dict()
    while 1:
        if n == 1:
            nameTemp = input("请输入联系人姓名: ")
            if nameTemp in contacts: # 注意写法
                print(nameTemp + ": " + contacts[nameTemp])
            else:
                print("您输入的姓名不在通讯录中!")
        if n == 2:
            nameTemp = input("请输入联系人姓名: ")
            if nameTemp in contacts:
                print("您输入的姓名在通讯录中已经存在-->>", end ="") # 不换行
                print(nameTemp + ": " + contacts[nameTemp])
            else:
                contacts[nameTemp] = input("请输入用户联系电话: ")
        if n == 3:
            nameTemp = input("请输入联系人姓名: ")
            if nameTemp in contacts:
                del(contacts[nameTemp])  # 注意写法，也可以使用dict.pop()
            else:
                print("您输入的联系人不存在...")
        if n == 4:
            print("|--- 感谢使用通讯录程序 ---|")
            break;
        n = int(input("\n请输入相关的指令代码: "))


PrintInfo()
num = int(input("请输入相关的指令代码: "))
Process(num)