# 6. Write a program to calculate the factorial of a given number using for loop. 
n = int(input("Enter Your No:  "))
 

if n<0:
    print("Negative no do not have a factorial")
elif n==0:
    print("The Factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The Factorial of {n} is {factorial}") 

