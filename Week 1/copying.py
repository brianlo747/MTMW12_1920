a = ['Jack', 'Jill', 'Tim', 'Dave']
b = a
a[0] = 'Fred'
print(b)

import numpy as np
a = np.array(['Jack', 'Jill', 'Tim', 'Dave'])
b = a.copy()
a[0] = 'Fred'
print(b)
