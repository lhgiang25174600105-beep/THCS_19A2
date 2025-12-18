n = int(input("Nhập số lượng cặp key-value: "))
d = {}
for i in range(n):
    key = input("Nhập key thứ " + str(i+1) + ": ")
    value = int(input("Nhập value cho key '" + key + "': "))
    d[key] = value

# Lọc các cặp thỏa điều kiện (value > 50)
dieu_kien = 50
d_loc = {}
for k in d:
    if d[k] > dieu_kien:
        d_loc[k] = d[k]

print("Các cặp key-value thỏa điều kiện (value >", dieu_kien, "):")
for k in d_loc:
    print(k, ":", d_loc[k])