# function with argument (Intro to return)

def Sum():
    a = int(input("Enter Your Number: "))
    b = int(input("Enter Your Number: "))
    Addition = a + b
    return Addition
    
a = Sum()
print(f"The sum of the given number is {a}")

# Return helps us store the Function if return is not used the function when stored will give none as the answer

