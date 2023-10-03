import pandas as pd
import numpy as np

sequenceofchars= np.array(['d','a','t','a'])
print(sequenceofchars)
print(type(sequenceofchars))
newseries= pd.Series(sequenceofchars)
print(type(newseries))
print(newseries)

citynames=['Chennai','Delhi','Mumbai']
dataframe= pd.DataFrame(citynames)
print(dataframe)
x=pd.Series()
print(x)
#creating list
listdata=[5,6,7.7,3.3,89,4.5]
#converting to pandas object
pdseries1=pd.Series(listdata)
print(pdseries1)
#creating dictionary object
dictdata={'A':'ClassA','B':"ClassB",'C':'ClassC'}
pdseries2=pd.Series(dictdata)
print(pdseries2)
#scalar values
scalardata=pd.Series([3,4,5,6,7],index=[1,2,3,4,5])
print(scalardata)
print(pdseries1.index)
print(pdseries1.values)
print(pdseries1.items)


