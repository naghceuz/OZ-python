# -*- coding: utf-8 -*- 

def add (a,b):
	print "Adding %d + %d" % (a,b)
	return a + b

def subtract(a,b):
	print "Subtracting %d - %d" % (a,b)
	return a - b

def multiply (a,b):
	print "Multiplying %d * %d" % (a,b)
	return a * b

def divide(a,b):
	print "Dividing %d / %d " % (a,b)
	return a/b

print "Lets do some match with just functions!"

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"


#交易所的交易总量
def tradingVolume(a,b,c,d,e):
	return a+b+c+d+e

print "The top five exchange trading volume is %d " % tradingVolume(200,300,300,300,300)


