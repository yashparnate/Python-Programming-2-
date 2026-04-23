# Create a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# 1. Append (Add element at end)
numbers.append(60)
print("After append:", numbers)

# 2. Insert (Add element at specific position)
numbers.insert(2, 25)
print("After insert:", numbers)

# 3. Extend (Add another list)
numbers.extend([70, 80])
print("After extend:", numbers)

# 4. Remove (Remove specific value)
numbers.remove(40)
print("After remove:", numbers)

# 5. Pop (Remove element using index)
numbers.pop(3)
print("After pop:", numbers)

# 6. Index (Find position of element)
print("Index of 30:", numbers.index(30))

# 7. Count (Count occurrences)
numbers.append(20)
print("Count of 20:", numbers.count(20))

# 8. Sort (Sort list)
numbers.sort()
print("Sorted List:", numbers)

# 9. Reverse
numbers.reverse()
print("Reversed List:", numbers)

# 10. Copy
new_list = numbers.copy()
print("Copied List:", new_list)

# 11. Length of list
print("Length of list:", len(numbers))

# 12. Access element
print("First element:", numbers[0])

# 13. Slicing
print("Slice (1 to 4):", numbers[1:4])

# 14. Clear list
numbers.clear()
print("After clear:", numbers)