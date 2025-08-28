# 7. Override the __len__() method on vector of problem 5 to display the dimension of the 
# vector. 
class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}z"
    def __add__(self, other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    def __mul__(self, other):
        result = vector(self.x * other.x, self.y * other.y, self.z * other.z)
        return result
    def __len__(self):
        return 3
x = vector(1,4,3)
z = vector(2,3,4)
print(x + z)
print(x*z)
print(len(x))
print(len(z))