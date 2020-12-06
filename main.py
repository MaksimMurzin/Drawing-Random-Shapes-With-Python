from turtle import Turtle, Screen
import random

timmy = Turtle()


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
# timmy.width(5)
#
# for _ in range(200):
#     change_color()
#     timmy.forward(random.randint(10,50))
#     timmy.setheading(random.choice([0, 90, 180, 270]))
#
#

# ==============================Draw a dick ===============================
# timmy.circle(20)
# timmy.forward(100)
# timmy.circle(-20,180)
# timmy.forward(100)
# timmy.circle(20)
#
#

# =========== make a Spirograph ======================

def draw_spirograph(number_of_circles):
    timmy.speed(10)
    change_color()
    timmy.circle(50)
    timmy.setheading(timmy.heading() + 360 / number_of_circles)


for _ in range(20):
    draw_spirograph(20)



screen = Screen()
screen.exitonclick()

