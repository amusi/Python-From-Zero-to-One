# Summary: 简单介绍类(class)的一个简单的例子
# Author:  Fangjie Chen
# Date:    2017-11-13

# Python中的类名约定以大写字母开头
class Turtle:
    # 属性
    color = "green"
    weight = 20
    height = 8
    mouth = "big"

    # 方法
    def climb(self):
        print("我正在努力地向前爬...")

    def run(self):
        print("我正在努力地向前跑...")

    def fly(self):
        print("我正在努力地向前飞...")

    def sleep(self):
        print("我正在睡觉...")
