'''
Snake =1 
Water = -1
Gun = 0
'''
import random
Your_Score = 0
Computer_Score = 0
def game():
    global Your_Score, Computer_Score
    computer = random.choice([1,0,-1])
    Youstr = (input("Enter Your Choice(s: Snake, w: Water, g: Gun):  "))     
    YouDict ={"s": 1, "w":0, "g":-1}
    DictLst= {1:"Snake", 0:"Water", -1:"Gun"}
    if Youstr not in YouDict:
       print("Invalid Choice! please choose b/w s, w or g")
       return
    You =YouDict[Youstr]

    print(f"You chose {DictLst[You]} \nComputer Chose {DictLst[computer]}")

    if You==computer:
        print("Thats A Tie")
    else:
        if computer == 1 and You == 0:
           print("You Lost :(")
           Computer_Score = 1
        elif computer == 1 and You == -1:
           print("You Won :)")
           Your_Score += 1
        elif computer == 0 and You == 1:
           print("You Won :)")
           Your_Score += 1
        elif computer == 0 and You == -1:
           print("You Lost :(")
           Computer_Score += 1
        elif computer == -1 and You == 1:
           print("You Lost :(")
           Computer_Score += 1
        elif computer == -1 and You == 0:
           print("You Won :)")
           Your_Score += 1  
        else:
           print("Something Went Wrong")   
    print(f"Score: \nYour Score:{Your_Score} \nComputer's Score:{Computer_Score} ")
game()
game()
game()