import random
import turtle

def snake_game():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Snake head
    head = turtle.Turtle()
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "Right"

    # Function to move the snake
    def move():
        if head.direction == "Up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "Down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "Right":
            x = head.xcor()
            head.setx(x + 20)

        if head.direction == "Left":
            x = head.xcor()
            head.setx(x - 20)

    # Keyboard bindings
    def go_up():
        if head.direction != "Down":
            head.direction = "Up"

    def go_down():
        if head.direction != "Up":
            head.direction = "Down"

    def go_right():
        if head.direction != "Left":
            head.direction = "Right"

    def go_left():
        if head.direction != "Right":
            head.direction = "Left"

    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_right, "Right")
    screen.onkey(go_left, "Left")

    # Main game loop
    while True:
        screen.update()
        move()
        turtle.delay(100)  # Adjust speed

snake_game()