l1=[10,20,30,40,50,60,70,80,10]
#print(L1)
#print(len(L1))
print(l1[:])
print(l1[:8])
print(l1[0:8])
print(l1[:8])
print(l1[0:8:2])
print(l1[0:-1:1])
print(l1.copy())
l1.copy()
print(l1)
#append
l1=[10,20,30,40,50,60,70,80]
l2=[10,20,30,40,50,60,70,80]
l1.append(l2[:])
print(l1)
#copy()
l3=[10,20,30,40,50,60,]
print(l3.copy())
print(l3)
#len()
print(l3[0:len(l3)])
print(l3[-8:-1:1])
print(l3[-5:])
print(l3[5:0:1])