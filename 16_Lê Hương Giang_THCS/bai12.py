# Nhập kích thước ma trận A
m = int(input("Nhập số hàng của A: "))
n = int(input("Nhập số cột của A: "))

# Nhập kích thước ma trận B
p = int(input("Nhập số hàng của B: "))
q = int(input("Nhập số cột của B: "))

# Kiểm tra điều kiện nhân
if n != p:
    print("Không thể nhân hai ma trận này")
else:
    # Nhập ma trận A
    A = []
    for i in range(m):
        hang = []
        for j in range(n):
            x = int(input("Nhập phần tử A: "))
            hang = hang + [x]
        A = A + [hang]

    # Nhập ma trận B
    B = []
    for i in range(p):
        hang = []
        for j in range(q):
            x = int(input("Nhập phần tử B: "))
            hang = hang + [x]
        B = B + [hang]

    # Khởi tạo ma trận kết quả C
    C = []
    for i in range(m):
        hang = []
        for j in range(q):
            hang = hang + [0]
        C = C + [hang]

    # Nhân hai ma trận
    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    # In ma trận kết quả
    print("Ma trận kết quả:")
    for i in range(m):
        for j in range(q):
            print(C[i][j], end=" ")
        print()