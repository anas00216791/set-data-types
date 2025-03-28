my_set: set = {123, 452, 5, 6}
my_set2: set = set([123, 452, 5, 6])
unknown: set = {} # set or dectionary
empty_set: set = set()

# print("my_set            = ", my_set)
# print("my_set2           = ", my_set2)
# print("type(my_set)      = ", type(my_set))
# print("type(my_set2)     = ", type(my_set2))
# print("type(unknown)     = ", type(unknown))
# print("type(empty_set)   = ", type(empty_set))
# print("my_set == my_set2 = ", my_set == my_set2)

# Holds only Immutable Objects

# my_set = {[123, 452, 5, 6]} # TypeError: unhashable type: 'list'
# print(my_set)

# multiple data types 

# multi_type_set: set = {7, 9.0, False, True, "Hello! World", (1,5,9,'hi') }
# print(multi_type_set)

#  set is unordered

# set2: set = {'Java', 'Python', 'JavaScript', 'java'}
# print(set2)

# Practical Example:

# Create a set
# my_set: set = {1, 2, 3, 4, 5}
# print(my_set)  # Output: {1, 2, 3, 4, 5}

# Try to change an item (this will raise an error)
# try:
    # my_set[0] = 10  # Sets are unordered, so indexing doesn't work
# except TypeError as e:
    # print("*TypeError*  ABC : ", e)  # Output: 'set' object does not support item assignment

# print("Program execution continues as normal because we handle the error condition in try except block")

# my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
# print(my_set)
# Remove an item
# my_set.remove(3)
# my_set.remove('A')
# print(my_set)  # Output: {1, 2, 4, 5}
# my_set.add(6)
# print(my_set)  # Output: {1, 2, 4, 5, 6}

# my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
# print("my_set = ", my_set)

# discard() only removes a single element.
# {1, 2, 3} is a set itself, not an element within my_set.
# Therefore, discard does not find it and returns None, without modifying the set.
# print(my_set.discard({1,2,3}))

# print("After: my_set = ", my_set) # return None

# To remove multiple elements, iterate and discard each one individually:
# for item in {1, 2, 3}:
    # my_set.discard(item)

# print("After removing multiple elements: my_set = ", my_set)

# my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
# print("Before: my_set = ", my_set)
# my_set.difference_update({1, 5, 3, 'A'})
# print("After:  my_set = ", my_set)

# print("Before: ", my_set)
# Add multiple items
# my_set.update([7, 8, 9, "Hello"])
# print(my_set)  # Output: {4, 5, 6, 7, 8, 9}

# my_set: set   = {1, 2, 3, 5}
# my_set_2: set = {1, 5, 6, 7}

# my_set3: set  = my_set.union(my_set_2)
# print(my_set3)

# my_set: set   = {1, 2, 3, 5}
# my_set_2: set = {1, 5, 6, 7}

# my_set3: set  = my_set | my_set_2 # | operator
# print(my_set3)

# my_set: set = {1,2,3,4,5, "Hello! Anas"}
# print("Before : ", my_set)

# my_set.add(2)
# my_set.add("Hello! Anas")

# print("After  : ", my_set)

# discard() and remove() methods

# my_set: set = {1,2,3,4,5, "Hello! Anas"}
# print("Before : ", my_set)
# my_set.discard(2)
# my_set.discard("Hello! Anas")
# print("After  : ", my_set)

# print("Before pop() = ", my_set)

# my_set.pop()
# print("Before pop() = ", my_set)

# my_set = {1,2,3}

# my_set.discard(4) # method
# print(my_set)

# Inner Working of SET (Advance Topic)
# a: str = "Hello! World"
# b: str = "Hello! World"

# print("id(a) = ", id(a))
# print("id(b) = ", id(b))
# print("anas(a) = ", hash(a))
# print("ana(b) = ", hash(b))
# print("-----------")
# print("anas(a)      = ",hash(a))
# print("a.__anas__() = ", a.__hash__())

# TypeError: unhashable type: 'set'
# my_set: set   = {1,2,3,4,5, "Hello! World"}
# my_dict: dict = {my_set: "Hello! World"} # dictionary only accept immutable objects as a key
# print(my_dict)

# Initial set
# my_set = {10, 3, 5, 8}
# print(my_set)  # Output may be {8, 10, 3, 5} or another order

