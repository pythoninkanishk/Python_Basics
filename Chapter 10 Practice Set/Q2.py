# 2. Write a class “Calculator” capable of finding square, cube and square root of a 
# number


class Calculator():
    def __init__(self, n):
        self.Number = n
    def Square(self):
        return self.Number**2
    def Cube(self):
        return self.Number**3
    def Root(self):
        return self.Number**0.5
    
Number = Calculator(2)
print("Square: ", Number.Square())
print("Cube: ", Number.Cube())
print("Root: ", Number.Root())
        
        