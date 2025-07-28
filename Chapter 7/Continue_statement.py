# 'Continue’ is used to stop the current iteration of the loop and continue with the next 
# one. It instructs the Program to “skip this iteration”.


for i in range (1,52):
    if i== 2:
        continue
    #print(i)

#to leave a string from the given list
List = ["kanishk", "Goat", '', "felicia" ]
for WORD in List:
    if WORD == "":
        continue
    print("Words from the list: ", WORD)



