class products:
    def getproducts(self,productname,productprice):
        
        self.p_productname = productname
        self.pr_productprice=productprice
        
        print(self.p_productname,self.pr_productprice)
        
        
p = products()
p.getproducts("samsung",10000)