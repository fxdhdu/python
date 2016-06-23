print("Hello Python")

a = 10
b = 2
c = a + b
print(c)

score = 70

if score >= 80 :
    print("very good")
elif score >= 60 :
    print("good")
elif score >= 30 :
    print("bad")
else :
    print("very bad")

for i in range(0, 100) :
    print(i)

for i in range(0, 100) :
    print("Item {0}".format(i))

for i in range(0, 100) :
    print("Item {0}, {1}".format(i, "Hello Python"))

def sayHello() :
    print("Hello World")

def max(a, b) :
    if a > b :
        return a
    else :
        return b

sayHello()
print(max(2, 3))
