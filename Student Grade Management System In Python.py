# Initializing dictionary
student_grades = {}


# Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with grade {grade}")


# Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s marks have been updated to {grade}")
    else:
        print(f"{name} is not found!")


# Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")


# View all students
def display_all_students():
    if not student_grades:
        print("No student records found.")
    else:
        print("\nStudent Records")
        print("-" * 25)
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")


# Main program
def main():
    while True:
        print("\n===== Student Grade Manager =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name: ")
            grade = int(input("Enter new student grade: "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
main()