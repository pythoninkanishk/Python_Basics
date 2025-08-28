# 10. Write a program to wipe out the content of a file using python. 
def Clear():
   with open("Files.txt") as f:
    Content = f.read()
   Content2 = Content.replace(Content, " ")
   with open("Files.txt", "w") as f:
     f.write(Content2)
Clear()