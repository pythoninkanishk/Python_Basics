# Strings Slicing
# This code demonstrates how to slice strings in Python.
name = "Kanishk"
name2 = name[1:3]


print(name[-4:-1])
print(name[3:6])

#advanced slicing
print(name[:3]) #here we are slicing from the start to index 3 as when no number is given it takes the start i.e index 0 (name[0:3])
print(name[3:]) #here we are slicing from index 3 to the end of the string as when no number is given it takes the end of the string ie index -1 (name[3:-1])

print(name[1:6:4])# here we are slicing from index 1 to index 6 with a step of 4
print(name[::2]) # here we are slicing the string with a step of 2  \