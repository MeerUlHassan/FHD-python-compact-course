#Create a program that will calculate the factorial

n = int(input('Enter an non-negative integer to check factorial: ' ))

if n < 0:
    print("Error: Factorial does not exist for negative numbers.")
elif n == 0 or n == 1:
    print(f"The factorial of {n} is: 1")
else:
    factorial = 1
        # Loop from 2 up to n
    for i in range(2, n + 1):
        factorial *= i
    print(f"The factorial of {n} is: {factorial}")