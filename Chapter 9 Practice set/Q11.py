# 11. Write a python program to rename a file to “renamed_by_ python.txt. 
import os

Old_file = "Files.txt"
New_Name = "renamed_by python.txt"
os.replace(Old_file, New_Name)