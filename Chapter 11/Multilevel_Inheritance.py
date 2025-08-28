class Employee:
        name = input("Enter the name of the employee: ")
        salary = int(input("Enter the salary of the employee: "))
        def Selfintro(self):
         print(f"The Name of the employee is {self.name} and the salary is {self.salary}")
class Coder(Employee):
          Language = input("Enter the programming language of the programmer: ")
          def Selfintro2(self):
           print(f"The Name of the programmer is {self.name} and the salary is {self.salary} and the programming language is {self.Language}")
class Manager(Coder):
          Manager = input("Enter the name of the manager: ")
          def Selfintro3(self):
           print(f"The Name of the programmer is {self.name}, the salary is {self.salary}, and the programming language is {self.Language} and is managed by {self.Manager}")
A = Employee()
B = Coder() 
c = Manager()
c.Selfintro3()
# In this code, we have implemented multilevel inheritance where the Manager class inherits from Coder, which in turn inherits from Employee.
# This allows Manager to access attributes and methods from both Coder and Employee classes, demonstrating the concept of multilevel inheritance.