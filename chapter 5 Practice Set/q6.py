# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

friends_languages = {}

friends_languages['Alice'] = input("Alice, enter your favorite language: ")
friends_languages['Bob'] = input("Bob, enter your favorite language: ")
friends_languages['Charlie'] = input("Charlie, enter your favorite language: ")
friends_languages['Diana'] = input("Diana, enter your favorite language: ")

print("Friends' favorite languages:", friends_languages)
# This code creates a dictionary where each friend's name is the key and their favorite language is the 