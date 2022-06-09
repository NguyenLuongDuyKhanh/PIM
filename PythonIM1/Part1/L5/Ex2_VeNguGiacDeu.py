# Write your code here :-)
import turtle
tina = turtle.Turtle()
tina.shape('classic')

so_canh_ngu_giac = 5
goc_ngu_giac = 180-108
do_dai_canh_ngu_giac = 50

so_canh_luc_giac = 6
goc_luc_giac = 180-120
do_dai_canh_luc_giac = 50

so_canh_bat_giac = 8
goc_bat_giac = 180-135
do_dai_canh_bat_giac = 50

#Vẽ ngũ giác
tina.penup()
tina.goto(0,0)
tina.pendown()
for canh in range(so_canh_ngu_giac): # số cạnh
    tina.forward(do_dai_canh_ngu_giac)
    tina.left(goc_ngu_giac)

tina.penup()
tina.goto(150,0)
tina.pendown()
for canh in range(so_canh_luc_giac):
    tina.forward(do_dai_canh_luc_giac)
    tina.left(goc_luc_giac)

tina.penup()
tina.goto(300,0)
tina.pendown()
for canh in range(so_canh_bat_giac):
    tina.forward(do_dai_canh_bat_giac)
    tina.left(goc_bat_giac)

turtle.done()
