from multipledispatch import dispatch
class static:
    @dispatch(int,int)
    def d1(self,a,b):
      print(a,b)
    
    @dispatch(str,str) 
    def d1(self,a,b):
      print(a,b)
      
    @dispatch(str,str,int) 
    def d1(self,a,b,c):
      print(a,b)
      
c = static()
c.d1(10,20)
c.d1("hi","mamatha")
    