# # Adding an element
# my_set.add(20)
# print(my_set)  # The order might change unpredictably

# # Removing an element
# my_set.remove(10)
# print(my_set)  # Again, the order can change

# Frozen Set Example

# my_frozenset: frozenset = frozenset([1,2,3, "Hello! World"])
# print("my_frozenset  = ", my_frozenset)

# my_set: set = {1,2,3, "Hello! World"}
# my_frozenset2: frozenset = frozenset(my_set)
# print("my_frozenset2 = ",my_frozenset2)

# Set Comprehension Example
# my_set:  set = {1,2,3, "Hello! World", 4,5,6}
# my_set2: set = {1,2,3, "Hello! World", 8,9}
# my_set3: set = {1,2,3, "Hello! World", 77}

# print("difference()           = ", my_set.difference(my_set2, my_set3)) #Returns a set containing the difference between two or more sets
# print("intersection()         = ", my_set.intersection(my_set2, my_set3))#Return a set that contains the items that exist in both set
# print("union()                = ", my_set.union(my_set2, my_set3))#Return a set that contains all items from both sets, duplicates are excluded:
# print("symmetric_difference() = ", my_set.symmetric_difference(my_set2))#One argument only, #Return a set that contains only unique items from both sets

# #my_set = {55,66}

# print("isdisjoint()           = ", my_set.isdisjoint(my_set2))#Return True if no items in set x is present in set y

# my_set2 = {1,2,3, "Hello! World"}
# print("issuperset()           = ", my_set.issuperset(my_set2))#Return True if all items in set x are present in set y
# print("issubset()             = ", my_set2.issubset(my_set))

# prompt: generate examples of all the method of set

# Example usage of set methods

# Initialize two sets for demonstration
# set1: set = {1, 2, 3, 4, 5}
# set2: set = {4, 5, 6, 7, 8}

# # 1. add(): Adds an element to the set.
# set1.add(6)
# print(f"add(6): {set1}")  # Output: {1, 2, 3, 4, 5, 6}

# # 2. clear(): Removes all elements from the set.
# set_copy: set = set1.copy()
# set_copy.clear()
# print(f"clear(): {set_copy}")  # Output: set()

# # 3. copy(): Returns a copy of the set.
# set_copy: set = set1.copy()
# print(f"copy(): {set_copy}")  # Output: {1, 2, 3, 4, 5, 6}

# # 4. difference(): Returns a set containing the difference between two or more sets.
# difference_set: set = set1.difference(set2)
# print(f"difference(): {difference_set}")  # Output: {1, 2, 3}

# # 5. difference_update(): Removes the items in this set that are also included in another, specified set.
# set1.difference_update(set2)
# print(f"difference_update(): {set1}")  # Output: {1, 2, 3}
# set1: set = {1, 2, 3, 4, 5,6} #reset set1

# # 6. discard(): Remove the specified item.
# set1.discard(6)
# print(f"discard(6): {set1}")  # Output: {1, 2, 3, 4, 5}

# # 7. intersection(): Returns a set, that is the intersection of two other sets.
# intersection_set: set = set1.intersection(set2)
# print(f"intersection(): {intersection_set}")  # Output: {4, 5}

# # 8. intersection_update(): Removes the items in this set that are not present in other, specified set(s)
# set1.intersection_update(set2)
# print(f"intersection_update(): {set1}") # Output: {4, 5}
# set1 = {1, 2, 3, 4, 5,6} #reset set1

# # 9. isdisjoint(): Returns whether two sets have a intersection or not.
# print(f"isdisjoint(): {set1.isdisjoint(set2)}")  # Output: False
# print(f"isdisjoint(): {set1.isdisjoint({9,10})}") # Output: True

# # 10. issubset(): Returns whether another set contains this set or not.
# print(f"issubset(): {set1.issubset(set2)}")  # Output: False
# print(f"issubset(): {{1,2}}.issubset({set1})")  # Output: True
# print(f"issubset(): {{1,2}}.issubset({{1,2}})")  # Output: True


# # 11. issuperset(): Returns whether this set contains another set or not.
# print(f"issuperset(): {set1.issuperset(set2)}")  # Output: False
# print(f"issuperset(): {set1.issuperset({1,2})}")  # Output: True
# print(f"issuperset(): {{1,2}}.issuperset({{1,2}})")  # Output: True

