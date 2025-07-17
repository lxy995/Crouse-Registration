import os

#=====Helpers=====
students = "students.txt"
courses = "courses.txt"
enrollments = "enrollments.txt"

for file in [students, courses, enrollments]:
    if not os.path.exists(file):
        open(file, "w").close()


#=====Core program=====

#Choice 1

def add_student():
    with open("students.txt", "a") as file:
        while True:
            print("\n===== Student Registration =====")
            print("1. Add Student")
            print("2. Exit")

            choice = input("Enter your choice (1/2): ")
            if choice == "1":
                student_id = input("Enter Student ID: ")
                student_name = input("Enter Student Name: ")
                student_contact = input("Enter Student Contact: ")

                file.write(f"{student_id},{student_name},{student_contact}\n")  #  save to the file

                print("\nStudent details recorded:")
                print(f"ID: {student_id}, Name: {student_name}, Contact: {student_contact}")
            elif choice == "2":
                print("Records Ended.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")




#Choice 2

def add_course():
    while True:
        print("\n===== Course Registration =====")
        course_id = input("Enter Course ID: ").strip()
        course_name = input("Enter Course Name: ").strip()
        max_students = input("Enter Maximum Students: ").strip()

        # Validate course details
        if not course_id or not course_name or not max_students.isdigit():
            print("Error: Invalid input. Course ID and Name are required, and Max Students must be a number.")
            continue

        max_students = int(max_students)

        # Check if course already exists
        try:
            with open("courses.txt", "r") as file:
                existing_courses = file.readlines()
                if any(line.startswith(course_id + ",") for line in existing_courses):
                    print(f"Error: Course ID {course_id} already exists!")
                    continue
        except FileNotFoundError:
            pass  # File does not exist yet, so it's safe to create a new one

        # Save course to the file
        with open("courses.txt", "a") as file:
            file.write(f"{course_id},{course_name},{max_students}")

        print("\nCourse successfully added:")
        print(f"ID: {course_id}, Name: {course_name}, Max Students: {max_students}")

        # Ask if user wants to add another course
        another = input("Do you want to add another course? (yes/no): ").strip().lower()
        if another != "yes":
            break

    print("Returning to the main menu...")




#Choice 3

def enroll_in_course():
    while True:
        print("\n===== Course Enrollment =====")
        student_id = input("Enter Student ID: ").strip()
        student_name = input("Enter Student Name: ").strip()
        course_id = input("Enter Course ID to Enroll In: ").strip()

        if not student_id or not student_name or not course_id:
            print("Error: Student ID, Name, and Course ID are required.")
            continue

        course_exists = False
        course_data = None  # To store course info
        updated_courses = []  # To store modified course list

        try:
            with open("courses.txt", "r") as file:
                courses = file.readlines()

            for line in courses:
                if line.strip():
                    existing_id, course_name, max_students = line.strip().split(",")
                    max_students = int(max_students)

                    if existing_id == course_id:
                        course_exists = True
                        enrolled_students = 0

                        # Count enrolled students in this course
                        try:
                            with open("enrollments.txt", "r") as enroll_file:
                                for enroll_line in enroll_file:
                                    _, _, enrolled_course = enroll_line.strip().split(",")
                                    if enrolled_course == course_id:
                                        enrolled_students += 1
                        except FileNotFoundError:
                            pass  # No enrollments yet

                        if enrolled_students >= max_students:
                            print(f"Error: Course '{course_name}' is full! No available seats.")
                            continue  # Try another course

                        course_data = (existing_id, course_name, max_students, enrolled_students)

                        # Update available seats by subtracting 1
                        new_available_seats = max_students - enrolled_students - 1
                        updated_courses.append(f"{course_id},{course_name},{new_available_seats}\n")
                    else:
                        updated_courses.append(line)  # Keep other courses unchanged

        except FileNotFoundError:
            print("Error: No courses found. Please add courses first.")
            continue

        if not course_exists:
            print(f"Error: Course ID '{course_id}' not found!")
            continue

        # Check if student is already enrolled
        try:
            with open("enrollments.txt", "r") as file:
                for line in file:
                    existing_student, _, enrolled_course = line.strip().split(",")
                    if existing_student == student_id and enrolled_course == course_id:
                        print(f"Error: Student '{student_name}' is already enrolled in this course!")
                        continue
        except FileNotFoundError:
            pass  # No enrollments yet

        # Save the enrollment
        with open("enrollments.txt", "a") as file:
            file.write(f"{student_id},{student_name},{course_id}\n")

        # Rewrite courses.txt with updated seat count
        with open("courses.txt", "w") as file:
            file.writelines(updated_courses)

        print("\nEnrollment successful:")
        print(f"Student ID: {student_id}, Name: {student_name}, Course: {course_data[1]} (Seats left: {new_available_seats})")

        another = input("Do you want to enroll another student? (yes/no): ").strip().lower()
        if another != "yes":
            break

    print("Returning to the main menu...")



#Choice 4

