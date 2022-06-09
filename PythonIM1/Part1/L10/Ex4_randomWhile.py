import turtle
import random
kathy = turtle.Turtle()

So_buoc_can_di = random.randint(0,10)
kathy.write("Toi sẽ di " + str(So_buoc_can_di) + " buoc")

So_buoc_da_di = 0
while(So_buoc_da_di<So_buoc_can_di):
    kathy.forward(5)
    So_buoc_da_di=So_buoc_da_di+1
