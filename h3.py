def d1():
    x=10
    print("scope",x)
    
    def d2():
        y=20
        z=30
        print("scope",y)
        print("scope",z)
    return d2

print("before:")
d = d1()
d()
print("after:")
del d1
d()
            
            

     
