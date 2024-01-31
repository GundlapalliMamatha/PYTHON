class products:
    def getproducts(cls,productname,productprice):
        
        cls.p_productname = productname
        cls.pr_productprice=productprice
        
        print(cls.p_productname,cls.pr_productprice)
        
        
p = products()
p.getproducts("samsung",10000)