# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

with open("poems.txt") as f:
    text = f.read()
    if "twinkle" in text:
        print("Twinkle is there in the file")
    else:
        print("Twinkle is not there in the file")

    