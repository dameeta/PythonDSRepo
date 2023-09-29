import numpy as np

data1=np.empty(2,dtype=int)
print("Data is:\n ", data1)

data2=np.empty([3,3],dtype=int)
print("\n Data2 is : \n", data2)

data3=np.empty([4,4])
print("\n The data3 is:\n",data3)

data4 =np.zeros(2,dtype=int)
print("\n Data4 is:\n ", data4)
data5=np.zeros([3,3],dtype=int)
print("\n Data5 is : \n", data5)

data6=np.zeros([4,4])
print("\n The data6 is:\n",data6)


data7 =np.zeros(2,dtype=int)
print("Data7 is:\n ", data7)

arr1=np.array([[2,3,4,7],[3,5,6,7]])
arr2=np.array([[2,3,6,8],[6,7,8,9]])
print(arr1)
print(arr2)
print('Addition of two matrix arr1 and arr2 is')
print(arr1+arr2)

newarray1=np.arange(10,2,-1)
print('Arrays of -ve sequence ',newarray1)
newarray2=newarray1[np.array([3,1,3])]
print(newarray2)

