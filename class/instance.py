class emp:
    
    def getemployees(self,eid,empname,empsalary):
        
        self.eid=eid#instance variable
        self.empname=empname#instance variable
        self.empsalary=empsalary#instance variable
        
        print(self.eid,self.empname,self.empsalary)
    
    
e = emp()
e.getemployees(122,"mamatha",122000)

e.empaddress="sithaphalmandi"
print(e.eid,e.empname,e.empsalary,e.empaddress)
print(getattr(e.empname="srinivas"),e.eid,e.empname,e.empsalary,e.empaddress)