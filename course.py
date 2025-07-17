courses = [
    "CSC1024,Programming Principles,15",
    "ECN3033,Economics Principle,10",
    "LES1011,Introduction to Legal Studies,12"
]

with open("courses.txt", "w") as file:
    for course in courses:
        file.write(course + "\n")

print("courses.txt has been created with course data.")
