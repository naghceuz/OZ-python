# -*- coding: utf-8 -*- 
# 引用一个argv库
from sys import argv

# 运行时需要输入一个文件名
script, input_file = argv 

# 一个函数，print_all, 输入是一个文件，打印文件中的内容
def print_all(f):
	print f.read()

# 一个函数把文件的位置放在一个固定的地方
def rewind(f):
	f.seek(0)

# 一个函数，两个输入。打印第一个输入，然后一行一行打印输入2的内容
def print_a_line(line_count, f):
	print line_count, f.readline()

# 打开文件，存诚current_file 
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)




