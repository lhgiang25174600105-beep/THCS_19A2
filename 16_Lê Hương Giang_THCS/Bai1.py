giasanpham = float(input("giá sản phẩm: "))
soluongmua = int(input("số lượng mua : "))
# Tính
tienhang = giasanpham * soluongmua
thue = tienhang * 0.10
tongtien = tienhang + thue
# In ra 
print("Tiền hàng: ", round(tienhang, 2))
print("Thuế: ", round(thue, 2))
print("Tổng tiền trả: ", round(tongtien, 2))