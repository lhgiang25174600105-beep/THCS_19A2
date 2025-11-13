ten_dang_nhap = input("Tên đăng nhâp: ")
mk = input("Mật khẩu: ")
# 
cond1 = ten_dang_nhap == "admin"
cond2 = mk != "password123"
#
print("Có được quyền truy cập? : ", cond1 and cond2)