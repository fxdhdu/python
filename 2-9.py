#coding=utf-8
#列表
students = ["a", "b", "c", "d", "e"]
print students[3]

students[3] = "e"
print students[3]

#元组
students = ("a", "b", "c", "d", "e") #元组中的元素不能修改
print students[3]

a = set("abcnmaaaggsng")
b = set("cdfm")
print a
print b
#交集
x = a & b
print x

#并集
y = a | b
print y

#差集
z = a - b
print z

#去除重复元素
new = set(a)
print a

#字典
k = {"姓名": "fxd", "籍贯": "hz"}
print k["籍贯"]

k["爱好"] = "音乐"
print k["姓名"]
print k["爱好"]
