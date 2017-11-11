try:
    for i in range(3):
        for j in range(3):
            if i == 2:
                raise KeyboardInterrupt
            print(i, j)
except KeyboardInterrupt:
    print("退出啦!")
