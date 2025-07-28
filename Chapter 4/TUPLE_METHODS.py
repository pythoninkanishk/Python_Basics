A = (1, 2, 3, 3, 4, 5) # Creating a tuple with multiple elements

# Counting occurrences of an element in a tuple
print(A.count(3)) # Output: 2

# Using count() to get the number of times 2 appears
print(A.count(2)) # Output: 1

# Using index() with a start position
print(A.index(3, 2)) # Finds the index of 3 starting from position 2, Output: 3

# Handling ValueError with index()
try:
    print(A.index(10)) # 10 is not in the tuple, raises ValueError
except ValueError:
    print("10 is not found in the tuple.")
