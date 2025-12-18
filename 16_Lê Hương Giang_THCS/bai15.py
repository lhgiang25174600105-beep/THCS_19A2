n = int(input("Nhập số lượng phần tử trong tuple: "))
t = ()  # Khởi tạo tuple rỗng
for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i+1) + ": "))
    t = t + (x,)
so_chan = ()
so_le = ()

for k in t:
    if k % 2 == 0:# Nếu chia hết cho 2 → số chẵn
        so_chan = so_chan + (k,)
    else:# Ngược lại → số lẻ
        so_le = so_le + (k,)

# Tính tổng các phần tử trong mỗi tuple bằng vòng lặp
tong_chan = 0
for k in so_chan:
    tong_chan = tong_chan + k

tong_le = 0
for k in so_le:
    tong_le = tong_le + k

print("Tuple ban đầu:", t)
print("Tuple chứa số chẵn:", so_chan, "và tổng:", tong_chan)
print("Tuple chứa số lẻ:", so_le, "và tổng:", tong_le)