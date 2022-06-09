import turtle

RuaXanh = turtle.Turtle()
RuaXanh.shape('turtle')
RuaXanh.penup()
RuaXanh.goto(0,0)
RuaXanh.pendown()
x_RuaXanh=0
y_RuaXanh=0

RuaDo = turtle.Turtle()
RuaDo.shape('turtle')
RuaDo.penup()
RuaDo.goto(100,0)
RuaDo.pendown()
x_RuaDo=100
y_RuaDo=0

RuaDo.speed(1)
RuaXanh.speed(1)
#sobacthang = int(
for bacthang in range(30):
    x_RuaXanh=x_RuaXanh+10
    RuaXanh.setx(x_RuaXanh)
    y_RuaXanh=y_RuaXanh+10
    RuaXanh.sety(y_RuaXanh)

    x_RuaDo=x_RuaDo+20
    RuaDo.setx(x_RuaDo)
    y_RuaDo=y_RuaDo+20
    RuaDo.sety(y_RuaDo)

