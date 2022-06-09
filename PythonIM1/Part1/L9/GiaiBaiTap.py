import turtle
tina = turtle.Turtle()
tina.shape('turtle')
tina.penup()
tina.pendown()
so_buoc = int(input("alo alo alo  "))
buoc_tangx=0
buoc_tangy=0
for x in range (so_buoc) :
    buoc_tangy=buoc_tangy+20
    tina.sety(buoc_tangy)
    buoc_tangx=buoc_tangx+20
    tina.setx(buoc_tangx)

import turtle
o= turtle.Turtle()
o.shape('turtle')
o.penup()
o.setx(-200)
o.pendown()
so_buoc = int(input("alo alo alo  "))

tangx=-200
tangy=20
for c in range (so_buoc) :
    tangy=tangy+20
    o.sety(tangy)
    tangx=tangx+20
    o.setx(tangx)
