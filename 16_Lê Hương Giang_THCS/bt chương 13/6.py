import csv
with open("nhan_vien.txt", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID","Tên", "Lương"])
    writer.writerow([1, "NVA", 60000])
    writer.writerow([2,"NVB", 70000])
    writer.writerow([3, "NVC", 80000])
    writer.writerow([4, "NVD", 90000])
with open("nhan_vien.txt", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for dong in reader:
        luong = int(dong["Lương"])
        if luong > 50000:
            print(
                "ID", dong["ID"],
                "-Tên", dong["Tên"],
                "-Lương", dong["Lương"]
            )
