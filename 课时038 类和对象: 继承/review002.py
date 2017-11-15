# Summary:定义一个点（Point）类和直线（Line）类，使用getLen方法可以获得直线的长度
# Author: Fangjie Chen
# Date:   2017-11-15
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Line(Point):
    def __init__(self, p1, p2):
        self.x = p1.x - p2.x
        self.y = p1.y - p2.y
        self.len = 0
    # 计算直线长度
    def getLen(self):
        self.len =  math.sqrt(self.x * self.x + self.y * self.y)
        return self.len
