# TYPE OF FILES. 
# There are 2 types of files: 
# 1. Text files (.txt, .c, etc) 
# 2. Binary files (.jpg, .dat, etc)

#Opening a file 
file = open("file.txt", "a")
text = file.write(" Kanishk is the goat") #Append helps to add text to the given line it can be done by using "a"
file.close
# similar to append 'w' is used to write, 'r'is used to read   
 