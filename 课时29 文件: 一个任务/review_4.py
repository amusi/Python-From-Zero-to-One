# Summary: 编写一个程序，实现”全部替换”功能
# Author:  Amusi
# Date:    2017-11-02

def Allreplace(file_name, old_word, new_word):
    f = open(file_name)
    content = []
    count = 0

    for each in f:
        if old_word in each:
            count += each.count(old_word)           # 计算每行出现的数量
            each2 = each.replace(old_word,new_word) # 行替换后的内容
        content.append(each2)   # 替换后总的内容

    f.close()
    decide = input("\n文件 %s 中共有%s个[%s]\n您确定要把所有的[%s]替换成[%s]吗？\n[YES/NO]:" \
                   % (file_name, count, old_word, old_word, new_word))

    if decide in ["YES", "Yes", "yes"]:
        f_write = open(file_name, "w")
        f_write.writelines(content)
        f_write.close()
        print("替换成功！")


file_name = input("请输入文件名: ")
old_word = input("请输入需要替换的单词或字符: ")
new_word = input("请输入新的单词或字符: ")

Allreplace(file_name, old_word, new_word)
