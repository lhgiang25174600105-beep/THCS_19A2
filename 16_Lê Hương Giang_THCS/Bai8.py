can_nang = float(input("Cân nặng (kg): "))
chieu_cao = float(input("Chiều cao (m): "))
BIM = can_nang / (chieu_cao * chieu_cao)
print("Kết quả BIM: ", round(BIM, 2))