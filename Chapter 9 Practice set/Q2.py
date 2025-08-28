# 2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score. 
import random
def game():
    Random_NoGenerator = random.randint(1,61)
    print("Generated No: ",Random_NoGenerator)
    try:
        with open("Hi-Score.txt", "r") as f:
          content = f.read()
          if content.strip() == "":
             High_Score = 0
          else:
             High_Score = int(content)
    except FileNotFoundError:
        High_Score = 0
         
    if Random_NoGenerator> High_Score:
        print("Congratulations You Made a new High Score")
        with open("Hi-Score.txt", "w") as f:
            hS = f.write(str(Random_NoGenerator))
    else:
        print("please try again to beat the high score")
    return Random_NoGenerator  
Score = game()
print(f"Your Score:{Score}")
    
