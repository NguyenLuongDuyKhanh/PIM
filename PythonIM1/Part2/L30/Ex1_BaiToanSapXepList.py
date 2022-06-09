DaySo = [45,89,1,2,0]

DaySoTuBeDenLon = []
while DaySo:
    Sobe = DaySo[0]
    for x in DaySo:
        if x < Sobe:
            Sobe = x
    DaySoTuBeDenLon.append(Sobe)
    DaySo.remove(Sobe)
print(DaySoTuBeDenLon)


DaySo = [45,89,1,2,0]

DaySoTuLonDenBe = []
while DaySo:
    Solon = DaySo[0]
    for x in DaySo:
        if x > Solon:
            Solon = x
    DaySoTuLonDenBe.append(Solon)
    DaySo.remove(Solon)
print(DaySoTuLonDenBe)