import sys
import os
import sys
import os
thu_vien_chung = r"C:\Users\poror\thcs19a2\BT chương 12\bài 5\thu_vien_chung"
sys.path.append(thu_vien_chung)
import xu_ly_so
so = 13
if xu_ly_so.kiem_tra_so_nguyen_to(so):
    print(so, "là số nguyên tố")
else:
    print(so, "không phải là số nguyên tố")
