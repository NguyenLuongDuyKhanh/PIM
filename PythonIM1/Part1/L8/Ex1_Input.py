import turtle
tina = turtle.Turtle()
tina.shape('turtle')

Buoc_tangx=0
Buoc_tangy=0
for i in range(10):
    Buoc_tangy = Buoc_tangy + 50
    tina.sety(Buoc_tangy)
    Buoc_tangx = Buoc_tangx +50
    tina.setx(Buoc_tangx)
