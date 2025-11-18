a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
while b !=0:
    phan_du = a % b
    a = b
    b = phan_du
ucln = a
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")