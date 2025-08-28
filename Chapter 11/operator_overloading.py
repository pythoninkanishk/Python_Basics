class math:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n
X = math(2)
M = math(3)

print(X + M)          

# p1+p2 # p1.__add__(p2) 
# p1-p2 # p1.__sub__(p2) 
# p1*p2 # p1.__mul__(p2) 
# p1/p2 # p1.__truediv__(p2) 
# p1//p2 # p1.__floordiv__(p2)