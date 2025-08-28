 # 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt. 

N = int(input("Enter Your Number: "))
table = [N*i for i in range(1,11)]
print(table)

with open("Table.txt", "a") as f:
    f.write(f"Table of {N}: {(table)} \n")