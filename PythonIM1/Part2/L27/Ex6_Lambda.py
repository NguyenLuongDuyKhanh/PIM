a = [45,89,1,2,0]
print("List trước khi chọn lọc: ", a)

print("Chọn ra các phần tử lớn hơn 10: ")
list_moi = list(filter(lambda a: a > 10,a))
print(list_moi)

print("Chọn ra các phần tử chia hết cho 2: ")
list_moi = list(filter(lambda a: a % 2 == 0,a))
print(list_moi)

print("Nhân 2 tất cả các phần tử: ")
list_moi = list(map(lambda a: a*2,a))
print(list_moi)