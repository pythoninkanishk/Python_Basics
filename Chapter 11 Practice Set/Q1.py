# 1. Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector. 
class vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"THE GIVEN VECTOR ({self.x}, {self.y})"
class vector3D(vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def __str__(self):
        return f"THE GIVEN VECTOR ({self.x}, {self.y}, {self.z})"
 
X = vector2D(1,3)
print(X)
Y = vector3D(1, 2, 3)
print(Y)
