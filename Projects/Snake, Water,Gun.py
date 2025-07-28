import random
'''
Snake =1 
Water = -1
Gun = 0
'''

Computer = random.choice([1,0,-1])
Youstr = (input("Enter Your Choice: "))
Dict = {"s":1, "w":-1, "g":0}
RevDic = {1:"Snake", 0:"Gun", -1 :"Water"}

You = Dict[Youstr]

print(f"You Chose {RevDic[You]}. \nComputer Chose {RevDic[Computer]}.")

if(Computer == You):
    print("ITS A TIE!")
else:
    if(Computer == 1 and You == -1):
        print("You Win!!")
    elif(Computer == 1 and You == 0):
        print("You Lost :(")
    elif(Computer == -1 and You == 1):
        print("You Win!!")
    elif(Computer == -1 and You == 0):
        print("You Lost :(")
    elif(Computer == 0 and You == 1):
        print("You Lost :(")
    elif(Computer == 0 and You == -1):
        print("You Win!!")
    else:
        print("Something Went Wrong :/")