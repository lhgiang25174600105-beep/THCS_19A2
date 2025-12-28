def dao_nguoc_chuoi(chuoi):
    chuoi_dao = " "
    for i in chuoi:
        chuoi_dao = i + chuoi_dao
    return chuoi_dao
def dem_so_tu(chuoi):
    tu = chuoi.split()
    return len(tu)