# 9. Write a program to find out whether a file is identical & matches the content of 
# another file. 
with open("This.txt") as f:
    Content = f.read()
with open("This(2).txt") as g:
    Content2 = g.read()
if Content == Content2:
    print("The Content in both the files is same")
else:
    print("The Content in both the files is not the same")