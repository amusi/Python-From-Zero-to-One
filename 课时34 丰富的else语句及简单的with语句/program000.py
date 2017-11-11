# 要么怎样，要么不怎样
def choose(flag):
    if flag == True:
        print("True")
    else:
        print("False")
choose(True)

# 干完了能怎样，干不完就别想怎样
def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("%d最大约数是%d" % (num, count))
            break
        count -= 1
    else:
        print("%d是素数!" % num)

num = int(input("请输入一个数: "))
showMaxFactor(num)
