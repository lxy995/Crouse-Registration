students = [
    "23060247,Student1,Student1@gmail.com"
    "25006537,Student2,Student2@gmail.com"
    "24136657,Student3,Student3@gmail.com"
    "25008327,Student4,Student4@gmail.com"
    "24011224,Student5,Student5@gmail.com"
    "23090921,Student6,Student6@gmail.com"
    "23096654,Student7,Student7@gmail.com"
    "23013246,Student8,Student8@gmail.com"
    "23135254,Student9,Student9@gmail.com"
    "24081101,Student10,Student10@gmail.com"
    "65330021,Student11,Student11@gmail.com"
]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("students.txt has been created with student data.")
