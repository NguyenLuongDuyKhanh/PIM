DaySo = [4, 1, 5, 9, 3, 6]
DaySoTuBeDenLon = []

DaySoTuBeDenLon.append(min(DaySo))
print("Day so sau khi sap xep: ", DaySoTuBeDenLon)

# DaySo - > [5, 9, 3, 6]
DaySo.remove(min(DaySo))
DaySoTuBeDenLon.append(min(DaySo))
print("Day so sau khi sap xep: ", DaySoTuBeDenLon)

# DaySo - > [5, 9, 6]
DaySo.remove(min(DaySo))
DaySoTuBeDenLon.append(min(DaySo))
print("Day so sau khi sap xep: ", DaySoTuBeDenLon)

DaySo.remove(min(DaySo))
DaySoTuBeDenLon.append(min(DaySo))
print("Day so sau khi sap xep: ", DaySoTuBeDenLon)

DaySo.remove(min(DaySo))
DaySoTuBeDenLon.append(min(DaySo))
print("Day so sau khi sap xep: ", DaySoTuBeDenLon)