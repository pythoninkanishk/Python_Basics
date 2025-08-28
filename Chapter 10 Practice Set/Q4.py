# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator():
    @staticmethod
    def greet():
        print("Hello User")
    def __init__(self, n):
        self.Number = n
    def Square(self):
        return self.Number**2
    def Cube(self):
        return self.Number**3
    def Root(self):
        return self.Number**0.5

Calculator.greet()


Number = Calculator(2)
print("Square: ", Number.Square())
print("Cube: ", Number.Cube())
print("Root: ", Number.Root())