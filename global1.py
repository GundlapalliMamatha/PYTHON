empId = 34576
def emp():
    
    globals()["empId"] = 56789
    print(globals()["empId"]) 
    print("empId Number: ", empId) 
    
    
emp()