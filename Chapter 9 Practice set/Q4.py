# 4. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.

def updatefile():
    with open("Donkey.txt")as f:
       content = f.read()
    content = content.replace("Donkey", "#####")
    with open("Donkey.txt", "w") as f:
       f.write(content)

updatefile()