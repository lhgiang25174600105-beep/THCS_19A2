n = int(input("Nhập số lượng: "))

tong_chan = 0
tong_le = 0

for i in range(n):
    x = int(input("Nhập số: "))

    if x % 2 == 0:
        tong_chan = tong_chan + x
    else:
        tong_le = tong_le + x

print("Tổng các số chẵn:", tong_chan)
print("Tổng các số lẻ:", tong_le)