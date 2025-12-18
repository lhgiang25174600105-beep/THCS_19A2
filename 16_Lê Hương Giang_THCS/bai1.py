chuoi = input("Nhập vào một chuỗi: ")
dem_so_luong_ki_tu_chu_cai = 0
dem_so_luong_ki_tu_chu_so = 0
dem_so_luong_ki_tu_dac_biet = 0
for ky_tu in chuoi:
    if ("a" <= ky_tu <= "z") or ("A" <= ky_tu <= "Z"): # 1 trong hai đúng sẽ chạy
        dem_so_luong_ki_tu_chu_cai = dem_so_luong_ki_tu_chu_cai + 1
    elif "0" <= ky_tu <= "9":
        dem_so_luong_ki_tu_chu_so = dem_so_luong_ki_tu_chu_so + 1
    else:
        dem_so_luong_ki_tu_dac_biet = dem_so_luong_ki_tu_dac_biet + 1
print ("Số lượng kí tự chữ cái là: ", dem_so_luong_ki_tu_chu_cai)
print ("Số lượng kí tự chữ số là: ", dem_so_luong_ki_tu_chu_so)
print ("Số lượng kí tự đặc biệt: ",dem_so_luong_ki_tu_dac_biet)