DaySo = [1, 5, 9, 3, 6]
DaySoTuBeDenLon = []

while DaySo:
    DaySoTuBeDenLon.append(min(DaySo))
    DaySo.remove(min(DaySo))

print(DaySoTuBeDenLon)