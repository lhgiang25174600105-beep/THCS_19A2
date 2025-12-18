n = int(input("Nhập số lượng cặp key-value: "))
d = {}
for i in range(n):
    key = input("Nhập key thứ " + str(i+1) + ": ")
    value = input("Nhập value cho key '" + key + "': ")
    d[key] = value

# Đảo ngược dictionary
dao_nguoc = {}
for k in d:
    v = d[k]
    dao_nguoc[v] = k  # Value trở thành key, key trở thành value

# In kết quả
print("Dictionary ban đầu:", d)
print("Dictionary đảo ngược:", dao_nguoc)