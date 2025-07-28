L1 = ["kanishk", "manthan", 0, 0.10]
L1.append("new_item") # Appending a new item to the end of the list
print(L1)

l2 = [1,2,3,6,5,43, 11, 0.10]
l2.sort() # Sorting the list in ascending order
print(l2)

l3 = [1,2,3,6,5,43, 11, 0.10]
l3.reverse() # Reversing the order of the list
print(l3)

l4 = [1,2,3,6,5,43, 11, 0.10]
l4.insert(2, "random numbers hai") # Inserting an item at index 2
print(l4)

l5 = [1,2,3,6,5,43, 11, 0.10]
l5.pop(3) # Removing the last item from the list
print(l5)

l6 = [1,2,3,6,5,43, 11, 0.10]
l6.remove(3) # Removing the first occurrence of the item 3
print(l6)

l7 = [1,2,3,6,5,43, 11, 0.10]
l7.clear() # Clearing all items from the list
print(l7) # This will print an empty list

l8 = [1,2,3,6,5,43, 11, 0.10]
l8.count(2) # Creating a shallow copy of the list
print(l8) # This will print the original list