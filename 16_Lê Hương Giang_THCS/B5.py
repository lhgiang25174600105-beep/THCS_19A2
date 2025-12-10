n = int(input("Nhập số n: "))
def kiem_tra_so_doi_xung(n):
    s = 0 
    i = n
    if n < 1:
        print("Nhập sai yêu cầu đề bài") 
    else:
        while n>0:
            s = s*10 + n%10
            n = n//10
        return s == i
if kiem_tra_so_doi_xung(n):
    print(n, "Là số đối xứng")
else:
    print(n, "Không là số đối xứng")