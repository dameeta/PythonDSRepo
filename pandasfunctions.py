import pandas as pd
import numpy as np

x=pd.Series(['A','B','C'])
#y=pd.Series(['K','L','M'])
print(x.map({'A':'New','B':'second'}))