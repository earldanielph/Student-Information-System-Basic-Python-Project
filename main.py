# Student Information System - Functionality 2
# Earl Daniel Villanueva

students = []
for i in range(5):
    studentName = str(input('Student Name: '))
    studentSN = str(input('Student Number: '))
    studentMobile = str(input('Mobile Number: '))
    studentEmail = str(input('Email: '))
    studentBalance = str(input('Balance: ₱'))

    students.append([studentName, studentSN, studentMobile, studentEmail, studentBalance])
index = int(input("Enter value from 1 - 5 to print student information and 0 to exit: "))
while index != 0:
    student = students[index - 1]
    print(student[0] + ',' + student[1] + ',' + student[2] + ',' + student[3] + ', ₱' + student[4])
    print()
    index = int(input("Enter value from 1-5 to print student information: "))

