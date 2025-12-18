n = int(input("Nhập số phần tử của tập A: "))
A = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1} của A: "))
    A = A + [x]  # Thêm phần tử bằng phép cộng list

m = int(input("Nhập số phần tử của tập B: "))
B = []
for i in range(m):
    x = int(input(f"Nhập phần tử thứ {i+1} của B: "))
    B = B + [x]  
# Phần tử thuộc A nhưng không thuộc B
thuoc_A = []
for a in A:
    if a not in B:
        thuoc_A = thuoc_A + [a]  # Thêm phần tử bằng phép cộng list

# Phần tử thuộc B nhưng không thuộc A
thuoc_B = []
for b in B:
    if b not in A :
        thuoc_B = thuoc_B + [b]  # Thêm phần tử bằng phép cộng list

# Phần tử thuộc cả A và B (giao)
giao = []
for a in A:
    if a in B:
        giao = giao + [a]  # Thêm phần tử bằng phép cộng list

# Phần tử thuộc A hoặc B (hợp)
hop = []
for a in A:
    if a not in hop:
        hop = hop + [a]  # Thêm phần tử bằng phép cộng list
for b in B:
    if b not in hop:
        hop = hop + [b]  # Thêm phần tử bằng phép cộng list

# In kết quả
print("Các phần tử thuộc A nhưng không thuộc B:", thuoc_A)
print("Các phần tử thuộc B nhưng không thuộc A:", thuoc_B)
print("Các phần tử thuộc cả A và B (giao):", giao)
print("Các phần tử thuộc A hoặc B (hợp):", hop)