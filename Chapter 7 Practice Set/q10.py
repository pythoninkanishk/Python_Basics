# 10. Write a program to print multiplication table of n using for loops in reversed

n = int(input("Enter Your number: "))
i = 1
for i in range (10,0,-1):
    print(f"{n} X {i} = {n*i}")