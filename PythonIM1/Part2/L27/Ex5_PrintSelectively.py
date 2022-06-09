a = [45,89,1,2,0]
print("List trước khi chọn lọc: ", a)

print("Chọn ra các phần tử lớn hơn 10: ")
for x in a:
    if x > 10:
        print(x)

print("Chọn ra các phần tử chia hết cho 2: ")
for x in a:
    if x % 2 == 0:
        print(x)
