class product:
    productname="car"
    productid=101
    @classmethod
    def getproductdetails(cls):
        print(cls.productname,cls.productid)
        
product.getproductdetails()
        