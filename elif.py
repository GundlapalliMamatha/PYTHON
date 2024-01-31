userSalary = float(input("Enter your Salary: "))
print(userSalary)

if userSalary <= 10000:
    print("No Tax Deduction")
elif userSalary <= 50000:
    print("Tax Deduction")
else:
    print("User Salary is out of range or exceeds the maximum limit for tax calculation")
    
    