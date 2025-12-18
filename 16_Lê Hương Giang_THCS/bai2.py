chuoi = input("Nhập vào một chuỗi: ")
n = int(input("Nhập số n: "))
tu = ""        # dùng để ghép từng từ
do_dai = 0 # đếm độ dài của từ
print("Các từ có độ dài lớn hơn", n, "là:")
for ky_tu in chuoi:
    if ky_tu != ' ':          # nếu chưa gặp dấu cách
        tu = tu + ky_tu       # ghép ký tự vào từ
        do_dai = do_dai + 1   # tăng độ dài từ
    else:                     # nếu gặp dấu cách
        if do_dai > n:        # kiểm tra độ dài
            print(tu)
        tu = ""               # reset từ
        do_dai = 0            # reset độ dài
# kiểm tra từ cuối cùng
if do_dai > n:
    print(tu)