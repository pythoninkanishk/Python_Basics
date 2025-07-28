    # 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50 => F 
Marks = float(input("Enter Your Marks: "))
if 100>=Marks>=90:
    print("Grade: A")
elif 90>=Marks>=80:
    print("Grade: A")
elif 80>=Marks>=70:
    print("Grade: A")
elif 70>=Marks>=60:
    print("Grade: A")
elif 60>=Marks>=50:
    print("Grade: A")
elif 50>=Marks>=0:
    print("Grade: A")
else:
    print("please add valid no b/w the range 0 to 100")

