class Student:
    def __init__(self, ID, Name, Dob, Mark):
        self.IDs = ID
        self.names = Name
        self.dob = Dob
        self.mark = Mark

    def get_in4(self, ID, Name, Dob, Mark):
        stu = Student(ID, Name, Dob, Mark)
        stu_lst.append(stu)

    def show_stu(self, st):
        print("ID: ", st.IDs)
        print("Name: ", st.names)
        print("DoB: ", st.dob)
        print("Mark: ", st.mark)
        print("\n")

    def show_cour(self):
        for i in range(course_lst.__len__()):
            print(course_lst[i])

    def input_cour(self):
        num_cr = int(input("Enter number of courses: "))
        if (num_cr <= 0):
            print("Input number of coure again !")
        else : 
            for i in range(num_cr):
                tpmid = int(input("Enter course ID: "))
                tpmName = str(input("Enter course name: "))
                tpm_cour = {"ID": tpmid, "Name": tpmName}
                course_lst.append(tpm_cour)

    def input_mark_cr(self, st, cour_id):
        stu_mark  = int(input(f"Enter mark of the {cour_id}: "))
        st.mark = {"ID": cour_id, "Mark": stu_mark}


course_lst = []
stu_lst = []
st = Student(0,"","",{})


print("\t\t\t1. Add student (ID, name, DoB only)")
print("\t\t\t2. Add course information ")
print("\t\t\t3. Show list of students")
print("\t\t\t4. Show list of courses")
print("\t\t\t5. Enter student mark of a courses")

while True:
    choice = int(input("\nEnter your option: "))
    if (choice == 1):
        stu_num = int(input("Enter number of students: "))
        for i in range(stu_num): 
            ids = int(input(f"Enter ID of {i} student: "))
            name = str(input(f"Enter name of {i} student: "))
            dob = int(input(f"Enter DOB of {i} student: "))
            mark = {}
            st.get_in4(ids, name, dob, mark)
    if (choice == 2):
        st.input_cour()
    if (choice == 3):
        for i in range(stu_lst.__len__()):
            st.show_stu(stu_lst[i])
    if (choice == 4):
        st.show_cour()
    if (choice == 5):
        st.show_cour()
        tpm = int(input("Enter the course to enter mark: "))
        for i in range(stu_lst.__len__()):
            st.input_mark_cr(stu_lst[i], tpm)

