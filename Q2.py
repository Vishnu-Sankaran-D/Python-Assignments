# Student Marks Analysis

# 1. Create a list and convert it into a tuple
marks = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks)

# 2. Display collections and data types
print("List:", marks)
print("List Data Type:", type(marks))

print("Tuple:", marks_tuple)
print("Tuple Data Type:", type(marks_tuple))

# 3. Find highest and lowest marks
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

# 4. Count students who scored at least 40
count = (marks[0] >= 40) + (marks[1] >= 40) + (marks[2] >= 40) + (marks[3] >= 40) + (marks[4] >= 40)
print("Students Scoring at Least 40:", count)

# 5. Check valid mark range
valid = all(0 <= mark <= 100 for mark in marks)
print("All Marks Are Valid:", valid)

# 6. Modify list element
marks[0] = 85
print("Modified List:", marks)

# Try modifying tuple
# marks_tuple[0] = 85

# Observation:
# List is mutable, so its elements can be changed.
# Tuple is immutable, so its elements cannot be changed.

print("Original Tuple:", marks_tuple)
