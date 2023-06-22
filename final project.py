import uuid
"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Mohammed marwan attalla
Delivery Date : 22-06-2023
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)


class Course:
    def __init__(self, name, mark):
        self.course_id = str(uuid.uuid4())
        self.course_name = name
        self.course_mark = mark


class Student:

    # TODO 3 define static variable indicates total student count
    num_of_student = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, student_name, student_age, student_number):
        self.student_id = str(uuid.uuid4())
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []

        Student.num_of_student += 1

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_course(self, course):
        self.courses_list.append(course)
    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
# TODO 6 print student courses with their marks
        for course in self.courses_list:
            print("Course ID:" , course.course_id)
            print("Course Name :", course.course_name)
            print("Course Mark :", course.course_mark)

    # method to get student_average as a value

# TODO 7 return the student average

    def get_student_average(self):
        if len(self.courses_list) == 0:
            return 0

        total_mark = sum(course.course_mark for course in self.courses_list)
        average = total_mark / len(self.courses_list)
        return average


# in Global Scope
# TODO 8 declare empty students list
students = []
while True:

    # TODO 9 handle Exception for selection input
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit\n"
                              "Enter Your Selection : "))

        if selection == 1:

            # TODO 10 make sure that Student number is not exists before
            student_number = input("Enter Student Number")

            student_name = input("Enter Student Name")
            while True:
                try:
                    student_age = int(input("Enter Student Age"))
                    break
                except:
                    print("Invalid Value")
            is_existing = any(student.student_number == student_number for student in students)

            if is_existing:
                print("Student Number already exists.")
            # TODO 11 create student object and append it to students list
            else:
                student = Student(student_name, student_age, student_number)
                students.append(student)
            print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number")
            # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
            found_student = None

            for student in students:
                if student.student_number == student_number:
                    found_student = student
                    break

            if found_student is not None:
                students.remove(found_student)
                print("Student Deleted Successfully")
            else:
                print("Student Not Exist")

        elif selection == 3:
            student_number = input("Enter Student Number")
            # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
            found_student = None

            for student in students:
                if student.student_number == student_number:
                    found_student = student
                    break

            if found_student is not None:
                print("Student Details:")
                print("Student ID:", found_student.student_id)
                print("Student Name:", found_student.student_name)
                print("Student Age:", found_student.student_age)
                print("Student Number:", found_student.student_number)
                print("Courses:")
                found_student.get_student_courses()
            else:
                print("Student Not Exist")

        elif selection == 4:
            student_number = input("Enter Student Number")
            # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
            found_student = None

            for student in students:
                if student.student_number == student_number:
                    found_student = student
                    break

            if found_student is not None:
                average = found_student.get_student_average()
                print("Student Average:", average)
            else:
                print("Student Not Exist")

        elif selection == 5:
            student_number = input("Enter Student Number")
            # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses
            found_student = None

            for student in students:
                if student.student_number == student_number:
                    found_student = student
                    break

            if found_student is not None:
                course_name = input("Enter Course Name")
                while True:
                    try:
                        course_mark = float(input("Enter Course Mark"))
                        break
                    except ValueError:
                        print("Invalid Value")

                course = Course(course_name, course_mark)
                found_student.enroll_course(course)
                print("Course Added Successfully")
            else:
                print("Student Not Found")
        # TODO 16 call a function to exit the program
        elif selection == 6:
            break

        else:
            print("Invalid Selection")
    except ValueError:
        print("Invalid Selection")
