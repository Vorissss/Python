import turtle
import random


screen = turtle.Screen()
screen.title("🌟 Golden tree")
screen.bgcolor("black")
screen.setup(width=800, height=600)
turtle.colormode(255)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)


def draw_branch(length, t):
    if length < 10:
        t.color((255, 215, 0))
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        return
    else:
        t.color((139, 69, 19))
        t.forward(length)

        angle = random.randint(20, 35)
        scale = random.uniform(0.6, 0.8)

        t.left(angle)
        draw_branch(length * scale, t)
        t.right(angle * 2)
        draw_branch(length * scale, t)
        t.left(angle)

        t.backward(length)


t.penup()
t.goto(0, -250)
t.pendown()
t.left(90)
draw_branch(120, t)

leaves = turtle.Turtle()
leaves.hideturtle()
leaves.speed(0)
leaves.penup()

for _ in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-50, 200)
    leaves.goto(x, y)
    brightness = random.randint(200, 255)
    leaves.dot(random.randint(6, 12), (brightness, 215, 0))

turtle.done()