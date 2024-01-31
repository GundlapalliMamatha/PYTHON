def Account():
    Accountbalance = float(input("Enter your accountbal: "))

    if  Accountbalance == 10000.0:
        print('positive')
    elif Accountbalance > 10000.0:
        print("account bal is negative ")
    else:
        print("low account balance")
    
    
Account()