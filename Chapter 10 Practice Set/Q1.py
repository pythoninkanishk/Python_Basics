# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.
class Programmer():
    Company = "Microsoft"
    def __init__(self, Name, Salary, Pincode):
        self.Name = Name 
        self.Salary = Salary
        self.Pincode = Pincode

P = Programmer("Kanishk", "4800000", 302031)
print(P.Name, P.Company, P.Salary, P.Pincode)
G = Programmer("Ramesh", "2000000", "302030")
print(G.Name, G.Company, G.Salary, G.Pincode)