n = int(input("Nhập cấp của ma trận: "))
tong = 0
for i in range(n): # cột
    for j in range(n): # hàng
        x = int(input("Nhập phần tử: "))

        if j == n - 1 - i:
            tong = tong + x
print("Tổng các phần tử trên đường chéo phụ là:", tong)