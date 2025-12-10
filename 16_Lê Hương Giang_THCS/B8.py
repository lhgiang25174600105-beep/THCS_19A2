a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
def tim_so_le_lon_nhat(a, b, c):
    so_le_lon_nhat = -1 # nếu không có số lẻ nào sẽ trả về -1
    if a%2 != 0 : # a ko chia hết cho 2 thì a là số lẻ
        so_le_lon_nhat = a 
    if b%2 != 0 :
        if b > so_le_lon_nhat:
            so_le_lon_nhat = b
    if c%2 !=0 :
        if c > so_le_lon_nhat:
            so_le_lon_nhat = c
    return so_le_lon_nhat
print("Số lẻ lớn nhất là: ",tim_so_le_lon_nhat(a,b,c))

