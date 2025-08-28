# SUPER() METHOD 

class Employee:
    def __init__(self):
        print("Constructor of Employee class")
    
class Coder:
    def __init__(self):
        print("Constructor of Coder class")
    
class Programmer(Employee):
    def __init__(self):
     super().__init__()  # Calls the constructor of Employee
     print("Constructor of Programmer class")
a = Programmer()
# In this code, we have used the super() method to call the constructor of the Employee class from the Programmer class.
print("Programmer class is created successfully", )
