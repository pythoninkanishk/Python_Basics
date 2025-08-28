# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’. 

try :
 a = int(input("Enter Numerator: "))
 b = int(input("Enter Denominator: "))
 if b == 0:
    raise ZeroDivisionError("Infinite")
except Exception as e:
   print(e)
