# 3. Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number. 

N = int(input("Enter Your Number: "))
table = [N*i for i in range(1,11)]
print(table)