# ===== PHẦN 1: Tạo tệp nguồn (chạy 1 lần) =====
with open("tep_nguon.bin", "wb") as f:
    f.write(b"Day la noi dung cua tep nguon")
with open("tep_dich.bin", "wb") as f:
    f.write(b"Day la noi dung cua tep dich")
# ===== PHẦN 2: Sao chép tệp =====
file_nguon = "tep_nguon.bin"
file_dich = "tep_dich.bin"
with open(file_nguon, "rb") as nguon:
    with open(file_dich, "wb") as dich:
        while True:
            dl = nguon.read(1024)
            if dl == b"":
                break

print("Sao chép thành công!")