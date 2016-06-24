#coding=utf-8
#函数

a = "hellodog"
print len(a)


b = "student"
c = b.split("u")
print b
print c


def function(a, b):
	if a > b :
		print "a is big"
	else :
		print "b is big"

function(1, 2)


def test2(i, j):
	'''乘法运算'''
	k = i * j
	return (i, j, k)

x = test2(4, 6)
print x

print test2.__doc__

help(test2)
#文档字符串

