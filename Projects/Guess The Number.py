import random
# Guess the Number
def GuessTheNumber():
 Computer = random.choice(range(1, 11))
 Attempts = 3
 for i in range(Attempts):
   You = int(input(f"[Attempts: {i+1}]Enter Your Guess (Out Of 10): "))
   if You>Computer:
    print("Number is too high :(")
   elif You<Computer:
    print("Number is too Low :(")
   else:
    print("Congratulations, You Won!!!")
    return
 print(f"You're Out Of Attempts 😒, the correct answer is {Computer}") 
GuessTheNumber() 
