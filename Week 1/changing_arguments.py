def maxAbs(a,b):
    "Make both arguments non-negative and return the bigger one"
    a = abs(a)
    b = abs(b)
    return max(a,b)

z = maxAbs(1.1, -1.2)
print("z is {}".format(z))
