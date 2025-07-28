# 2. Write a python program using function to convert Celsius to Fahrenheit.
def Cel_to_fahr_converter():
    C = int(input("Enter Temperature in Celsius: "))
    Fahrenheit = (9/5*C) + 32
    return Fahrenheit 
Converter = Cel_to_fahr_converter()
print(f"The Given temperature is {Converter} in fahrenheit")