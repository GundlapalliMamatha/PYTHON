def d1(a):
    def d2(b):
        return print(a+b) 
    return d2

d=d1(10)
d(20)