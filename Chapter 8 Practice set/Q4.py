# 4. Write a recursive function to calculate the sum of first n natural numbers. 
def sumofnum(n):
    if n == 1:
        return 1
    else:
       return n+sumofnum(n-1)
Number = sumofnum(int(input("Enter the number: ")))
print(f"The Sum of numbers till the given no is {Number}")