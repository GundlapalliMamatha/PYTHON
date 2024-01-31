num = int(input("Enter a number: "))

# Convert the number to a string to find its length
num_str = str(num)
n = len(num_str)

# Calculate the sum of each digit raised to the power of n
armstrong_sum = sum(int(digit) ** n for digit in num_str)

# Check if the sum is equal to the original number
if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")