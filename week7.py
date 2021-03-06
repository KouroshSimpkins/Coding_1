import turtle as t
import random

def draw_polygon(side_length, number_of_sides):
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        t.forward(side_length)
        t.right(angle)
    
    t.done()

# Implement a random walker using turtle graphics

def random_walk():
    screen = t.Screen()
    screen.setup(1000,1000)
    n = 20
    walkers = []
    for i in range(n):
        walkers.append(t.Turtle())
    for i in range(n):
        walkers[i].color(random.random(), random.random(), random.random())

    for i in range(n):
        walkers[i].penup()
        walkers[i].setpos(0, 0)
        walkers[i].pendown()
        for j in range(150):
            walkers[i].forward(10)
            rotate = random.randint(0, 3)*90
            while rotate == 180:
                rotate = random.randint(0, 3)*90
            walkers[i].right(rotate)

    t.done()

random_walk()