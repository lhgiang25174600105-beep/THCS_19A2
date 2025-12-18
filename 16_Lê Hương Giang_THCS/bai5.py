n = int(input("Nhập số lượng phần tử: "))

ket_qua = []   # danh sách rỗng

for i in range(n):
    x = int(input("Nhập phần tử: "))

    da_ton_tai = False
    for y in ket_qua:
        if x == y:
            da_ton_tai = True
            break

    if  da_ton_tai== False:
        ket_qua = ket_qua + [x]   # tạo danh sách mới có thêm x 
        

print("Danh sách sau khi loại bỏ phần tử trùng lặp:")
print(ket_qua)