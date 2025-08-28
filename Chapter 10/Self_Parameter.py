#Self Parameter:
class employee:
    Language  = "Py"  #This is a Class 
    Salary = 12000000
    def GetLanguage(self): #we need self parameter as Kanishk.GetLanguage() is taken as Employee.GetLanguage(Kanishk) so we write self to define kanishk as a variable

        print(f"The Salary of employee is {self.Salary}") 
Kanishk = employee()
Kanishk.GetLanguage()

