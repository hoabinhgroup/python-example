def tinhtong(lst):
    tong = 0
    for i in lst:
        tong += i
    return tong


tong = tinhtong([1, 2, 3, 4, 5])  # Kết quả sẽ là 15
print(f"Tổng của danh sách là: {tong}")  # In ra kết quả