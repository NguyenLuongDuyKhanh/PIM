import time
import turtle

def Thuc_Hien_Khi_Nhan_Space():
    print("Bạn đã nhấn space")

def Thuc_Hien_Khi_Tha_Space():
    print("Bạn đã thả space")

# setting up screen
s = turtle.Screen()
s.setup(450, 900)
s.bgcolor("black")
s.title("turtle racing 2")

s.onkeypress(Thuc_Hien_Khi_Nhan_Space, "space")
s.onkeyrelease(Thuc_Hien_Khi_Tha_Space, "space")

s.listen()
