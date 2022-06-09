import turtle
import random
tur = turtle.Turtle()
print("1. Vuong")
print("2. Tron")
print("3. Tam giac")
hinh = input("Nhap vao hinh muon ve: ")
x = random.randint(20,40)
if hinh == "Vuong" or int(hinh) == 1:
    for i in range(4):
        tur.forward(x)
        tur.left(90)
elif hinh == "TamGiac" or int(hinh) == 2:
    for i in range(3):
        tur.forward(x)
        tur.left(120)
elif hinh == "Tron" or int(hinh) == 3:
    tur.circle(x)
