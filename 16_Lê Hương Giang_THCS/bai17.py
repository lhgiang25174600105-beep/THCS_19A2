n = int(input("Nhập số lượng cặp key-value: "))
d = {}
for i in range(n):
    key = input("Nhập key thứ " + str(i+1) + ": ")
    value = int(input("Nhập value cho key '" + key + "': "))
    d[key] = value
#Khởi tạo key và giá trị lớn nhất bằng phần tử đầu tiên
dau_tien = True  # Biến cờ để nhận phần tử đầu tiên
for k in d:
    if dau_tien:
        key_lon_nhat = k
        gia_tri_lon_nhat = d[k]
        dau_tien = False
    else:
        if d[k] > gia_tri_lon_nhat:
            gia_tri_lon_nhat = d[k]
            key_lon_nhat = k
print("Key có giá trị lớn nhất:", key_lon_nhat)
print("Giá trị lớn nhất:", gia_tri_lon_nhat)