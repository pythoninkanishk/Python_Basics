# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.
class complexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
         return f"{self.a}+{self.b}i"
    def __add__(self, other):
        return complexNum({self.a + other.a}, {self.b + other.b})
    def __mul__(self, other):
        real = {self.a * other.a - self.b * other.b}
        Imag = {self.a * other.b + self.b * other.a}
        return complexNum(real, Imag)
x = complexNum(1,4)
z = complexNum(2,3)
print(x + z)
print(x*z)



