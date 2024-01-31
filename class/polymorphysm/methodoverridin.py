class parent:
    
    def d1(self):
        
        print("d1 method p")
        
        def d2():
            pass
        
        
class child():
    
    def d1(self):
        
        print("d1 method c")
        
d = parent()
d.d1()


       
child().d1()
        
        

        
    
            