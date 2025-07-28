# 7. If the names of 2 friends are same; what will happen to the program in problem 
# 6? 

# If the names of two friends are the same in problem 6, the second entry will overwrite the first one in the dictionary. This is because dictionary keys must be unique, and if a key is repeated, the last value assigned to that key will be retained.
friends_languages = {}

friends_languages['Alice'] = input("Alice, enter your favorite language: ")
friends_languages['Alice'] = input("Alice, enter your favorite language: ")
friends_languages['Charlie'] = input("Charlie, enter your favorite language: ")
friends_languages['Diana'] = input("Diana, enter your favorite language: ")

print("Friends' favorite languages:", friends_languages)