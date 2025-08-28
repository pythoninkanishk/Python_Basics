# 3. Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary
class employee:
    Salary = 100000
    Increment = 20
    @property
    def SalaryAfterIncrement(self):
       return self.Salary + self.Salary*(self.Increment/100)
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, salary):
        self.Increment = (salary/self.Salary-1)*100
    
e = employee()
e.SalaryAfterIncrement = 100000000
print(e.Increment)




