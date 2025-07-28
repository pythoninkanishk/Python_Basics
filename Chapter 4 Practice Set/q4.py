# 4. Write a program to sum a list with 4 numbers.

NO =  []

First = int(input("Enter the first number: "))
NO.append(First)
Second = int(input("Enter the second number: "))
NO.append(Second)
Third = int(input("Enter the third number: "))
NO.append(Third)
Fourth = int(input("Enter the fourth number: "))
NO.append(Fourth)   

Sum = sum(NO)
print("Sum of the numbers in the list:", Sum)