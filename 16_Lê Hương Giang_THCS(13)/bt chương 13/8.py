import os

os.mkdir("temp_files")

file_cu = "temp_files/file.txt"
with open(file_cu, "w", encoding="utf-8") as f:
    f.write("Day la tap tin tam thoi")

file_moi = "temp_files/new_file.txt"
os.rename(file_cu, file_moi)

os.rename(file_moi, "new_file.txt")

os.rmdir("temp_files")

print("Hoàn thành các thao tác!")