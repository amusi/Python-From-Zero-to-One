def save_file(boy, girl, count):
    # 创建文件名称
        file_name_boy = "boy_"+ str(count) + ".txt"
        file_name_girl = "girl_" + str(count) + ".txt"

        # 打开文件
        boy_file = open(file_name_boy, "w")
        girl_file = open(file_name_girl, "w")

        # 按行写入
        boy_file.writelines(boy)
        girl_file.writelines(girl)

        # 关闭文件
        boy_file.close()
        girl_file.close()
def split_file(file_name):
    f = open(file_name)  # 按相对路径打开文件

    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != "======":
        # 我们这里使用split进行字符串分割操作
            (role, line_spoken) = each_line.split(":", 1)
            if role == "Amusi":
                boy.append(line_spoken)
            if role == "Lucy":
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)

            # 重新初始化
            boy = []
            girl = []
            count += 1
    f.close

split_file("record.txt")
