PIM1 = ['An', 'Luan', 'Minh', 'Tuan', 'Vi']
print(PIM1)
TenCanTim = input('Nhap ten can tim: ')
check = False

for x in PIM1:
    if x == TenCanTim:
        check = True
        print("Tim thay", TenCanTim, "o vi tri", PIM1.index(x))
        break

if check == False:
    print('Khong tim thay ',TenCanTim)