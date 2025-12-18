x = int(input("Nhập số thứ 1: "))
lon_nhat = x
lon_thu_hai = x

# Nhập các số còn lại
for i in range(2, x + 1):
    print("Nhập số thứ", i)
    x = int(input())
    if x > lon_nhat:
        lon_thu_hai = lon_nhat
        lon_nhat = x
    elif x < lon_nhat and x > lon_thu_hai:
        lon_thu_hai = x

print("Số lớn thứ hai là:", lon_thu_hai)