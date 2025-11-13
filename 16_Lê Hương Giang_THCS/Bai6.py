nam = int(input("Nhập năm: "))
cond1 = nam % 400 == 0
cond2 = nam % 4 == 0
cond3 = nam % 100 != 0
print(nam)
print("Là năm nhuận? :", cond1 or (cond2 and cond3))