class grandparent:
    def d1(self):
        print("instance method d1")
        
class parent:
    def d2(self):
        print("instance method d2")        
        
class child(grandparent,parent):
    def d3(self):
        print("instance method d3")
        
c=child()   
c.d3()
c.d1()
c.d2()