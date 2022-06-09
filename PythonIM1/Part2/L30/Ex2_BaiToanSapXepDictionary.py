PIM1 = {
    'STT1'  : 5,
    'STT2'  : 9,
    'STT3'  : 4,
    'STT4'  : 7,
    'STT5'  : 8,
}
sorted_values = sorted(PIM1.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in PIM1.keys():
        if PIM1[k] == i:
            sorted_dict[k] = PIM1[k]
            break

print(sorted_dict)