#Type function helps us to find the type of a variable
#It can be used to check the type of any variable

A = 1
t = type (A)
print(t) #This will print <class 'int'> indicating that A is an integer variable

B = 2.3
T = type (B)
print(T) #This will print <class 'float'> indicating that B is a floating point variable

C = "Hello"
X = type (C)
print(X) #This will print <class 'str'> indicating that C is a string variable

D = "21.4"
Y = type (D)
print(Y) 
#This will print <class 'str'> indicating that D is a string variable but it can be converted to a float using float(D)

E = "23.4"
float(E)
Z = type (E)
print(Z)