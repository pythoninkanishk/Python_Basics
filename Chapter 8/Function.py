# A function is a group of statements performing a specific task. 
#This is the function Definition
def sum(name, end = "Thank You"):
    a =int(input("Enter Your Number: "))
    b =int(input("Enter Your Second Number: "))
    print(f"The sum of the two numbers is {a+b} for {name},\n {end}")
#this is the function call
sum("Kanishk")
sum("Parnika", "Thank u")
sum("Aanya", "Dhanyawad")

# Here end = "Thank You" sets a default parameter value if a value is not mentioned it will use the default value as in line 8