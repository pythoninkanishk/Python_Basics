# 2. Write a program to print third, fifth and seventh element from a list using enumerate 
# function. 
list1 = [1,34,8,90,8,7,5,8,12,78]
for i, item in enumerate(list1):
    if i == 3 or i == 5 or i == 7:
         print(i,item)