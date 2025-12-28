ds = [1, 3, 5, 7, 9, 11, 12]
with open("so_nguyen.txt", "w", encoding="utf-8") as f:
    for so in ds:
        f.write(str(so)+"\n")
print("Đã ghi danh sách")