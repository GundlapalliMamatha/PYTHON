l3=[10,20,30,40,50,60]
   # -6 -5 -4 -3 -2 -1
#print(l3[-6:-1]) #[10, 20, 30, 40, 50]its not printing 60
#print(l3[-5:-2]) #[20, 30, 40]its not printed -2position 50
#print(l3[0:-1:1]) # [10, 20, 30, 40, 50]its not printed 60
#print(l3[-1:-6:1]) #[]its not printed in reverse order
#print(l3[::-2])

print(l3[-1:-6:1]) # []
print(l3.pop(4))
print(l3.remove(60))
print(l3)
del l3[20]
print(l3)