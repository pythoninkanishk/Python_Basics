# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner. 

#score of 5 students out of 20

Score = []
Marks_of_first_kid = int(input("Enter the marks of first student: "))
Score.append(Marks_of_first_kid)
Marks_of_second_kid = int(input("Enter the marks of second student: "))
Score.append(Marks_of_second_kid)   
Marks_of_third_kid = int(input("Enter the marks of third student: "))
Score.append(Marks_of_third_kid)
Marks_of_fourth_kid = int(input("Enter the marks of fourth student: "))
Score.append(Marks_of_fourth_kid)
Marks_of_fifth_kid = int(input("Enter the marks of fifth student: "))
Score.append(Marks_of_fifth_kid)
Score.sort()
print("Sorted marks of students:", Score)