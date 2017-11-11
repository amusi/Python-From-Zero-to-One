# Summary: 编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件（要求查找mp4,rmvb,avi的格式即可），并把创建的一个文件（videoList.txt）存放所有找到的文件的路径
# Author:  Amusi
# Date:    2017-11-03
import os
def search_file(file_path, target):
    os.chdir(file_path)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            video_list.append(os.getcwd() + os.sep + each_file + os.linesep)

        if os.path.isdir(each_file):
            search_file(each_file, target) # 递归调用
            os.chdir(os.pardir)   # 递归调用后切记返回上一层目录


file_path = input("请输入您需要搜索的路径: ")
program_dir = os.getcwd()

target = [".mp4", ".avi", ".rmvb"]
video_list = []
search_file(file_path, target)

f = open(program_dir + os.sep + "videoList.txt", "w")
f.writelines(video_list)
f.close