import numpy as np

nos = np.linspace(1,20,16,dtype=int).reshape(4,-1)

print(nos)

mask = nos%2 == 1
print(mask)
print(nos[mask])