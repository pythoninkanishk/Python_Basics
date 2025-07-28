# 1. Write a program to print multiplication table of a given number using for loop. 
# let us assume the given no is 7

Number =int(input("Enter A Number: "))
i = 1
for i in range(1,11):

    print(f"{Number} X {i} = {Number*i}")
