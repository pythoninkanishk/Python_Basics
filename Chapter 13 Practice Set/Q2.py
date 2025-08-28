# 2. Write a program to input name, marks and phone number of a student and format it 
# using the format function like below:

a = input(("Enter Your Name: "))
b = int(input("Enter Your Marks: "))
c = int(input("Enter Your Phone No.: "))

Format = "The Name of the student is {0}, his marks are {1} and Phone no is {2} ".format( a , b, c )
print(Format)