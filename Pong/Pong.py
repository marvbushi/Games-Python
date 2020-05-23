import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of the animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of the animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of the animation
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 # everytime the ball moves it moves by 2px
ball.dy = -2 # everytime the ball moves it moves by 2px

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
# update score
def update_score():
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

def play_sound():
    winsound.Beep(1000, 5) # pong sound

# paddle_a
def paddle_a_up():
    y_cor = paddle_a.ycor()
    y_cor += 20
    paddle_a.sety(y_cor)

def paddle_a_down():
    y_cor = paddle_a.ycor()
    y_cor -= 20
    paddle_a.sety(y_cor)

# paddle_b
def paddle_b_up():
    y_cor = paddle_b.ycor()
    y_cor += 20
    paddle_b.sety(y_cor)

def paddle_b_down():
    y_cor = paddle_b.ycor()
    y_cor -= 20
    paddle_b.sety(y_cor)

# Kayboard binding
wn.listen() # listen for keyboard input
wn.onkeypress(paddle_a_up, "w") # when the user press lower "w" call function paddle_a_up
wn.onkeypress(paddle_a_down, "s") # when the user press lower "s" call function paddle_a_down

wn.onkeypress(paddle_b_up, "Up") # when the user press arrow up call function paddle_b_up
wn.onkeypress(paddle_b_down, "Down") # when the user press arrow down call function paddle_b_down


# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking top - bottom
    # once it gets to certain point we need it to bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        play_sound()
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        play_sound()

    # border checking left - right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        update_score()
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        update_score()

    # paddle_a and ball collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        play_sound()

    # paddle_b and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        play_sound()

    