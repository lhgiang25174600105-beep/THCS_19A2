tien_gui = float(input("Số tiền gửi: "))
lai_suat = float(input("Lãi suất hàng năm:  "))
# Tính lãi 
lai_1_thang = tien_gui * (lai_suat/100) * (1/12) # 1 tháng bằng 1/12 năm
lai_2_quy = tien_gui * (lai_suat/100) * (1/2) # 1 quý bằng 3 tháng -> 2 quý bằng nửa năm (6/12)
lai_3_nam = tien_gui * (lai_suat/100) * 3
#
print("Số tiền lãi nhận được sau 1 tháng: ", round(lai_1_thang, 2))
print("Số tiền lãi nhận được sau 2 quý là: ", round(lai_2_quy, 2))
print("Số tiền lãi nhận được sau 3 năm là: ", round(lai_3_nam, 2))