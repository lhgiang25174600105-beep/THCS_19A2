with open("vanban.txt", "r", encoding="utf-8") as f:
    nd = f.read()
cac_tu = nd.split()
tan_suat = {}
# Duyệt qua từng từ
for i in cac_tu:
    # Chuyển về chữ thường để tránh trùng (Python và python)
    i = i.lower()
    # Nếu từ đã có trong từ điển
    if i in tan_suat:
        tan_suat[i] += 1
    else:
        tan_suat[i] = 1
print("Tần suất xuất hiện của các từ:\n")
for i, so_lan in tan_suat.items():
    print(f"{i} : {so_lan}")