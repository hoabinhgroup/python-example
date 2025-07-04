students = []

def add_student(name, age, email):
    student = {
        "name": name,
        "age": age,
        "email": email
    }
    students.append(student)


name = input("Enter student's name: ")
age = input("Enter student's age: ") 
email = input("Enter student's email: ")

print("Adding student...")
add_student(name, age, email)
print(students)