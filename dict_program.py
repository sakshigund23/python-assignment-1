# 4.1 Create and access dictionary elements
student = {
    "name": "Sakshi Gund",
    "roll_no": 16,
    "course": "CSE"
}

print("Student Dictionary:", student)
print("Name:", student["name"])
print("Course:", student["course"])

# 4.2 Update Dictionary
student["roll_no"] = 1055         # update value
student["college"] = "MIT-ADT"    # add new key-value pair
print("After Updating Dictionary:", student)

# 4.3 Removing Elements
student.pop("course")
print("After Removing 'course':", student)

# 4.4 Merging Dictionaries
extra_info = {
    "year": "First Year",
    "city": "Pune"
}

merged_dict = student | extra_info   # Python 3.9+
print("Merged Dictionary:", merged_dict)