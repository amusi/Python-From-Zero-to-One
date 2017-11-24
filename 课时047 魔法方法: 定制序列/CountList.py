# Summary:  编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数
# Author:   Fangjie Chen
# Date:     2017-11-23
class CountList:
    # 初始化——*args参数是可变数量的
    def __init__(self, *args):
        # 列表推导式
        self.values = [x for x in args]
        # 创建一个新列表
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self, values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]
