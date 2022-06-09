DaySo = [1,4,3,7,9,5]
SoNho = DaySo[0]
SoLon = DaySo[0]

for x in DaySo:
    if x > SoLon:
        SoLon = x

for x in DaySo:
    if x < SoNho:
        SoNho = x
print("Phần tử lớn nhất trong List: ", SoLon)
print("Phần tử nhỏ nhất trong List: ", SoNho)