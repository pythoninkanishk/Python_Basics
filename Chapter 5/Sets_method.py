Set = {1,2,4,5,6}

# Set.add(8)
# print(Set)
# This is used to add a single element to the set.

# Set.pop()
# This removes a random element from the set.
# print(Set)

# Set.remove(2)
# print(Set)
# This removes the specified element from the set.

# Set.clear()
# This removes all elements from the set.

Set2 = {1,2,3,4,5}

set3 = Set.union(Set2)
print(set3)
# This creates a new set that is the union of Set1 and Set2.

Set4 = Set.intersection(Set2)
print(Set4)
# This creates a new set that contains only the elements present in both Set and Set2.

Set5 = Set.difference(Set2)
print(Set5)
# This creates a new set with elements present in Set but not in Set2.

Set6 = Set.symmetric_difference(Set2)
print(Set6)
# This creates a new set with elements present in either Set or Set2 but not in both.

Set_copy = Set.copy()
print(Set_copy)
# This creates a shallow copy of the set.

is_subset = Set.issubset(Set2)
print(is_subset)
# This checks if all elements of Set are present in Set2.

is_superset = Set.issuperset(Set2)
print(is_superset)
# This checks if Set contains all elements of Set2.

is_disjoint = Set.isdisjoint(Set2)
print(is_disjoint)
# This checks if Set and Set2 have no elements in common.