# Summary:多重继承使用不当会导致重复调用（也称钻石继承、菱形继承）的问题，请分析以下代码在实际编程中有可能导致什么问题？
# Author: Fangjie Chen
# Date:   2017-11-15

class A():
    def __init__(self):
        print("进入A...")
        print("离开A...")

class B(A):
    def __init__(self):
        print("进入B...")
        A.__init__(self)
        print("离开B...")

class C(A):
    def __init__(self):
        print("进入C...")
        A.__init__(self)
        print("离开C...")


class D(B, C):
    def __init__(self):
        print("进入D...")
        # B.__init__(self)
        # C.__init__(self)
        # 使用super函数解决多重继承的问题
        super().__init__()
        print("离开D...")
