# 6. Write a python function which converts inches to cms. 

def inch_to_CentConvert():
    inc = int(input("Enter Values in Inches: "))
    return inc*2.54
Result = inch_to_CentConvert()
print(f"In centimeters:{Result}")