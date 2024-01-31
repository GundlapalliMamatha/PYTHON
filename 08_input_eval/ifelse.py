userName = "Admin"
userPassword = "Admin"

name = input("Enter your user name: ")
print(name)

password = input("Enter your password: ")
print(password)

if name == userName and password == userPassword:
    print("Login Success")
else:
    print("Login Failed")