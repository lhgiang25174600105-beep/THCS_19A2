m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

# Hàng đầu tiên
tong_lon_nhat = 0
for j in range(n):
    x = int(input("Nhập phần tử: "))
    tong_lon_nhat = tong_lon_nhat + x

hang_lon_nhat = 0

# Các hàng còn lại
for i in range(1, m):
    tong_hang = 0
    for j in range(n):
        x = int(input("Nhập phần tử: "))
        tong_hang = tong_hang + x

    if tong_hang > tong_lon_nhat:
        tong_lon_nhat = tong_hang
        hang_lon_nhat = i

print("Hàng có tổng lớn nhất là hàng:", hang_lon_nhat)
print("Tổng lớn nhất là:", tong_lon_nhat)