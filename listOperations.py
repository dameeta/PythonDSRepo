l1=[4,3,2,5,7]
#repetition of list
l1repetition=l1*2
print(l1repetition)
l2=[8,9,11,15,17]
#concatenation
print(len(l1+l2))

for i in l1repetition:
    print(i,end=' ')
#Membership

print(8 in l1)

l2.pop()
l2.pop()
l2.pop()
l2.pop()
l2.remove(17)

print(l2)