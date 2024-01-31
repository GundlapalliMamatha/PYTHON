def data():
    
     a = 10
     b = "Sai Kiran"
     c = [1, 2,3, 4, 5]
    
     print("Data: ",a, b, c)  
     data = locals()
     print("Data: ", data)  
    
     print("Data: ", locals()["a"] )
     print("Data: ", locals()["b"] )
     print("Data: ", locals()["c"] )
    
    # data['a'] = 20
     #print('Temporary: ', data['a'])
     #print(locals()["a"])
     #print("Data: ", a)
    
     #print("Data: ", data) 
     

data()