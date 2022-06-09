number = 147852

donvi = number % 10
chuc = number // 10 % 10
tram = number // 100 % 10
nghin = number // 1000 % 10
chucnghin = number // 10000 % 10
tramnghin = number // 100000 % 10

print(donvi)
print(chuc)
print(tram)
print(nghin)
print(chucnghin)
print(tramnghin)

donvi = number % 10
chuc = int((number % 100) / 10)
tram = int((number % 1000) / 100)
nghin = int((number % 10000) / 1000)
chucnghin = int((number % 100000) / 10000)
tramnghin = int((number % 1000000) / 100000)

print(donvi)
print(chuc)
print(tram)
print(nghin)
print(chucnghin)
print(tramnghin)