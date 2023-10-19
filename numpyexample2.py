import numpy as np
temperatures = np.array([
    45.9,34.44,30.2,23.8,20.12,19.2
]).reshape(2,1,3)
print(temperatures)
#in numpy the axes are 
# two dim arrayhas vertical axis (axis 0) and a horizontal axis(axis 1)
tab=np.array([
    [3,4,5,2],[8,2,4,1],[6,3,5,6],[9,10,2,3]])
print(tab.max())
print(tab.max(axis=0))
print(tab.max(axis=1))