def firstFunction():
    print("hello Students")
firstFunction()


def add(a,b):
    sum = a+b
    return sum
print(add(1,2)) 


x = 101  #Global Variable/scope

def func():
    x = 102 #Local scope
    print(x)

func()
print(x)

27