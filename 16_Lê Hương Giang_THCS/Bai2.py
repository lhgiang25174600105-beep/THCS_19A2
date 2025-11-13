keo = int(input("Tổng số kẹo: "))
hocsinh = int(input("Số học sinh: "))
# 
so_keo_moi_hoc_sinh = keo // hocsinh
so_keo_con_thua = keo % hocsinh
#
print("Số kẹo mỗi học sinh nhận được: ", so_keo_moi_hoc_sinh)
print("Số kẹo còn thừa: ", so_keo_con_thua)
