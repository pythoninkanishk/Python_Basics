# Recursion is a function which calls itself. 

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
a = factorial( int(input("Enter Your Number: ")))
print(f"the Factorial of the given no  is {a}")