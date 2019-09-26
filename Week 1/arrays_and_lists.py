myList = [8, 3, 5, 1]

import numpy as np
arraySize = 5
myArray = np.zeros(arraySize)

for i in range(arraySize):
    myArray[i] = 2*i + 3
print(myArray)
