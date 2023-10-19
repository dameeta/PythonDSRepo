l1=[4,3,2,5,7]
print('Printing l1',l1)
#repetition of list
l1repetition=l1*2
print('Printing l1',l1)
print(l1repetition)
l2=[8,9,11,15,17]
#concatenation
print('Length of l1+l2',len(l1+l2))
for i in l1repetition:
    print(i,end=' ')
#Membership
print('\n')
print('if 3 in 11',3 in l1)
l2.pop()
l2.pop()
l2.pop()
l2.pop()
l2.pop()
#l2.remove(17)

print(l2)