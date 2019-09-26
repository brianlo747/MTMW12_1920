def closerToZero(a,b):
    "Return the argument that is closer to zero"
    if abs(a) < abs(b):
        return a
    else:
        return b

x = 1.1
y = -1.1
z = closerToZero(x,y)

print("z is {}".format(z))
