# Walrus Operator
if n := len([1,2,4,5,0])<3:
    print('The Length of the given list is less than 3')
elif n := len([1,2,4,5,0])==3:
    print('The length of the given list is 3')
else :
    print('The length of the given list is more than 3')

# Useful in loops or conditions where you want to assign and check in one go
