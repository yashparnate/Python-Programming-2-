# Creating a tuple
tup = (10, 20, 30, 40, 50, 20)

print("Original Tuple:", tup)

# 1. Access element
print("First element:", tup[0])

# 2. Negative indexing
print("Last element:", tup[-1])

# 3. Slicing
print("Slice (1 to 4):", tup[1:4])

# 4. Length of tuple
print("Length of tuple:", len(tup))

# 5. Count occurrences
print("Count of 20:", tup.count(20))

# 6. Find index of element
print("Index of 30:", tup.index(30))

# 7. Tuple concatenation
tup2 = (60, 70)
new_tuple = tup + tup2
print("After concatenation:", new_tuple)

# 8. Tuple repetition
repeat_tuple = tup * 2
print("After repetition:", repeat_tuple)

# 9. Check membership
print("Is 40 in tuple?", 40 in tup)

# 10. Iterating through tuple
print("Elements in tuple:")
for i in tup:
    print(i)

# 11. Convert tuple to list (to modify)
list1 = list(tup)
list1.append(100)
print("Tuple converted to list and modified:", list1)

# 12. Convert list back to tuple
tup3 = tuple(list1)
print("List converted back to tuple:", tup3)