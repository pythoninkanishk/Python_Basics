
Age = int(input("Enter your age: "))
if Age%2 == 0:
     print("The number is even") 
# If statement 1
#The else and elif below the first if statement will be considered for the first elif


if Age>= 18:
    print("you are eligible to vote")
# Second if statement

elif Age < 0:
    print("Invalid age entered")    
else:
    print("you are not eligible to vote")

# IMPORTANT NOTES: 
# 1. There can be any number of elif statements. 
# 2. Last else is executed only if all the conditions inside elifs fail. 