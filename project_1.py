
import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(900, 700)

t = turtle.Turtle()
t.speed(6)
t.pensize(5)

# Create a separate turtle for the rainbow
alex = turtle.Turtle()

# Rainbow
rainbow_colors = ["violet", "indigo", "blue","green", "yellow", "orange", "red"]
radius = 120
radius_increase = 15
alex.speed(15)
alex.pensize(18)
alex.up()
alex.left(90)
for rainbow_color in rainbow_colors:
     alex.color(rainbow_color)
     alex.goto(-radius, -100)
     alex.down()
     alex.circle(-radius,180)
     alex.up()
     alex.left(180)
     radius = radius + radius_increase

alex.hideturtle()

# Move without drawing
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# Draw a circle
def circle(x, y, r, color):
    move(x, y - r)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


# Shoulders (semicircle)
move(-100, -150)
t.fillcolor("white")
t.begin_fill()
t.forward(200)
t.left(90)
t.circle(100, 180)
t.end_fill()


# Left ear
move(-65, 50)
t.fillcolor("white")
t.begin_fill()
t.goto(-55, 130)
t.goto(-10, 75)
t.goto(-65, 50)
t.end_fill()


# Right ear
move(10, 75)
t.begin_fill()
t.goto(55, 130)
t.goto(65,50)
t.goto(10, 75)
t.end_fill()


# Head
circle(0, 0, 80, "white")


# Eyes
circle(-30, 10, 7, "black")
circle(30, 10, 7, "black")


# Nose
move(-7, -25)
t.fillcolor("pink")
t.begin_fill()
t.goto(7, -25)
t.goto(0, -35)
t.goto(-7, -25)
t.end_fill()


# Whiskers
for y in [-30, -40, -50]:
    move(-25, y)
    t.goto(-95, y)

    move(25, y)
    t.goto(95, y)


# Name
move(0, -190)
t.write("Oliver", align="center", font=("Arial", 18, "bold"))


screen.exitonclick()
