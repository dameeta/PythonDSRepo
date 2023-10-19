list1=[]
print('Printing list1',list1)
list2=[8,5,4.5,3,0,'data','store']
print('Printing list2',list2)
list3=[0,3,2.9,1.2]
print('Printing list3',list3)

list2.append(list3)
print('Printing list2',list2)
print(list2[0],list2[1],list2[-1][3])
print('Printing list1',list1)
list1.append(list2)
list1.append(1)
print('Again printing list1',list1)

print('list1 at 0th index',list1[0])
print('list1 at 1st index',list1[1])
print('Accessing last element of the list1',list1[-1])
#slicing of list
newstringlist=['C','o','m','p','u','t','e','r']
print(newstringlist[1:4])
print('all data from m till end',newstringlist[2:])
print('all data from beginning till end',newstringlist[:])
print('Hello')
list1[0]
list1[1]
