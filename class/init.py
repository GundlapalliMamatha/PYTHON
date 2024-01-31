# class products:
#     def __init__(self,productname,productprice):
        
#         print(productname,productprice)
        

        
# products("samsung",10000)
# products("lg",20000)
class products:
    def __init__(self,productname,productprice):
        
        self.p_productname = productname
        self.pr_productprice=productprice
        
        print(self.p_productname,self.pr_productprice)
        
        
products("samsung",10000)