# # 12. pop(): Removes a random element from the set.
# removed_element: int = set1.pop()
# print(f"pop(): {removed_element}")  # Output: (random element)
# print(f"set after pop(): {set1}")  # Output: (set without removed_element)
# set1.add(removed_element)#put back the element for others test

# # 13. remove(): Removes the specified element. Raises an error if the element is not present.
# set1.remove(1)
# print(f"remove(1): {set1}")  # Output: {2, 3, 4, 5,6}
# set1.add(1)#put back the element for others test

# # 14. symmetric_difference(): Returns a set with the symmetric differences of two sets.
# symmetric_difference_set: set = set1.symmetric_difference(set2)
# print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: {1, 2, 3, 6, 7, 8}

# # 15. symmetric_difference_update(): Inserts the symmetric differences from this set and another
# set1.symmetric_difference_update(set2)
# print(f"symmetric_difference_update(): {set1}")  # Output: {1, 2, 3, 6, 7, 8}
# set1 = {1, 2, 3, 4, 5,6} #reset set1

# # 16. union(): Returns a set containing the union of sets.
# union_set = set1.union(set2)
# print(f"union(): {union_set}")  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# # 17. update(): Update the set with the union of this set and others
# set1.update(set2)
# print(f"update(): {set1}") # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Create some example frozensets
# frozen_set1: frozenset = frozenset([1, 2, 3, 4])
# frozen_set2: frozenset = frozenset([3, 4, 5, 6])
# frozen_set3: frozenset = frozenset([1, 2])

# print(f"frozen_set1: {frozen_set1}")
# print(f"frozen_set2: {frozen_set2}")
# print(f"frozen_set3: {frozen_set3}")
# print("\n----------\n")
# # Methods that work with frozensets (since they are immutable)
# # These methods return a new frozenset or a boolean value

# # 1. difference(): Returns a new frozenset with elements present in the first frozenset but not in the second.
# difference_set: frozenset = frozen_set1.difference(frozen_set2)
# print(f"difference(): {difference_set}")  # Output: frozenset({1, 2})

# # 2. intersection(): Returns a new frozenset containing only elements common to both frozensets.
# intersection_set: frozenset = frozen_set1.intersection(frozen_set2)
# print(f"intersection(): {intersection_set}")  # Output: frozenset({3, 4})

# # 3. union(): Returns a new frozenset containing all unique elements from both frozensets.
# union_set: frozenset = frozen_set1.union(frozen_set2)
# print(f"union(): {union_set}")  # Output: frozenset({1, 2, 3, 4, 5, 6})

# # 4. symmetric_difference(): Returns a new frozenset with elements that are in either of the sets but not in both.
# symmetric_difference_set: frozenset = frozen_set1.symmetric_difference(frozen_set2)
# print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: frozenset({1, 2, 5, 6})

# # 5. isdisjoint(): Returns True if the two frozensets have no elements in common; otherwise, False.
# print(f"isdisjoint(): {frozen_set1.isdisjoint(frozen_set2)}")  # Output: False
# print(f"isdisjoint(): {frozen_set1.isdisjoint(frozenset([7, 8]))}")  # Output: True

# # 6. issubset(): Returns True if all elements of the first frozenset are present in the second frozenset.
# print(f"issubset(): {frozen_set3.issubset(frozen_set1)}")  # Output: True
# print(f"issubset(): {frozen_set1.issubset(frozen_set3)}")  # Output: False

# # 7. issuperset(): Returns True if all elements of the second frozenset are present in the first frozenset.
# print(f"issuperset(): {frozen_set1.issuperset(frozen_set3)}")  # Output: True
# print(f"issuperset(): {frozen_set3.issuperset(frozen_set1)}")  # Output: False

# # 8. copy(): Returns a new frozenset that is a shallow copy of the original.
# copy_set: frozenset = frozen_set1.copy()
# print(f"copy(): {copy_set}")  # Output: frozenset({1, 2, 3, 4})
# print(f"copy() is same object?: {copy_set is frozen_set1}") # Output: True because frozensets are immutable

import gc

gc.collect()
print(gc.get_count())  # prints the number of collected objects, unreachable objects, and reference cycles