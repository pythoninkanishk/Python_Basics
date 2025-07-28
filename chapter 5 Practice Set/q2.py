# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 

Numbers = {}
Numbers = set()  # Using a set to store unique numbers
print("Enter 8 numbers:")
Numbers.add(int(input("Enter number 1: ")))
Numbers.add(int(input("Enter number 2: ")))
Numbers.add(int(input("Enter number 3: ")))
Numbers.add(int(input("Enter number 4: ")))
Numbers.add(int(input("Enter number 5: ")))
Numbers.add(int(input("Enter number 6: ")))
Numbers.add(int(input("Enter number 7: ")))
Numbers.add(int(input("Enter number 8: ")))
print("Unique numbers:", Numbers)
# Note: The code uses a set to ensure uniqueness of numbers.