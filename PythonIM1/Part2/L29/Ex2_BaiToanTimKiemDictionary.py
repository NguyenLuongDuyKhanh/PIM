PIM1 = {
    'STT1' : 'An',
    'STT2' : 'Luan',
    'STT3' : 'Minh',
    'STT4' : 'Tuan',
    'STT5' : 'Vi'
}
TenCanTim = input("Nhap ten can tim: ")
check = False

for x in PIM1:
    if TenCanTim == PIM1[x]:
        check = True
        print("Tim thay ", TenCanTim, "o vi tri",x)
        break

if check == False:
    print("Khong tim thay ", TenCanTim)