Tuoi_Cua_Minh = 12
Tuoi_Cua_Ban = int(input("Bạn bao nhiêu tuổi? "))

if Tuoi_Cua_Ban > Tuoi_Cua_Minh:
    #Chỉ được thực hiện khi điều kiện ở dòng 4 đúng
    print("Bạn lớn tuổi hơn mình")
elif Tuoi_Cua_Ban < Tuoi_Cua_Minh: #-> else if
    #Chỉ được thực hiện khi điều kiện ở dòng 4 sai
    print("Bạn nhỏ tuổi lơn mình")
else:
    print("Ban bang tuoi minh")
