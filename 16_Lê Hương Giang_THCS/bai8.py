n = int(input("Nhập số lượng phần tử: "))

ds = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    ds = ds + [x]

k = int(input("Nhập số lần dịch chuyển k: "))

# dịch chuyển k lần
for t in range(k):
    cuoi = ds[n - 1]     # lấy phần tử cuối
    ds_moi = [cuoi]     # danh sách mới, bắt đầu bằng phần tử cuối

    for i in range(n - 1):
        ds_moi = ds_moi + [ds[i]]

    ds = ds_moi         # cập nhật lại danh sách

print("Danh sách sau khi dịch chuyển:")
print(ds)