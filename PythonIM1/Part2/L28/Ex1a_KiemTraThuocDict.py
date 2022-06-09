PIM1 = {
    'STT1'  : 'An',
    'STT2'  : 'Luan',
    'STT3'  : 'Minh',
    'STT4'  : 'Tuan',
    'STT5'  : 'Vi'
}

TenCanKiemTra = input("Nhap ten can kiem tra: ")
check = False
for x in PIM1:
    if PIM1[x] == TenCanKiemTra:
        check = True
        break

if check:
    print(TenCanKiemTra, 'thuoc Dictionary')
else:
    print(TenCanKiemTra, 'khong thuoc Dictionary')