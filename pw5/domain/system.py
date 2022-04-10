import numpy as np
from domain.student import *
from domain.course import *

class System():
    def __init__(self, stu_lst, cour_lst):
        self.stu_lst = []
        self.cour_lst = []

    def check_valid_stu(self, Id):
        for i in range(self.stu_lst.__len__()):
                if self.stu_lst[i].IDs == Id:
                    print("Valid student identifier !")
                    return True

    def check_valid_cour(self, Id):
        for i in range(self.cour_lst.__len__()):
                if self.cour_lst[i].IDs == Id:
                    print("Valid course identifier !")
                    return True
    
    def AddStudent(self):
        stu = open("student.txt", "a")
        tpmID = int(input("Enter student ID - (Syntax only number): "))
        tpmName = str(input("Enter student name: "))
        tpmDob = str(input("Enter student's DoB: "))
        st = Student(tpmID, tpmName, tpmDob)
        self.stu_lst.append(st)
        stu.write(f"{tpmID},{tpmName},{tpmDob}\n")
        stu.close()

    def Add_mark_cr(self, studentID, cour_id):
        stu_mark  = math.floor(float(input(f"Enter mark of the {cour_id}: ")))
        studentID.mark.append({"ID": cour_id, "Mark": stu_mark})

    def avgGPA(self, tpmarr, studentID):
        for i in range(self.stu_lst.__len__()):
            if self.stu_lst[i].IDs == studentID:
                tpmMark = self.stu_lst[i].mark
                for j in range(tpmMark.__len__()):
                    tpmarr.append(tpmMark[j]["Mark"])
        tpmNparr = np.array(tpmarr)
        stu_GPA = np.average(tpmNparr)
        print(f"GPA of student {studentID}: {stu_GPA}")


    def show_stu(self):
        for i in range(self.stu_lst.__len__()):
            print("ID: ", self.stu_lst[i].IDs)
            print("Name: ", self.stu_lst[i].names)
            print("DoB: ", self.stu_lst[i].dob)
            print("Mark: ", self.stu_lst[i].mark)
            print("\n")
    
    def Addcourse(self):
        course = open("course.txt", "a")
        tpmID = int(input("Enter course ID: "))
        tpmSub = str(input("Enter name of course: "))
        cr = Courses(tpmID, tpmSub)
        self.cour_lst.append(cr) 
        course.write(f"{tpmID},{tpmSub}\n")
        course.close()
    
    def show_cour(self):
        for i in range(self.cour_lst.__len__()):
            print("\nCourse ID: ", self.cour_lst[i].get_id())
            print("Course Name: ", self.cour_lst[i].get_name())