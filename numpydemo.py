import numpy as np

arr1=np.array([[2,6,6],[9,10,11],[7,8,9]])

print('Type of arr1 is:',type(arr1),'arr1 is of',arr1.ndim,'dimension')
print(arr1)
print('The shape of arr1 is:',arr1.shape,'The data type of an arr1 is:',arr1.dtype,'size of an arr1 is:',arr1.size)  # noqa: E501
#generating arrays

arr2=np.zeros((2,2))
print(arr2.dtype)

arr3=np.arange(1,20,2)
print(arr3)

