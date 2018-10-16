class Student:
    def __init__(self, name, id_number, gpa, expected_grade, work_status):
        self.name = name
        self.id_number = id_number
        self.gpa = gpa
        self.expected_grade = expected_grade
        self.work_status = work_status
        
    def get_name(self):
        return self.name
    
    def get_id_number(self):
        return self.id_number
    
    def get_gpa(self):
        return self.gpa
    
    def get_expected_grade(self):
        return self.expected_grade
    
    def get_work_status(self):
        return self.work_status
    
    def set_gpa(self, gpa):
        self.gpa = gpa
        
    def set_expected_grade(self, grade):
        self.expected_grade = grade
        
        
def get_student_info():
    name = str(input("What is the name of the student? "))
    id_number = int(input("What is the i.d. number of " + name + "? "))
    gpa = float(input("What is " + name + "'s GPA? "))
    expected_grade = int(input("What is the expected grade of " + name + "? "))
    work_status = str(input("Does " + name + " work full-time or part-time? "))
    return (name, id_number, gpa, expected_grade, work_status)
    
def print_menu():
    menuStr = str("1. Look up and print the student GPA." + '\n' +
        "2. Add a new student to the class." + '\n' +
        "3. Change the GPA of a student." + '\n' +
        "4. Change the expected grade of a student." + '\n' +
        "5. Print the data of all the students in a tabular format." + '\n' +
        "6. Quit the program. ")
    print("\n\n")
    print(menuStr)
    
def getStudent(student_list, student_name):
    """ Return student with given name or None if no student with given name """
    theStudent = None
    for student in student_list:
        if student.get_name() == student_name:
            theStudent = student
            break
    return theStudent
    
def print_student_info_table(student_list):
    # name, id_number, gpa, expected_grade, work_status
    print("{} {} {} {} {}".format("Name", "ID", "GPA", "EXPECTED GRADE", "WORK STATUS"))
    for student in student_list:
        name = student.get_name()
        id_number = student.get_id_number()
        gpa = student.get_gpa()
        expected_grade = student.get_expected_grade()
        work_status = student.get_work_status()
        print("{} {} {} {} {}".format(name, id_number, gpa, expected_grade, work_status))
    
def menu(student_list):
    valid_input = True
    while valid_input == True:
        try:
            print("\n\n")
            print_menu()
            user_input = int(input())
            if user_input not in range(1, 7):
                print("You have entered an invalid selection for the menu. Please enter a number from 1 to 6. ")
                valid_input = False
            else:
                # # Look up and print student GPA
                if user_input == 1:
                    name = input("What is the students name? ")
                    student = getStudent(student_list, name)
                    if student is None:
                        print("Sorry, could not find", name)
                    else:
                        gpa = student.get_gpa()
                        print("{}'s gpa is {}".format(name, gpa))
                # # Add a new student to the class
                if user_input == 2:
                    name, id_number, gpa, expected_grade, work_status = get_student_info()
                    student = Student(name, id_number, gpa, expected_grade, work_status)
                    student_list.append(student)
                 # # Change the GPA of a student
                if user_input == 3:
                    name = input("What is the students name? ")
                    student = getStudent(student_list, name)
                    if student is None:
                        print("Sorry, could not find", name)
                    else:
                        new_gpa = input("What is the new gpa? ")
                        student.set_gpa(new_gpa)
                # # Change the expected grade of a student
                if user_input == 4:
                    name = input("What is the students name? ")
                    student = getStudent(student_list, name)
                    if student is None:
                        print("Sorry, could not find", name)
                    else:
                        new_grade = input("What is the new expected grade? ")
                        student.set_expected_grade(new_grade)
                # # Print the data of all the students in a tabular format
                if user_input == 5:
                    # name, id, gpa, expected grade, PT or FT
                    print_student_info_table(student_list)
                 # # Quit the program
                if user_input == 6:
                    print("")
                    print("Okay. Now quitting the program.")
                    valid_input = False
        except:
            pass
    
    
    
def main():
    #name, id_number, gpa, expected_grade, work_status = getStudentInfo()
    student_list = []
    student_list.append(Student('Wally', 345, 3.4, 4, 'Full-time'))
    student_list.append(Student('Bo', 23, 4.0, 80, 'Part-Time'))
    student_list.append(Student('Tom', 78, 2.0, 70, 'Part-Time'))
    student_list.append(Student('Jimmy', 100, 4.0, 90, 'Full-Time'))
    student_list.append(Student('Billy', 88, 3.3,  78, 'Full-Time'))
    menu(student_list)
    print("All done.")  
if __name__ == '__main__':
    main()
