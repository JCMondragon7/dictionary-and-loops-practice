# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

# 2. Combine the First and Last name into this format:
    #    "Last, First"  

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken


students = [
    {
        "cps_id": "1001",
        "name": "Smith, Jordan",
        "middle_name": "A",
        "homeroom": "201",
        "grade": 9,
        "primary_email": "jordan.smith@cps.edu",
        "secondary_email": "jsmith@gmail.com"
    },
    { "cps_id": "1002",
        "name": "abelo,rodelo",
        "middle_name": "b",
        "homeroom": "101",
        "grade": 11,
        "primary_email": "rodeloabelo@cps.edu",
        "secondary_email": "rabelo@gmail.com"},
    {
        "cps_id": "1003",
        "name": "Lopez, Maria",
        "middle_name": "E",
        "homeroom": "305",
        "grade": 10,
        "primary_email": "maria.lopez@cps.edu",
        "secondary_email": "mlopez@yahoo.com"
    }
]

# -----------------------------------
# Function: Search for a student
# -----------------------------------
def search_student(full_name):
    for student in students:
        if student["name"].lower() == full_name.lower():
            print("\n--- Student Found ---")
            print(f"CPS ID: {student['cps_id']}")
            print(f"Homeroom: {student['homeroom']}")
            print(f"Grade Level: {student['grade']}")
            print(f"Primary Email: {student['primary_email']}")
            return
    print("\nStudent not found.")

# -----------------------------------
# Function: Add a new student
# -----------------------------------
def add_student():
    print("\n--- Add New Student ---")

    cps_id = input("CPS ID: ")

    # Check for duplicate CPS ID
    for student in students:
        if student["cps_id"] == cps_id:
            print("Error: CPS ID already exists. Student not added.")
            return

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    middle_name = input("Middle Name: ")
    homeroom = input("Homeroom: ")
    grade = int(input("Grade Level: "))
    primary_email = input("Primary Email: ")
    secondary_email = input("Secondary Email: ")

    # Combine name as "Last, First"
    formatted_name = f"{last_name}, {first_name}"

    # Create student dictionary
    new_student = {
        "cps_id": cps_id,
        "name": formatted_name,
        "middle_name": middle_name,
        "homeroom": homeroom,
        "grade": grade,
        "primary_email": primary_email,
        "secondary_email": secondary_email
    }

    # Add student to list
    students.append(new_student)

    # Confirmation output
    print("\nStudent successfully added!")
    print(f"Total students in system: {len(students)}")
    print("New Student Record:")
    print(new_student)

# -----------------------------------
# Main Program Loop
# -----------------------------------
while True:
    print("\n--- Student Lookup Tool ---")
    print("1. Search for a student")
    print("2. Add a new student")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        name_input = input("Enter student name (Last, First): ")
        search_student(name_input)

    elif choice == "2":
        add_student()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")