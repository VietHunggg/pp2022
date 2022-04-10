from re import I
from domain.system import *

def main():
    stu_lst = []
    cour_lst = []
    init = System(stu_lst,cour_lst)
    print("\t\t\t1. Add student (ID, name, DoB only)")
    print("\t\t\t2. Add course information ")
    print("\t\t\t3. Show list of students")
    print("\t\t\t4. Show list of courses")
    print("\t\t\t5. Enter student mark of a courses")
    print("\t\t\t6. Average GPA ")
    print("\t\t\t7. Press any key except 1-6 to exit !")

    while True:
        choice = int(input("Enter your options: "))
        if choice == 1:
            init.AddStudent()
        if choice == 2:
            init.Addcourse()
        if choice == 3:
            init.show_stu()
        if choice == 4:
            init.show_cour()
        if choice == 5:
            init.show_cour()
            tpm = int(input("Enter the course to enter mark: "))
            for i in range(init.stu_lst.__len__()):
                init.Add_mark_cr(init.stu_lst[i], tpm)
        if choice == 6:
            tpmarr = []
            tpmID = int(input("Enter the student ID to check GPA: "))
            if init.check_valid_stu(tpmID) == True:
                init.avgGPA(tpmarr, tpmID)


if __name__ == "__main__":
    main()


