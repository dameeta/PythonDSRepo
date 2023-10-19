import pandas as pd

data = pd.DataFrame({"col1":[4,5,6,None,7,7],"col2":[34,56,None,7,4,3],
                     "col3":[5,6,None,4,3,2],
                     "col4":[6,7,8,9,45,None]})
print(data)
print(data.mean(axis=0))
print(data.mean(axis=0,skipna=True))
