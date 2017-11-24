# Summary: 先定义一个温度类，然后定义两个描述符类用于描述摄氏度和华氏度两个属性
#          要求两个属性会自动进行转换，也就是你可以给摄氏度这个属性赋值，然后打印的华氏度属性是自动转换后的结果
#          华氏度 = 摄氏度*1.8 + 32

# Author: Fangjie Chen
# Date:   2017-11-23

# 摄氏度
class Celsius:
    def __init__(self, value = 26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

# 华氏度
class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel*1.8 + 32
    def __set__(self, instance, value):
        instance.cel = (float(value)-32) / 1.8

# 温度
class Temperature:
    cel = Celsius()
    fah = Fahrenheit()
