try:
    A = int(input("Enter Your Number: " ))
    print(A)
except Exception as a:
    print(a)
print("Thank You")


#This sends error messages when exceptions are made in the given code without crashing it.

# We can also specify the exception to catch like below:
try:
    Z = int(input("Enter A Number: "))
    print(Z)
except ValueError as v:
    print(v)
print("Thank You")
# or
try:
    H = int(input("Enter A Number For Numerator: "))
    D = int(input("Enter A Number for Denominator: "))
    print(H/D)
except ZeroDivisionError as E:
    print(E)
print("Thank You")