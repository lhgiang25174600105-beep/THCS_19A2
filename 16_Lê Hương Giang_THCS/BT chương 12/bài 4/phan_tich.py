from du_lieu.danh_sach import sap_xep_tang_dan
ds = [3, 6, 8, 9, 1, 2]
sx = sap_xep_tang_dan(ds)
print("Danh sách sau khi sắp xếp là: ",sx)
from du_lieu.tu_dien import lay_gia_tri
td = {
    "ten":"Giang",
    "tuoi":18,
    "lop": "DHKL19A2HN"
}
gt = lay_gia_tri(td, "ten")
print("Giá trị của từ khóa 'ten': ",gt)