# 摄氏度转华氏度
def c2f(cel):
    fah = cel * 1.8 + 32
    return fah

# 华氏度转摄氏度
def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel
