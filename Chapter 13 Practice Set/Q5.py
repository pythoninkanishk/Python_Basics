# 5. Write a program to find the maximum of the numbers in a list using the reduce 
# function. 

from functools import reduce 

l = [290 , 45, 680, 90, 65, 30, 450, 900 ,987]

def Greatest(a,b):
    if (a>b):
        return a 
    else:
        return b 
    
print(reduce(Greatest, l))