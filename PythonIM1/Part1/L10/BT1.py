import turtle
import random

mau_sac = ['red','green','blue','black','gray','yellow']

kathy = turtle.Turtle()
kathy.penup()
kathy.shape('turtle')
toa_dox_kathy=random.randint(-300,300)
toa_doy_kathy=random.randint(-300,300)
kathy.goto(toa_dox_kathy,toa_doy_kathy)
kathy.color(random.choice(mau_sac))

jack = turtle.Turtle()
jack.penup()
jack.shape('turtle')
toa_dox_jack=random.randint(-300,300)
toa_doy_jack=random.randint(-300,300)
jack.goto(toa_dox_jack,toa_doy_jack)
jack.color(random.choice(mau_sac))

felix = turtle.Turtle()
felix.penup()
felix.shape('turtle')
toa_dox_felix=random.randint(-300,300)
toa_doy_felix=random.randint(-300,300)
felix.goto(toa_dox_felix,toa_doy_felix)
felix.color(random.choice(mau_sac))
