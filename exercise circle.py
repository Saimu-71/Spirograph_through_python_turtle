import turtle as t
import random
#Setting random Color
def random_color():

    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)



tom=t.Turtle()
t.colormode(255)#Setting Colormode in RGB
tom.speed("fastest")

def painting_spirograph(size_of_dist):
    for x in range(360//abs(size_of_dist)):
        tom.color(random_color())
        tom.circle(150)
        tom.setheading(tom.heading()+size_of_dist)

painting_spirograph(-3)




















screen=t.Screen()
screen.exitonclick()