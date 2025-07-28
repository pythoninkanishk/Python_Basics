# TYPES OF FUNCTIONS IN PYTHON 
# There are two types of functions in python: 
# • Built in functions (Already present in python) 
# • User defined functions (Defined by the user) 


# Build-In function
len(),print(),range()

#User defined Functions 
# (The one we made before)

def sum(name, end = "Thank You"):
    a =int(input("Enter Your Number: "))
    b =int(input("Enter Your Second Number: "))
    print(f"The sum of the two numbers is {a+b} for {name},\n {end}")
#this is the function call
sum("Kanishk", "Thanks")
sum("Parnika", "Thank u")
sum("Aanya", "Dhanyawad")
