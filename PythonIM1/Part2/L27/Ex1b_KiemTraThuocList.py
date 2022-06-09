PIM1 = ['An', 'Luan', 'Minh', 'Tuan', 'Vi']
print(PIM1)
TenCanKiemTra = input('Nhap ten can tim: ')

if TenCanKiemTra in PIM1:
    print(TenCanKiemTra,"thuoc PIM1")
elif TenCanKiemTra not in PIM1:
    print(TenCanKiemTra,"khong thuoc PIM1")