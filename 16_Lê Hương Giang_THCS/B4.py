a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
def tinh_trung_binh_cong(a, b, c):
    tbc = (a+b+c)/3
    return tbc
ket_qua = tinh_trung_binh_cong(a,b,c)
print(f"Trung bình cộng của ba số là: {ket_qua}")