# Step 1: Create student.txt and write name and college name

with open("student.txt", "w") as file:
    file.write("Name: Akash\n")
    file.write("College: TIMT College\n")

# Step 2: Read and print the content of student.txt

with open("student.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# Step 3: Add course name to the same file

with open("student.txt", "a") as file:
    file.write("Course: BCA\n")

print("Course name added successfully.")
