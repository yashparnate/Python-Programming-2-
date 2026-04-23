# Creating a set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("Set 1:", set1)
print("Set 2:", set2)

# 1. Add element
set1.add(10)
print("After add:", set1)

# 2. Update set (add multiple elements)
set1.update([11, 12])
print("After update:", set1)

# 3. Remove element
set1.remove(2)
print("After remove:", set1)

# 4. Discard element
set1.discard(3)
print("After discard:", set1)

# 5. Pop element
set1.pop()
print("After pop:", set1)

# 6. Union
print("Union:", set1.union(set2))

# 7. Intersection
print("Intersection:", set1.intersection(set2))

# 8. Difference
print("Difference (set1 - set2):", set1.difference(set2))

# 9. Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 10. Subset check
print("Is subset:", set1.issubset(set2))

# 11. Superset check
print("Is superset:", set1.issuperset(set2))

# 12. Copy set
new_set = set1.copy()
print("Copied Set:", new_set)

# 13. Length of set
print("Length of set1:", len(set1))

# 14. Clear set
set1.clear()
print("After clear:", set1)