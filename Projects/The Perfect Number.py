import random
n = random.randint(1,100)
a = 0
guesses = 0
while n != a:
    a = int(input("Guess The Number: "))
    if (a>n):
        print("Your number is too high")
        guesses += 1
    elif (a<n):
        print("Your number is too low")
        guesses += 1
print(f"You Guessed The Perfect Number {n} in {guesses} Guesses")