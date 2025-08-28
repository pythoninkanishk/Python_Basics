try: 
    N = int(input("Enter Your Number: "))
except Exception as e:
    print(e)
else:
    print(f"The number you entered is {N}")

#the use of else with try is to run a process if the code is executed properly without exceptions

