# 8. If languages of two friends are same; what will happen to the program in problem 
# 6? 

friends_languages = {}

friends_languages['Alice'] = input("Alice, enter your favorite language: ")
friends_languages['Bob'] = input("Bob, enter your favorite language: ")
friends_languages['Charlie'] = input("Charlie, enter your favorite language: ")
friends_languages['Diana'] = input("Diana, enter your favorite language: ")

print("Friends' favorite languages:", friends_languages)

# If two friends have the same favorite language, both entries will still be stored in the dictionary. The values can be the same, but the keys (friends' names) are unique, so there will be no conflict.