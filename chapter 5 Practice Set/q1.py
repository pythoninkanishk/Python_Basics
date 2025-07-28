# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

hindi_to_english = {
    'Namaste': 'Hello',
    'Dhanyawad': 'Thank you',
    'Kripya': 'Please',}

Hindi_to_english_dictionary = input('enter the word  you want to translate: ')

print("The English translation of", Hindi_to_english_dictionary, "is:", hindi_to_english.get(Hindi_to_english_dictionary, "Word not found"))