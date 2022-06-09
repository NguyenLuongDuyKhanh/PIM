import time
import turtle

#A
def Thuc_Hien_Khi_Nhan_A():
    print("bạn đã nhấn A")

def Thuc_Hien_Khi_Tha_A():
    print("Bạn đã thả A")

#B
def Thuc_Hien_Khi_Nhan_B():
    print("bạn đã nhấn B")

def Thuc_Hien_Khi_Tha_B():
    print("Bạn đã thả B")

#C
def Thuc_Hien_Khi_Nhan_C():
    print("bạn đã nhấn C")

def Thuc_Hien_Khi_Tha_C():
    print("Bạn đã thả C")

#D
def Thuc_Hien_Khi_Nhan_D():
    print("bạn đã nhấn D")

def Thuc_Hien_Khi_Tha_D():
    print("Bạn đã thả D")

# setting up screen
s = turtle.Screen()
s.setup(450, 900)
s.bgcolor("black")
s.title("turtle racing 2")
s.tracer(1)

#A
s.onkeypress(Thuc_Hien_Khi_Nhan_A, "a")
s.onkeyrelease(Thuc_Hien_Khi_Tha_A, "a")

#B
s.onkeypress(Thuc_Hien_Khi_Nhan_B, "b")
s.onkeyrelease(Thuc_Hien_Khi_Tha_B, "b")

#C
s.onkeypress(Thuc_Hien_Khi_Nhan_C, "c")
s.onkeyrelease(Thuc_Hien_Khi_Tha_C, "c")

#D
s.onkeypress(Thuc_Hien_Khi_Nhan_D, "d")
s.onkeyrelease(Thuc_Hien_Khi_Tha_D, "d")
s.listen()
