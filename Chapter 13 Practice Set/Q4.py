# 4. Write a program to filter a list of numbers which are divisible by 5. 

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def DivBy5(n):
    if (n%5 == 0):
        return True
    return False

Filter = filter(DivBy5 , l)
print(list(Filter))

