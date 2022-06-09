PIM1 = {
    'STT1'  : 5,
    'STT2'  : 9,
    'STT3'  : 4,
    'STT4'  : 7,
    'STT5'  : 8,
}

SoNho = PIM1['STT1']
for x in PIM1:
    if PIM1[x] < SoNho:
        SoNho = PIM1[x]
print("Diem so nho nhat trong lop: ", SoNho)

SoLon = PIM1['STT1']
for x in PIM1:
    if PIM1[x] > SoLon:
        SoLon = PIM1[x]
print("Diem so lon nhat trong lop: ", SoLon)