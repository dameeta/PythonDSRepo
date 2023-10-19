import pandas as pd
import numpy as np

x=pd.Series(['A','B','C'])
#y=pd.Series(['K','L','M'])
print('Printing series x',end='\n')
print(x)
print(x.map({'A':'New','B':'second'}))
l1=[10,20,30,40,60,88,7,9,33]
l2=l1
print(l2[0])
print(l1[3:7])
print(l1[3:7:-1])