# Q6. Create a Student Report System:
f= open("report.txt", "w")
f.write("Name: Rahul-85\n")
f.write("Name: Priya-90\n")
f.write("Name: Rohan-78\n")
f.write("Name: Sneha-92\n")
f.write("Name: Amit-65\n")
print("File Created !")

with open("report.txt","r") as file:
    for i in file:
        name, marks = i
    if int(marks)>80:
        print(f"{name}")


# Q7. Create an Employee File System:
import os

# Create employees.txt with 3 employees
with open("employees.txt", "w") as file:
    file.write("Rahul - Developer\n")
    file.write("Priya - Manager\n")
    file.write("Rohan - Tester\n")


# Read the file
print("Original Employees:")
with open("employees.txt", "r") as file:
    print(file.read())


# Append 2 more employees
with open("employees.txt", "a") as file:
    file.write("Sneha - Designer\n")
    file.write("Amit - Data Analyst\n")


# Read updated file
print("Updated Employees:")
with open("employees.txt", "r") as file:
    print(file.read())


# Delete the file
os.remove("employees.txt")


# Verify file exists or not
if os.path.exists("employees.txt"):
    print("File still exists")
else:
    print("File deleted successfully")