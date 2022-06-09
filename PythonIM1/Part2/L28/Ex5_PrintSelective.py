PIM1 = {
    'STT1'  : 5,
    'STT2'  : 9,
    'STT3'  : 4,
    'STT4'  : 7,
    'STT5'  : 8,
}
print("Danh sach lop ban dau: ", PIM1)
DanhSachCacBanTrenTrungBinh = {}
for x in PIM1:
    if PIM1[x] > 5:
        DanhSachCacBanTrenTrungBinh[x]=PIM1[x]
print("Danh sach cac ban tren trung binh", DanhSachCacBanTrenTrungBinh)

DanhSachCacBanCoDiemChan = {}
for x in PIM1:
    if PIM1[x] % 2 == 0:
        DanhSachCacBanCoDiemChan[x]=PIM1[x]
print("Danh sach cac ban co diem so chan", DanhSachCacBanCoDiemChan)