#!/G:\pythondemo\Test
# encoding: utf-8

# import os
#
# from day03.runoob1 import runoob1
# from day03.runoob2 import runoob2
#
# runoob1()
# runoob2()
#
#
# print(os.getcwd())







#
# #打开一个文件
# fo = open("mac-error.txt","w")
#
# print("文件名称：",fo.name)
# print("是否已关闭：",fo.closed)
# print("访问模式：",fo.mode)
# print("末尾是否强制加空格：",fo.softspace)
#


# #创建一个文件并写入数据
# fo = open("foo.txt","w")
# fo.write("www.primestone.com!\lynn\suzhou")
#
# fo.close()



# fo = open("mac-error.txt","r+")
# str = fo.read(300)
# print("读取的字符串是：",str)
#
# fo.close()



import os

#重命名文件foo.txt到too.txt
#os.rename("foo.txt","too.txt")

os.remove("too.txt")
