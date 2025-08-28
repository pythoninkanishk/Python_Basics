class employee:
    Language  = "Py"  
    Salary = 12000000
    def __init__(self, Name,  Job):
        self.Name = Name
        self.Job = Job
        print(f"My Name is {self.Name}. My occupation is {self.Job} ")
    def GetLanguage(self): 
        print(f"The Salary of employee is {self.Salary}")
    @staticmethod
    def Greet():
        print("Hello User")     
Kanishk = employee("Raju LALA", "Dhobi")
print(Kanishk.Salary)
print(Kanishk.Language)
