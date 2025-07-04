students = ["Nam", "Tung", "Minh", "Hanh", "Thang"]

listStudent = ["Thái"]

for student in students:
    listStudent.append(student)

def removeStudent(name):
    if name in listStudent:
        listStudent.remove(name)
    else:
        print(f"{name} không có trong danh sách.")

removeStudent("Minh")
print(listStudent)