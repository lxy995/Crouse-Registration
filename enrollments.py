
enrollments = [
    "23060247,CSC1024,2025-01-05",
    "25006537,CSC1024,2025-01-09",
    "24136657,CSC1024,2025-01-13",
    "25008327,CSC1024,2025-01-16",
    "24011224,CSC1024,2025-01-22",
    "23090921,ECN3033,2025-02-02",
    "23096654,ECN3033,2025-02-07",
    "23013246,LES1011,2025-02-12",
    "23135254,LES1011,2025-02-23",
    "24081101,LES1011,2025-02-31"
    ]

with open("enrollments.txt", "w") as file:
    for enrollment in enrollments:
        file.write(enrollment + "\n")

print("enrollments.txt has been created with the provided enrollment data.")
