def add_student(students):
    """Adds a new student to the records after checking for duplicate IDs."""
    student_id = input("Enter Student ID: ").strip()
    
    if student_id in students:
        print("PROGRAM DISPLAYS Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    
    # Input validation for age
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid age. Please enter a valid number.")
        return
        
    course = input("Enter Course: ").strip()
    email = input("Enter Email: ").strip()

    # Storing details as a nested dictionary
    students[student_id] = {
        "Student Name": name,
        "Age": age,
        "Course": course,
        "Email": email
    }
    print(f"Student '{name}' added successfully!")


def display_students(students):
    """Displays all student records in a readable format."""
    if not students:
        print("PROGRAM DISPLAYS No student records found.")
        return

    print("\n--- ALL STUDENT RECORDS ---")
    for s_id, info in students.items():
        print(f"ID: {s_id}")
        for key, value in info.items():
            print(f"  {key}: {value}")
        print("-" * 25)


def search_student(students):
    """Searches and displays a student's details by ID."""
    student_id = input("Enter Student ID to search: ").strip()
    
    if student_id in students:
        print(f"\n--- Student Found ---")
        print(f"Student ID: {student_id}")
        for key, value in students[student_id].items():
            print(f"{key}: {value}")
    else:
        print("PROGRAM DISPLAYS Student not found.")


def delete_student(students):
    """Deletes a student record by ID using dictionary methods."""
    student_id = input("Enter Student ID to delete: ").strip()
    
    # Using pop() to remove the record if it exists
    removed_student = students.pop(student_id, None)
    
    if removed_student:
        print(f"Student ID {student_id} ({removed_student['Student Name']}) has been deleted.")
    else:
        print("PROGRAM DISPLAYS Student not found. Cannot delete.")


def main():
    """Main loop driving the menu system."""
    # Outer dictionary to hold all student records
    student_records = {}
    
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_student(student_records)
        elif choice == '2':
            display_students(student_records)
        elif choice == '3':
            search_student(student_records)
        elif choice == '4':
            delete_student(student_records)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()
