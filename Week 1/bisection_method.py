import numpy as np

def solveByBisect(f, a, b, nmax=100, e=1e-6):
    "Find a root of function f by bisection"
    "between a and b to tolerance e."
    "Maximum nmax iterations. Returns the"
    "root and the number of iterations used."

    for it in range(nmax):
        c = 0.5*(a+b)
        if f(a)*f(c) < 0:
            b=c
        else:
            a=c
        if abs(f(c)) < abs(e):
            break
    else:
        raise Exception("No root found by \
                        solveByBisect")
    return c, it+1

# Define a function to solve
def poly5(x):
    return x**5 + x + 1

root, nIts = solveByBisect(poly5, -1, 1)
print("Root of poly5 is ", root, " in ", nIts, " iterations. Check ",
"poly5(root) = ", poly5(root))

root, nIts = solveByBisect(np.sin,-10,50,10,.1)
print("Root of sin is ", root, " in ", nIts, " iterations. Check ",
"sin(root) = ", np.sin(root))
# This produces an answer of 28.203125 in 8 iterations.
# Difference between the bisection method and exact answer is 0.07, within
# the tolerance of 0.1

root, nIts = solveByBisect(np.exp,-0.1, 0.5)
# This results in a No root found by solveByBisect exception.
