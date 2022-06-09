import turtle
tina = turtle.Turtle()
tina.pensize(5)

print("V. Hình vuông")
print("T. Hình tròn")
LuaChon = input("Nhập lựa chọn của bạn (t/v): ")

if LuaChon == "T" or LuaChon == "t":
    BanKinh = int(input("Nhập bán kính: "))
    tina.circle(BanKinh)
    print("Chu vi đường tròn là: ", round(2*3.14*BanKinh,2))
    print("Diện tích hình tròn là: ", round(3.14*BanKinh*BanKinh,2))

#Xử lý khi người dùng chọn hình vuông
elif LuaChon == "V" or LuaChon == "v":
    Canh = int(input("Nhập cạnh hình vuông: "))
    for x in range(4):
        tina.forward(Canh)
        tina.left(90)
    print("Chu vi hình vuông là: ", Canh*4)
    print("Diện tích hình vuông là: ", Canh*Canh)
