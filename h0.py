def d1():
    print("parent")
    def d2():
        print("child")
    return d2
d=d1()
print(d)
print(d.__name__)
d()