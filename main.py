# Evtech - Earl Daniel Villanueva
# You can connect with me here at this link. https://beacons.ai/evtech

students = []

def add_student(): 
    students_info = []
    student_name = input("\nEnter Student's Name: ")
    student_SN = input("\nEnter Student Number: ")
    student_mobile = int(input("\nEnter Student's Mobile Number: "))
    student_email = input("\nEnter Student's Email Address: ")
    student_balance = float(input("\nEnter Student's Balance: "))
    students_info.append(student_name)
    students_info.append(student_SN)
    students_info.append(student_mobile)
    students_info.append(student_email)
    students_info.append(student_balance)
    students.append(students_info)

def view_all():
    if len(students) == 0:
        print("\nThere are no students in the system\n")
    else:
        print("\nList of Students:")
        for i, student in enumerate(students):
            print("-------------------------------")
            print(f"Student {i + 1} details:")
            print(f"Name: {student[0]}")
            print(f"SN: {student[1]}")
            print(f"Mobile Number: {student[2]}")
            print(f"Email: {student[3]}")
            print(f"Balance: {student[4]}")
        print("\n")

while True:
    print("Welcome to Student Information System – Functionality 3")
    print(f"There are {len(students)} students in the system.")
    print("\nWhat would you like to do?")
    print("1. Add Student\n2. View all Students\n3. Exit")
    option = int(input("\nSelect an option (1/2/3): "))
    if option == 1:
        add_student()
    elif option == 2:
        view_all()
    elif option == 3:
        print("Thank you for using the system!")
        break
    else:
        print("Invalid option. Please try again.")