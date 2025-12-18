n = int(input("Nhập số lượng số: "))
ds = []
for i in range(n):
    x = int(input("Nhập số: "))
    ds = ds + [x] #thêm từ số vào danh sách
S = int(input("Nhập tổng cần tìm: "))
for i in range(n):
    for j in range(i + 1, n): # chọn số đứng sau i
        if ds[i] + ds[j] == S:
            print(ds[i], ds[j])