def drop_course_system():
    print("\n===== Drop a Course =====") #heading
    student_id = input("Enter your Student ID: ") # Prompt the user to enter their Student ID
    course_id = input("Enter the Course ID to drop: ") # Prompt the user to enter the Course ID

    #Remove the enrollment record from enrollments.txt
    enrollment_found = False #to check if the enrollment record has been found
    updated_enrollments = [] # List to keep all enrollment records except the one that will be dropped.

    try:
        with open("enrollments.txt", "r") as file: #open enrollments.txt in read mode.
            lines = file.readlines() # Read all lines from the file
    except FileNotFoundError:
        print("Error: enrollments.txt file not found.")
        return

    for line in lines:  # Loop through each line in the enrollments data
        record = line.strip().split(',')
        if len(record) != 3:  # Only proceed if record has exactly 3 fields
            continue  # Skip invalid lines

        rec_student_id, rec_student_name, rec_course_id = record  # Safe unpacking

        if rec_student_id == student_id and rec_course_id == course_id:
            enrollment_found = True
        else:
            updated_enrollments.append(line)  # Keep all other records



    # If no matching enrollment was found, inform the user and exit the function.
    if not enrollment_found:
        print("Enrollment record not found. You are not enrolled in the specified course.")
        return
    else: # If the record was found, open enrollments.txt in write mode and overwrite it
        with open("enrollments.txt", "w") as file:
            file.writelines(updated_enrollments)
        print("Enrollment record successfully removed.")

    #Update courses.txt by subtracting 1 from the seat count
    course_found = False
    updated_courses = []
    updated_seats = None  # Used for reporting the new seat count

    try:
        with open("courses.txt", "r") as file: #open courses.txt in read mode.
            course_lines = file.readlines()
    except FileNotFoundError:
        print("Error: courses.txt file not found.")
        return

    # Process each course record ( CourseID,CourseName,SeatCount)
    for line in course_lines:
        record = [field for field in line.split(',')]
        if len(record) < 3:
            updated_courses.append(line)
            continue

        current_course_id, course_name, seats_str = record # Unpack the record into variables.

        if current_course_id == course_id:
            try:
                seats = int(seats_str)
                seats -= 1  # Subtract one from the seat count (each drop reduces the count)
                updated_line = f"{current_course_id},{course_name},{seats}\n"
                updated_courses.append(updated_line)
                course_found = True #to indicate this course record was found and updated.
                updated_seats = seats
            except ValueError:
                print(f"Error: Seat count for course {course_id} is not a valid integer.")
                updated_courses.append(line)
        else:
            updated_courses.append(line)

    if course_found:
        with open("courses.txt", "w") as file:
            file.writelines(updated_courses)
        print(f"A seat has been removed. New seat count for course {course_id}: {updated_seats}") # Inform the user of the new seat count after the drop.
    else:
        print("Course record not found") # If no record for the specified course was found




#Choice 5

def view_available_courses():
    # Print a heading for the course viewing system.
    print("\n===== Available Courses =====\n")

    # Try to open and read the courses.txt file.
    try:
        with open("courses.txt", "r") as file:
            courses = file.readlines()  # Read all course records from the file.
    except FileNotFoundError:
        # If the courses.txt file is not found, print an error message.
        print("Error: file not found.")
        return

    # Print a formatted header for the output table.
    print("{:<10} {:<30} {:<15}".format("Course ID", "Course Name", "Available Seats"))
    print("-" * 60)  # Print a separator line.

    # Loop through each course record in the file.
    for line in courses:
        # Remove any leading/trailing whitespace characters (including newline).
        line = line.strip()
        # If the line is empty, skip it.
        if not line:
            continue

        # Split the line by commas into parts.
        record = line.split(",")
        # Check if the record has at least 3 fields.
        if len(record) >= 3:
            # Extract and clean up each field.
            course_id = record[0].strip()
            course_name = record[1].strip()
            available_seats = record[2].strip()

            # Print the course details in a formatted manner.
            print("{:<10} {:<30} {:<15}".format(course_id, course_name, available_seats))
        else:
            # If the line is not in the expected format, print a message indicating a bad record.
            print("Skipping invalid line:", line)

#Choice6

def students_information():
    students = 'students.txt'
    try:
        with open(students, 'r') as file:
            students = file.readlines()
        if not students:
            print("No students found.")
            return
        print("===== List of All Students =====")
        for line in students:
            print(line.strip())
    except FileNotFoundError:
        print("Error: Students file not found.")




 #Choice 7

def exit_program(exit):
    while exit == True: #Start an infinity loop
        confirm = input("Are you sure you want to exit? (yes/no): ") #Ask the user for exit confirmation
        if confirm.lower() == 'yes': #If the user confirms exit
            print("Exiting program. GoodBye!") #Print exit message
            exit = False #End the loop
            return exit
        elif confirm.lower() == 'no': #If the user cooses not to exit
            print("Return to the main menu.") #Inform about returning to the main menu
            return #Exit the function without closing the program
        else: #If user enters an invalid response
            print("Invalid input. Please enter 'yes' or 'no'.") #Propmt for valid input


#======Menu system======

def main():
    exit = True
    while exit == True:
     #Program Menu
        print("\n----Course Registration System----\n")
        print("1. Add a New Student")
        print("2. Add a New Course")
        print("3. Enroll Student in a Course")
        print("4. Drop a Course")
        print("5. View Available Courses")
        print("6. View Student Information")
        print("7. Exit")
        print("***************************\n")
        #User Choice
        choose = input("Enter your choice(1-7): ")

        if choose == "1":
            add_student()
        elif choose == "2":
            add_course()
        elif choose == "3":
            enroll_in_course()
        elif choose == "4":
            drop_course_system()
        elif choose == "5":
            view_available_courses()
        elif choose == "6":
            students_information()
        elif choose == "7":
            exit = exit_program(exit)

        else:
            print("Your choice is not within parameters.\n")
            print("*****************************\n")



# =====Run Program=====
if __name__ == "__main__":
    main()
else:
    print("This program is run from import.\n Please, run it directly form code.")
