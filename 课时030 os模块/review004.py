# Summary: 编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀），要求显示该文件所在的路径以及关键字在文件中的具体位置（第几行第几个字符）
# Author:  Amusi
# Date:    2017-11-03

import os # 加载模块

# 输出位置
def print_pos(key_dict):
    #
    keys = key_dict.keys()
    keys = sorted(keys) #由于字典是无序的，所以这里对行数进行排序
    for each_key in keys:
        print("关键字出现在第 %s 行, 第 %s 个位置" % (each_key, str(key_dict[each_key])))

# key在每行对应的位置
def pos_in_line(line, key):
    pos = []
    begin = line.find(key)
    while begin != -1:
        pos.append(begin + 1)   # 代码的索引+1 = 用户直观的索引
        begin = line.find(key, begin + 1) # 从下一个位置继续查找
    return pos

# 读取当前txt文件进行查询
def search_in_file(file_name, key):
    f = open(file_name)
    count = 0 # 记录行数
    key_dict = dict()

    # 遍历文件中的每一行
    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line, key) # key在每行对应的位置
            key_dict[count] = pos
    f.close()
    return key_dict
# 查询函数
def search_files(key, detail):
    # 获得当前路径及子目录下所有文件名
    all_files = os.walk(os.getcwd())
    txt_files = []

    # 遍历所有层目录下的所有文件
    for i in all_files:
        # 遍历当前层目录下的所有文件
        for each_file in i[2]:
            # 根据文件后缀判断是否为文本文件
            if os.path.splitext(each_file)[1] == ".txt":
                # 添加文件的绝对路径
                each_file = os.path.join(i[0], each_file)
                txt_files.append(each_file)

    # 对所有txt文件进行查询
    for each_txt_file in txt_files:
        # 读取当前txt文件进行查询
        key_dict = search_in_file(each_txt_file, key)
        if key_dict:
            print("=============================")
            print("在文件[%s]中找到关键字[%s]" % (each_txt_file, key))
            if detail in ["YES", "Yes", "yes"]:
                print_pos(key_dict)

key = input("请将脚本(.py)放在待查找的文件夹中，请输入待查询的关键字: ")
detail = input("请问是否需要打印关键字[%s]在文件中的具体位置(YES/NO): " % key)
search_files(key, detail)   # 查询