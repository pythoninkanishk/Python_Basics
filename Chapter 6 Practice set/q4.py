# 4. Write a program to find whether a given username contains less than 10 
# characters or not. 

Username = input("Username: ")
if (len(Username)>10):
    print("Username contains more than 10 characters")
elif(len(Username)==10):
    print("Username contains 10 characters")
else:
    print("username contains less than 10 characters")