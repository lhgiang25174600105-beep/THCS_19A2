n = int(input("Nhập số nguyên dương n: "))
def la_so_nguyen_to(n):
    if n <=1: # số nguyên tố phải lớn hơn 1
        return False
    for i in range (2,n):# chạy từ 2 đến n-1
        if n % i ==0 :
            # nếu n chia hết cho i chạy trong khoảng range thì không phải số nguyên tố
            # số nguyên tố chỉ có ước là 1 và chính nó
            return False
    return True
ket_qua = la_so_nguyen_to(n)
print(ket_qua)

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
def in_so_nguyen_to_trong_khoang(a,b):
    for i in range(a,b+1):
        if la_so_nguyen_to(i):
            print (i)
    return i
print(in_so_nguyen_to_trong_khoang(a,b))