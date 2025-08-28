# MAP EXAMPLE
l = [3,5,9,21,8]

square = lambda x:x*x
Mapfunc = map(square, l)
print(list(Mapfunc))

#FILTER EXAMPLE 
def even(n):
    if (n%2== 0):
        return True
    else:
        return False

OnlyEven = filter(even, l)
print(list(OnlyEven))

#REDUCE EXAMPLE 
from functools import reduce
def sum(a,b):
    return a+b
print(reduce(sum,l))