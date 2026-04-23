student = {
    "name": "Rahul",
    "age": 18,
    "course": "Python",
    "marks": 85
}

print("Original Dictionary:", student)

# 1. Access value
print("Name:", student["name"])

# 2. Using get()
print("Age:", student.get("age"))

# 3. Add new key-value pair
student["city"] = "Pune"
print("After adding city:", student)

# 4. Update value
student["marks"] = 90
print("After updating marks:", student)

# 5. Update multiple values
student.update({"age": 19, "course": "Data Science"})
print("After update():", student)

# 6. Remove item using pop()
student.pop("city")
print("After pop:", student)

# 7. Remove last inserted item
student.popitem()
print("After popitem:", student)

# 8. Keys of dictionary
print("Keys:", student.keys())

# 9. Values of dictionary
print("Values:", student.values())

# 10. Key-value pairs
print("Items:", student.items())

# 11. Check key existence
print("Is 'name' in dictionary?", "name" in student)

# 12. Length of dictionary
print("Length:", len(student))

# 13. Copy dictionary
new_student = student.copy()
print("Copied Dictionary:", new_student)

# 14. Loop through dictionary
print("Dictionary elements:")
for key, value in student.items():
    print(key, ":", value)

# 15. Clear dictionary
student.clear()
print("After clear:", student)