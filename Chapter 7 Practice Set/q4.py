# 4. Write a program to find whether a given number is prime or not. 
n = int(input("Enter Your Number: "))
for i in range(2,n):
    if n%i == 0:
        print("The Given Number is not prime Number: ")
else:
    print("The Given Number is a Prime Number")
