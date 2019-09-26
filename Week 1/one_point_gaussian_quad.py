# Calculate the approximate integral of sin(x) between a and b using
# 1-point Gaussian quadrature using N intervals

# Import numerical library
import numpy as np

# Set integration limits and number of intervals

# Lower limit a
a = 0

# Upper limit b
b = np.pi

# Number of intervals N
N = 20

# from these calculate the interval length dx
dx = (b - a) / N

# Initialise the integral
I = 0.0

# Sum contribution from each interval (end of loop at end of indentation)
for i in range(0,N):
    I += np.sin(a + (i+0.5) *dx)

I *= dx

# Check exact answer
exact = -np.cos(b) + np.cos(a)

# Print out comparison between one-point quadrature and exact methods
print('Gaussian quadrature integral (with ', N, ' intervals) is', I, \
    '\nExact integral = ', exact, ', error =', I - exact)
