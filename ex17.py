# -*- coding: utf-8 -*-

# 使用 argv 的特点
from sys import argv
# 使用exists, 这个命令将文件名字符串作为参数，如果文件存在的话，它将返回True，否则将返回 False
from os.path import exists

# 输入的时候需要python 脚本名，文件名1， 文件名2
script, from_file, to_file = argv

# 把文件1的内容复制，然后存到文件2
print "Copying from %s to %s " % (from_file, to_file)

# we could do thses two on one line , how ?
#  打开文件1
in_file = open(from_file)
# 读取文件1的内容
indata = in_file.read()

# 判断文件1的大小
print "The input file is %d bytes long" % len(indata)

# 
print "Does the output file exists ? %r " % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# 打开第二个文件
out_file = open(to_file, 'w')

# 把文件1的内容存到文件2
out_file.write(indata)


# 打印 整个程序运行完毕
print "Alright, all done."
# 关闭out_file 文档
out_file.close()
# 关闭 in_file 文档
in_file.close()

