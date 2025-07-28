# 8. Write a python function to print multiplication table of a given number.

def Table():
   n = int(input("Enter the number to get the table of: "))
   i = 1
   while i<=10:
      print(f"{n} X {i} = {n*i}")
      i += 1
Table()