# Summary:
# Author: Fangjie Chen
# Date:   2017-11-14
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置: (%d, %d)" % (self.x, self.y))

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry == True:
            print("有吃的啦！")
            self.hungry = False
        else:
            print("太撑了，吃不下了")

