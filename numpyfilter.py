import numpy as np

sqre = np.array([
    [9,4,12,3],[9,8,4,17],[15,6,13,14],[12,6,8,4]
])
print(sqre)
for x in range(4):
    print(sqre[:,x].sum())
