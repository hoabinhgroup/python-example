#Hiểu và sử dụng List, Tuple, Dictionary, Set.
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")  # Thêm phần tử vào danh sách
print(fruits)  # In danh sách sau khi thêm

# fruits.remove("banana")  # Xóa phần tử khỏi danh sách
# print(fruits)  # In danh sách sau khi xóa

# for fruit in fruits:  # Duyệt qua từng phần tử trong danh sách
#     print(fruit)  # In từng phần tử 

 #TUPLE – BỘ Giống list nhưng không thay đổi được, dùng để lưu hằng số:
# person = ("Nam", 22, 1.7, True)
# print(person)  # In tuple

#DICT – TỪ ĐIỂN

# student = {
#     "name": "Nam",
#     "age": 22,
#     "height": 1.7,
#     "is_student": True
# }

# print(student["name"])  
# for key,value in student.items():
#  print(f"{key}: {value}") # In dictionary

# hàm
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Tuấn")