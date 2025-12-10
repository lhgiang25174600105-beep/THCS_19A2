C = float(input("Nhập nhiệt độ độ C: "))
def chuyen_doi_nhiet_do (C):
    F = 1.8*C + 32
    return F
Ket_qua = chuyen_doi_nhiet_do(C)
print(f"{C} độ C chuyển qua độ F là: {Ket_qua} độ F")