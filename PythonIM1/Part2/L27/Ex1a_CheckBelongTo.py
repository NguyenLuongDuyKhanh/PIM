PIM1 = ['An', 'Luan', 'Minh', 'Tuan', 'Vi']
TenCanKiemTra = input("Nhap ten can kiem tra: ")

Check = False

for x in PIM1:
    if x == TenCanKiemTra:
        Check = True

if Check == True:
    print(TenCanKiemTra, "thuoc lop PIM1")
else:
    print(TenCanKiemTra, "khong thuoc lop PIM1")
