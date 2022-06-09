SoA = int(input("Nhập số A "))
SoB = int(input("Nhập số B "))

SoNhoHon = 0
if SoA < SoB:
    SoNhoHon = SoA
else:
    SoNhoHon = SoB

# Tinh UCLN
UCLN = 1
for x in range(SoNhoHon,1,-1):
    if SoA % x == 0 and SoB % x == 0:
        UCLN = x
        break

# Tinh BCNN
BCNN = 1
for x in range(1,SoA*SoB,1):
    BienTam = SoNhoHon*x
    if BienTam % SoA == 0 and BienTam % SoB == 0:
        BCNN = BienTam
        break
print("BCNN ", BCNN)
print("UCLN ", UCLN)
