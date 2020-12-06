from turtle import Turtle, Screen
import random

timmy = Turtle()
#
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)

#
# for sides in range(3,11):
#     turn_angle = 360/sides
#     change_color()
#     for side in range(sides):
#         timmy.forward(100)
#         timmy.right(turn_angle)
#
#


# ==============================random walk ====================================
timmy.width(3)

for _ in range(50):
    change_color()
    timmy.forward(random.randint(10,50))
    timmy.setheading(random.choice([0, 90, 180, 270]))




# ==============================Draw a dick
# timmy.circle(20)
# timmy.forward(100)
# timmy.circle(-20,180)
# timmy.forward(100)
# timmy.circle(20)
#
#
# screen = Screen()
# screen.exitonclick()