# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

Marks_subject_1 =int(input("Subject 1 marks: "))
Marks_subject_2 =int(input("Subject 2 marks: "))
Marks_subject_3 =int(input("Subject 3 marks: "))

Percentage_of_first_subject = int(Marks_subject_1/80*100)
Percentage_of_second_subject = int(Marks_subject_2/80*100)
Percentage_of_third_subject = int(Marks_subject_3/80*100)

if(Percentage_of_first_subject>33)and(Percentage_of_second_subject>33)and(Percentage_of_third_subject>33)and((Marks_subject_1+Marks_subject_2+Marks_subject_3)/240*100>40):
    print("Student has passed")
else:
    print("Student has failed")

    
