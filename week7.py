import turtle as t
import random

def draw_polygon(side_length, number_of_sides):
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        t.forward(side_length)
        t.right(angle)
    
    t.done()

#draw_polygon(100, 5)

# Implement a random walker using turtle graphics

screen = t.Screen()
screen.setup(1000,1000)
walkers = []
n = 20
for i in range(n):
    walkers.append(t.Turtle())
for i in range(n):
    walkers[i].color((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))

def random_walk():
    for i in range(n):
        angle = random.randint(0,3)*90
        walkers[i].right(angle)
        walkers[i].forward(10)
    screen.update()
    screen.ontimer(random_walk, 1000//20)

random_walk()