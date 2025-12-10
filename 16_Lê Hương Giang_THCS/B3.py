n = int(input("Nhập số n: "))
def kiem_tra_so_armstrong(n):
    #chuyển số thành chuỗi để lấy từng chữ số
    c = str(n) #vd: 153 tách ra thành "1" "5" "3"
    #lấy từng chữ số, nâng lên lũy thừa
    t=0
    #tạo biến t, bắt đầu bằng 0
    for i in c: # lặp qua từng kí hiệu c 
                # vd: bắt đầu từ "1" -> i ="1" rồi i="5" cuối cùng i="3"
        t += int(i)**3 # c = c + int(i)**3
    return t == n 
if kiem_tra_so_armstrong(n):
    print(n, "TRUE")
else:
    print(n, "FALSE")