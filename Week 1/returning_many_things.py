def sayHello():
    "Say hello to the caller"
    print("Hello")

def sayHelloTo(name):
    "Say hello to the name"
    print("Hello", name)

def swap(a,b):
    "Swap the order of a and b in the return"
    return b,a

[x,y] = swap(1,2)

print("x is {}".format(x))
print("y is {}".format(y))
