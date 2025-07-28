""" 4. Write a python program to print the contents of a directory using the os module.  Search online for the function which does that."""
import os

# Specify the directory path (use '.' for current directory)
directory_path = 'D:\Python'

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)