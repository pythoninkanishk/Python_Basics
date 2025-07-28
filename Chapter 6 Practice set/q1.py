# 1. Write a program to find the greatest of four numbers entered by the user. 

NO_1 = int(input("FIRST NUMBER: "))
NO_2 = int(input("SECOND NUMBER: "))
NO_3 = int(input("THIRD NUMBER: "))
NO_4 = int(input("FOURTH NUMBER: "))

if (NO_1>NO_2)and(NO_1>NO_3)and(NO_1>NO_4):
    print("FIRST NO IS THE GREATEST NO")
if (NO_2>NO_1)and(NO_2>NO_3)and(NO_2>NO_4):
    print("SECOND NO IS THE GREATEST NO")
if (NO_3>NO_1)and(NO_3>NO_2)and(NO_3>NO_4):
    print("THIRD NO IS THE GREATEST NO")
if (NO_4>NO_1)and(NO_4>NO_2)and(NO_4>NO_3):
    print("FOURTH NO IS THE GREATEST NO")

    