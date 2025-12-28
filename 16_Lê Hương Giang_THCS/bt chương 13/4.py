with open("san_pham.txt", "w", encoding="utf-8") as f :
    f.write("ID, Tên sản phẩm, Giá\n")
    f.write("1, Laptop, 1200\n")
    f.write("2, Chuột bàn phím, 25\n")
    f.write("3, Bàn phím, 75\n")
ID_san_pham = input("Nhập ID sản phẩm cần cập nhật giá: ")
gia_moi = input("Nhập giá mới: ")
with open("san_pham.txt", "r", encoding="utf-8") as f:
    r = f.readlines()

ds_moi = []
for dong in r:
    dong = dong.strip()
    if dong.startswith("ID"):
        ds_moi.append(dong)
        continue
id_sp, ten_sp, gia = dong.split(",")
if id_sp == ID_san_pham:
    dong_moi = f"{id_sp},{ten_sp},{gia_moi}"
else:
    dong_moi = dong
    ds_moi.append(dong_moi)

with open("san_pham.txt", "w", encoding="utf-8") as f:
    for dong in ds_moi:
        f.write(dong+"\n")
print("Đã cập nhật")
