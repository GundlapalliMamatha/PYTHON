from abc import ABC,abstractmethod
class parent(ABC):
    @staticmethod
    @abstractmethod
    def d1():
       pass
   
    @classmethod   
    @abstractmethod
    def d2(cls):
            pass
    @abstractmethod
    def d3(self):
            pass
        
class child(parent):
    def d1():
        print("d1 method of abs")
    def d2(cls):
        print("d2 method of abs")
    def d3(self):
        print("d3 method of abs")
        
            
c=child()
c.d2()
c.d1()
c.d3()