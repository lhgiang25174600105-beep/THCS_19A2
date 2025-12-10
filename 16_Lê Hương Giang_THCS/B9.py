n = int(input("Nhập số nguyên dương n: "))
def tinh_tong_chu_so(n):# dùng hàm đệ quy, nên ko dùng for 
    #có điều kiện khử đệ quy
    if n > 0:
        return n + tinh_tong_chu_so(n-1)
    return 0
if n < 0 :
    print("Yêu cầu nhập số nguyên dương")
else:
    print(tinh_tong_chu_so(n))