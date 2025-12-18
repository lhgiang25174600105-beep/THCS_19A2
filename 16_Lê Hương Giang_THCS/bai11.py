n = int(input("Nhập cấp của ma trận: "))
# Nhập ma trận
a = []
for i in range(n):
    hang = []
    for j in range(n):
        x = int(input("Nhập phần tử: "))
        hang = hang + [x]
    a = a + [hang]
# Kiểm tra đối xứng
doi_xung = True

for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] != a[j][i]:
            doi_xung = False
if doi_xung:
    print("Ma trận là ma trận đối xứng")
else:
    print("Ma trận KHÔNG phải là ma trận đối xứng")