class employee:
    Language  = "Py"  #This is a Class 
    salary = 12000000
Kanishk = employee() # THIS IS OBJECT INSTATIATION (Something like naming the employee "Kanishk")
employee.salary = 120000000 #This is a instance attribute
employee.Language = "JavaScript" #When both instance attributes and class attributes are defined then Instance attribute is prioritized
print(Kanishk.salary)     