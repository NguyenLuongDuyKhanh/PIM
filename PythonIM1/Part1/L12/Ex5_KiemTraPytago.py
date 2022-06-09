Canh_Huyen = int(input("Nhập số đo cạnh a: "))
Canh_Goc_Vuong_1 = int(input("Nhập số đo canh b: "))
Canh_Goc_Vuong_2 = int(input("Nhập số đo cạnh c: "))


if Canh_Huyen*Canh_Huyen == Canh_Goc_Vuong_1*Canh_Goc_Vuong_1 + Canh_Goc_Vuong_2*Canh_Goc_Vuong_2:
    print("Tam giác vuông")
else:
    print("Tam giác không vuông")
