# 8. Write a program to make a copy of a text file “this.txt”
# 
with open("This.txt") as f:
    Content = f.read()
with open("This(2).txt", "w") as f:
    f.write(Content)