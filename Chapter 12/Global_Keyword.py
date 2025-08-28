# ‘global’ keyword is used to modify the variable outside of the current scope. 

A = 10

def MyFunc():
    global A
    A = 19
    print(A)

MyFunc()
print(A)

# The Global Keyword made the "A" Variable inside the function global.

