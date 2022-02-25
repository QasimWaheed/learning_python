import math

class myClass1():
    def funct1(self):
        a = math.pi
        print(a)

def gs(num, x= 1):
    for i in range(x):
        result = num * x
    return result

a = myClass1()
a.funct1()
# print(myClass1.funct1())