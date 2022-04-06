
stu_num = int(input("Enter the number of students: "))
stu_list = [stu_num]
cour_list = []

def get_in4():
    print("\nEnter student information\n")
    id = int(input("Enter student ID: "))
    stu_name = str(input("Enter student name: "))
    stu_dob = str(input("Enter student DoB: "))
    num_cour = int(input("Enter student's number of courses: "))
    lst_mark = []
    for i in range(num_cour):
        cour_ID = int(input("Enter course ID: "))
        cour_mark = float(input("Enter course mark: "))
        stu_mark = {"cour_id" : cour_ID, "Mark": cour_mark}
        lst_mark.append(stu_mark)

    stu = {"ID" : id, "Name" : stu_name, "DOB" : stu_dob, "Mark" : lst_mark}
    stu_list.append(stu)

def show_stu():
    for i in range(len(stu_list)):
        print(stu_list[i])

def show_cour():
    for i in range(len(cour_list)):
        print(cour_list[i])

def get_cousre():
    x = int(input("Enter ID of course: "))
    y = str(input("Enter: "))
    cour  = {"ID" : x, "Name" : y}
    cour_list.append(cour)

def show_mark(stu_id,cour_id):
    for i in range(len(stu_list)):
        if (int(stu_list[i]["ID"]) == stu_id):
            for j in range(len(stu_list[i]["Mark"])):
                if (int(stu_list[i]["Mark"][j]["cour_ID"]) == cour_id):
                    print(stu_list[i]["Mark"][j])

print("\t\t\t1. Add student")
print("\t\t\t2. Add course information")
print("\t\t\t3. Show list of students")
print("\t\t\t4. Show list of courses")
print("\t\t\t5. Show student mark of a courses")

while True:
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        get_in4()
    elif (choice == 2):
        get_cousre()
    elif (choice == 3):
        show_stu()
    elif (choice == 4):
        show_cour()
    elif (choice == 5):
        tpm_id = int(input("Enter your ID of student: "))
        tpm_cour_id = int(input("Enter ID of course: "))
        show_mark(tpm_id, tpm_cour_id)