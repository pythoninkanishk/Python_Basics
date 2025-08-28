class Employee:
        name = input("Enter the name of the employee: ")
        salary = int(input("Enter the salary of the employee: "))
        def Selfintro(self):
         print(f"The Name of the employee is {self.name} and the salary is {self.salary}")
class Coder():
          Language = input("Enter the programming language of the programmer: ")
          def Selfintro2(self):
           print(f"The programming language used by Employee is {self.Language}")
class Programmer(Employee, Coder):
          def Selfintro3(self):
           print(f"The Name of the programmer is {self.name}, the salary is {self.salary}, and the programming language is {self.Language}")

B = Programmer()
B.Selfintro3()


# In this code, we have implemented multiple inheritance where the Programmer class inherits from both Employee and Coder classes.
# This allows Programmer to access attributes and methods from both parent classes.