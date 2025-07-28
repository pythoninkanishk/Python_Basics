#LENGTH OF STRING
NAME = "kanishk Badmash"

print(len(NAME)) # This will print the length of the string NAME

#string.endswith() method
print(NAME.endswith("mash")) # This will check if the string ends with "mash" and return True or False

#string.count() method
print(NAME.count('a')) # This will count the number of occurrences of 'a' in the string NAME

#Capitalize the string (Make the first letter capital)
Capitalized_string = NAME.capitalize()
print(Capitalized_string) # This will print the string with the first letter capitalized

#string.find() method
print(NAME.find("Bad")) # This will find the substring "Bad" in NAME and return its starting index, or -1 if not found

#string.replace() method
GOAT = NAME.replace("Badmash", "LAADLA") #This will replace "Badmash" with "Bad" in the string NAME
print(GOAT) # This will print the modified string

#string.upper() method
print(NAME.upper()) # This will convert all characters in the string NAME to uppercase

#string.lower() method
print(NAME.lower()) # This will convert all characters in the string NAME to lowercase

#string.isalpha() method
print(NAME.isalpha()) # This will check if all characters in NAME are alphabetic (no spaces or numbers)

#string.isdigit() method
print(NAME.isdigit()) # This will check if all characters in NAME are digits

#string.strip() method
str_with_spaces = "   Hello World!   "
print(str_with_spaces.strip()) # This will remove leading and trailing spaces from the string

#string.split() method
print(NAME.split()) # This will split the string NAME into a list of words using spaces as separator

#string.startswith() method
print(NAME.startswith("kan")) # This will check if the string starts with "kan" and return True or False