# Getter, Setter, @property Methods
class Employee:
    def __init__(self):
        self._ename = ""

@property 
def name(self):
    name = self._ename
    return name
@name.setter
def name(self, value):
    self.ename = value
    if value == " ":
        print("Please enter a valid name")
# Using the class
e = Employee()
e.name = "Kanishk"   # Calls setter
print(e.name)          # Calls getter
e.name =" "
print(e.name)          # Calls getter again