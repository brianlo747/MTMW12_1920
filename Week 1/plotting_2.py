import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
y1 = np.sin(x)
y2 = np.sin(3*x)
#plt.ion()
plt.clf()
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='sin(x)')
plt.legend()
plt.grid()
plt.xlabel('x')

plt.axis([x[0],x[-1], -1, 1])
plt.show()
