class parent:
    def d1(self):
        print("instance method d1")
        
        
class child(parent):
    def d2(parent):
        print("instance method d2")
        
c=child()   
c.d1()
c.d2() 