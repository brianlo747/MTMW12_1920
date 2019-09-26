def swap(a,b):
    "Swap the order of a and b in the return"
    return b,a

def closerToZero(a,b):
    "Return the argument that is closer to zero"
    if abs(a) < abs(b):
        return a
    else:
        return b

def maxAbs(a,b):
    "Make both arguments non-negative and return the bigger one"
    a = abs(a)
    b = abs(b)
    return max(a,b)

def main():
    "Put a script inside a main function"
    [x,y] = swap(closerToZero(1,2), maxAbs(3,4))
    print('x =', x, 'y =', y)

main()

help(swap)
