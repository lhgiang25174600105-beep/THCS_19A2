a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
def giai_phuong_trinh_bac_nhat (a,b):
    if a !=0:
        x = -b/a
        return f"Phương trình có một nghiệm duy nhất là: {x} "
    else: #(a = 0 )
        if b == 0:
            return "phương trình vô nghiệm"
        else:
            return "Phương trình có vô số nghiệm "
Ket_qua = giai_phuong_trinh_bac_nhat(a,b)
print(Ket_qua)
