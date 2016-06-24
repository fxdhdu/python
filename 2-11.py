#coding=utf-8
#pickle腌制
import pickle

#dumps(object)将对象序列化，用于对象的持久性存储，使用时再恢复（序列化过程称为pickle）
lista = ["wojiao", "fxd", "shima"] #列表
listb = pickle.dumps(lista)
print listb

#load(string)将对象原样恢复，并且对象类型也恢复原来的格式
listc = pickle.loads(listb)
print listc

#dump(object, file)将对象存储到文件里面序列化
group1 = ("baidu", "wen", "qingtian")
f1 = file('1.pk1', 'wb')
pickle.dump(group1, f1, True)
f1.close()

#load(object, file)将dump()存储在文件里面的数据恢复
f2 = file('1.pk1', 'rb')
t = pickle.load(f2)
print t
f2.close()
