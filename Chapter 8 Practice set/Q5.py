# 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3

def pattern():
    n = int(input("Enter Your Number: "))
    for i in range(n,0,-1):
      print("*"*i)
pattern()

