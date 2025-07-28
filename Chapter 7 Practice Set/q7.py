# 7. Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3 
n = int(input("Enter Your Number: "))
for i in range(1,n+1):
    print(" "*(n),end=" ")
    print("*"*(2*i-1),end = " ")
    print(" ")
