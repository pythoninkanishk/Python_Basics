# 5. Write a program which finds out whether a given name is present in a list or not. 

L_1 = ["Harry", "Kanishk", "Jai", "Aryan", "Ishan"]

Name = input("Enter Name: ")
if Name in L_1:
    print("The given name is there in the list")
else:
    print("The given name is not there in the list")