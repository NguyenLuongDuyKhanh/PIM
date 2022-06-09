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
