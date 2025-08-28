class Employee:
        name = input("Enter the name of the employee: ")
        salary = int(input("Enter the salary of the employee: "))
        def Selfintro(self):
         print(f"The Name of the employee is {self.name} and the salary is {self.salary}")
class Programmer(Employee):
          Language = input("Enter the programming language of the programmer: ")
          def Selfintro2(self):
           print(f"The Name of the programmer is {self.name} and the salary is {self.salary} and the programming language is {self.Language}")

A = Employee()
B = Programmer()
B.Selfintro2()


#To use the attributes of  Employee class in programmer without typing it again, we can use inheritance.
#In this case, Programmer is inheriting from Employee, so it can access the attributes and methods of Employee directly.
#When we create an instance of Programmer, it can use the attributes defined in Employee without needing to redefine them.
#This is also an example of single inheritance, where one class (Programmer) inherits from another class (Employee).
