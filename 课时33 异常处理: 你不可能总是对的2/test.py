try:
    
    f = open("try_except.txt", "w")
    print(f.write("我存在啦！"))
    sums = 1 + "1"
except (OSError, TypeError, ValueError):
    print("出错啦!")
finally:
    f.close()
