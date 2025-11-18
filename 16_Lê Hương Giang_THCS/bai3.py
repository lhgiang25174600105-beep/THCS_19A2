tu= int(input("Nhập mẫu số: "))
mau = int(input("Nhập tử số: "))

if mau == 0 :
    print("Không tồn tại")
else :
    a = abs(tu)
    b = abs(mau)

    while b != 0 :
        a,b = b, a%b
    ucln = a 

rgtu = tu // ucln
rgmau = mau // ucln

if rgmau < 0 :
    rgtu = - rgtu
    rgmau = - rgmau

print("phân số tối giản", rgtu, "/", rgmau)
