n = int(input("Nhập số lượng sinh viên: "))
diem_sinh_vien = {}
for i in range(n):
    ten = input("Nhập tên sinh viên thứ " + str(i+1) + ": ")
    diem = int(input("Nhập điểm của " + ten + ": "))
    diem_sinh_vien[ten] = diem
# Nhóm sinh viên theo điểm
nhom_theo_diem = {}
for ten in diem_sinh_vien:
    diem = diem_sinh_vien[ten]
    if diem in nhom_theo_diem:
        nhom_theo_diem[diem] = nhom_theo_diem[diem] + [ten]
    else:
        nhom_theo_diem[diem] = [ten]

# In kết quả
for diem in nhom_theo_diem:
    print(diem, ":", nhom_theo_diem[diem])