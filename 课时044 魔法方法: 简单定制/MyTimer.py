# 导入time模块
import time as t

class MyTimer():
    def __init__(self):
        self.unit = ["年", "月", "日", "时", "分", "秒"]
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0
        self.end = 0
        
    def __str__(self):
        return self.prompt
    __repr__ = __str__


    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    
    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示: 先调用stop()停止计时!"
        print("计时开始...")

    # 停止计时
    def stop(self):
        self.end = t.localtime()
        if not self.begin:
            print("提示: 请先调用start()进行计时！")
        else:
            self.__calc()
            print("计时结束...")
    
    # 内部方法，计算运算时间
    def __calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        # 为下一轮计时初始化变量
        self.begin = 0
        self.end = 0
