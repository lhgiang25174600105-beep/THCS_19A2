chuoi = input("Nhập chuỗi kí tự: ")
# Khởi tạo dictionary rỗng để lưu tần suất
tan_suat = {} 
for ky_tu in chuoi:
    if ky_tu in tan_suat:       # Nếu ký tự đã có trong dictionary
        tan_suat[ky_tu] = tan_suat[ky_tu] + 1
    else:                       # Nếu ký tự chưa có, khởi tạo giá trị 1
        tan_suat[ky_tu] = 1
print("Tần suất xuất hiện của các ký tự:")
for ky_tu in tan_suat:
    print(ky_tu, ":", tan_suat[ky_tu])