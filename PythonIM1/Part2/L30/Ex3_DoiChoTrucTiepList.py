numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
lenth = len(numbers)

for x in range(0, lenth - 1):
    for y in range(x + 1, lenth):
        if (numbers[x] > numbers[y]):

            sort = numbers[x]
            numbers[x] = numbers[y]
            numbers[y] = sort

print(numbers)