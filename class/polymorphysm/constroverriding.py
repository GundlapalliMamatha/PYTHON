from abc import ABC,abstractmethod
class parent(ABC):
    
    @abstractmethod 
    def __init__(self):
     pass

class child(parent):
      
   def __init__(self):
     print("special method")
     
     
child()

