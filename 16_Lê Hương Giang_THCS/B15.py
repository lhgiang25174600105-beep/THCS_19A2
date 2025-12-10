#đk : số đó phải là số tự nhiên lớn hơn 1 và chỉ có đúng hai ước số dương là 1 và chính nó
n = int(input("Nhập số nguyên dương n: "))
def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i ==0 :
            return False
    return True
print(so_nguyen_to(n))
for x in range(100, 501):
    if so_nguyen_to(x):
        print (x)


