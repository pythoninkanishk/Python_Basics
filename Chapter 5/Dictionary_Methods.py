# Dictionary Methods.py
DICTIONARY = {"Harry": 100, "Rohan": 200, "Hammad": 300, "Badman": 400}

print(DICTIONARY.items())

  # Returns a view object that displays a list of dictionary's key-value tuple pairs

print(DICTIONARY.keys())
  # Returns a view object that displays a list of all the keys in the dictionary

print(DICTIONARY.values())
 # Returns a view object that displays a list of all the values in the dictionary

(DICTIONARY.update({"Shivam": 500, "Kanishk": 600}))
print(DICTIONARY)
# Returns None and updates the dictionary with the specified key-value pairs

print(DICTIONARY.get("Harry"))
# Returns the value for the specified key if it exists, otherwise returns None

print(DICTIONARY.pop("Rohan"))
# Removes the specified key and returns the corresponding value

print(DICTIONARY)
# Shows the dictionary after removing "Rohan"

print(DICTIONARY.popitem())
# Removes and returns the last inserted key-value pair as a tuple

print(DICTIONARY)
# Shows the dictionary after popitem()

print(DICTIONARY.setdefault("Aman", 700))
# Returns the value of "Aman" if it exists, otherwise inserts "Aman" with value 700

print(DICTIONARY)
# Shows the dictionary after setdefault()

DICTIONARY.clear()
print(DICTIONARY)
# Removes all items from the dictionary, resulting in an empty dictionary