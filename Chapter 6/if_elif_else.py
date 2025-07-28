Age = int(input("Enter your age: "))
if Age>= 18:
    print("you are eligible to vote")
elif Age< 0:
    print("Invalid age entered")
elif Age == 0:
    print("0 is not a valid age to vote")
else:
    print("you are not eligible to vote")

