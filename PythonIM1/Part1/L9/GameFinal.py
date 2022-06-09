# các module cần thiết
from turtle import *
from random import randint

# thiết lập cho chú rùa có dạng mũi tên là chú rùa có nhiệm vụ vẽ đường đua
speed(0)
penup()
goto(-140, 140)

# tạo các vạch đua
for step in range(15):
  write(step, align='center')
  right(90)

  # mỗi vạch đua vẽ 8 nét
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)

  penup()
  backward(160)
  left(90)
  forward(20)

# tạo chú rùa thứ 1
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')

# đưa chú rùa đến vạch xuất phát
player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()

# rồi cho xoay 360 độ
for turn in range(10):
  player_1.right(36)

# chú rùa thứ 2
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')

# đưa chú rùa thứ 2 về vạch xuất phát
player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()

# rồi cho xoay 360 độ
for turn in range(72):
  player_2.left(5)

# tạo chú rùa thứ 3
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')

# đưa chú rùa thứ 3 về vạch xuất phát
player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()

# rồi cho xoay 360 độ
for turn in range(60):
  player_3.right(6)

# tạo chú rùa thứ 4
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('orange')

# đưa chú rùa thứ 4 về vạch xuất phát
player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()

# rồi cho xoay 360 độ
for turn in range(30):
  player_4.left(12)

# tiến hành đua
for turn in range(100):
  player_1.forward(randint(1, 5))
  player_2.forward(randint(1, 5))
  player_3.forward(randint(1, 5))
  player_4.forward(randint(1, 5))
