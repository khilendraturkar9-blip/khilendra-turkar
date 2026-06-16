list = ["apple", "banana", "mango", 
 "orange", "grapes"]

# Print first 3 fruits
print(list[0:3])

# Add "pineapple" at end
list.append("pineapple")
print(list)
# Remove "banana"
list.remove("banana")
print(list)
# Print final list
print(list)

# Create a tuple of student information
student = ("Rahul", 20, "Pune","python")
name, age, city, course = student
print("name:", name)
print("age:", age)
print("city:", city)
print("course:", course)

# Create a set of students
students = {"Rahul", "Priya", "Rahul",
"Rohan", "Priya", "Sneha"}

# Print set (duplicates remove!)
print("original set:", students)

# Add "Amit"
students.add("Amit")
print(students)

# Remove "Rohan"
students.remove("Rohan")
print(students)

# Create dictionary of 3 students with marks
marks = {}