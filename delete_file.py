#!/usr/bin/python
#-*-coding=utf8 -*-
import time
import os
import shutil

'''
删除指定路径下所有指定日期前的文件
包括指定路径下的文件夹里的文件
'''

N = int(input("请输入要删除几天前的文件:"))
path = input("请输入要删除的文件夹绝对路径(默认路径为C:\TestTools\GTR\Bin\log可以直接回车):")
# C:\TestTools\GTR\Bin\log
print("当前时间是： %s" % time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
def deletefile(path):
    if path == '':
        path = 'C:\TestTools\GTR\Bin\log'
    for eachfile in os.listdir(path):
        filename = os.path.join(path,eachfile)
        if os.path.isfile(filename):
            lastmodifytime = os.stat(filename).st_mtime
            print("======================")
            print("%s 文件的最后修改时间是： %s" % (filename,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(lastmodifytime))))
            print("%s 文件的创建时间是： %s" % (filename,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.stat(filename).st_ctime))))
            endfiletime = time.time() - 3600 * 24 * N #设置删除多久之前的文件
            print("删除文件的截止时间是： %s" % time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(endfiletime)))
            if endfiletime > lastmodifytime:
                print("我要删除文件： %s" % filename)
                os.remove(filename)
        elif os.path.isdir(filename):   #如果是目录则递归调用当前函数
            lastmodifytime = os.stat(filename).st_mtime
            print("======================")
            print("%s 目录的最后修改时间是： %s" % (filename,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(lastmodifytime))))
            print("%s 目录的创建时间是： %s" % (filename,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.stat(filename).st_ctime))))
            endfiletime = time.time() - 3600 * 24 * N #设置删除多久之前的文件
            print("删除目录的截止时间是： %s" % time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(endfiletime)))
            if endfiletime > lastmodifytime:
                print("我要删除目录： %s" % filename)
                shutil.rmtree(filename)

    input("删除完成，按回车键退出...")
    exit(0)

if __name__ == '__main__':
    deletefile(path)
