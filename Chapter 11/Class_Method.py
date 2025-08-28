# @classmethod

class Kanishk:
    Salary = 10000000
    @classmethod
    def salary(cls):
        print(f"This is a class method of Kanishk's Salary is {cls.Salary}")
        

a = Kanishk()
a.Salary = 100
a.salary()

#Here the @classmethod is used to print the class variable Salary whenever the salary method is called.
# so @classmethod is used to define a method that belongs to the class rather than an instance of the class.