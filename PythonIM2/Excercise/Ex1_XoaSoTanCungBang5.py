lst = [2, 4, 5, 11, 35, 43, 105]
# -> [2, 4, 11, 43]
for x  in lst:
    if x % 3 == 0:
        lst.remove(x)

print(lst)