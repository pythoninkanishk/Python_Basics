#Static Method:
# Sometimes we need a function that does not use the self-parameter. We can define a 
# static method
class employee:
    Language  = "Py"  #This is a Class 
    Salary = 12000000
    def GetLanguage(self): #we need self parameter as Kanishk.GetLanguage() is taken as Employee.GetLanguage(Kanishk) so we write self to define kanishk as a variable
        print(f"The Salary of employee is {self.Salary}")
    @staticmethod
    def Greet():
        print("Hello User")     
Kanishk = employee()
Kanishk.GetLanguage()
Kanishk.Greet()

# Here We didn't need to specify a user so we used the static method 