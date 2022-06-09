# Write your code here :-)
import turtle
tina = turtle.Turtle()
tina.shape('turtle')
theBigestPoint=950

tina.goto(theBigestPoint,theBigestPoint)
tina.goto(-theBigestPoint,theBigestPoint)
tina.goto(theBigestPoint,-theBigestPoint)
tina.goto(-theBigestPoint,-theBigestPoint)
tina.goto(0,0)

tina.write("               This is how big my grid is!")
