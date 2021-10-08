#Learning python by developing games
#1. pingpong game

#turtle module is used for graphics, game design
import turtle
# from turtle import *

window = turtle.Screen()
window.title("PingPong :)")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#score 
score_a = 0
score_b = 0

#paddle 1
paddle_a = turtle.Turtle() #creates object of class Turtle
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0);

#paddle 2
paddle_b = turtle.Turtle() #creates object of class Turtle
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0);

#ball
ball = turtle.Turtle() #creates object of class Turtle
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#speed of the ball movement, moves by 0.2 pixels, decide based on the speed of your system 
ball.dx = 0.14
ball.dy = 0.14

#Pen turtle object for score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 18, "normal"))

###moving the paddle up and down
#moving paddle a using w,s keys
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)


#moving paddle b using arrow keys
def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

#keyboard binding 
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


#Main game loop, here is the motions which game does on its own
while True:
	window.update() #whenever opens first update, 

	#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#border checking
	#top and bottom border
	if ball.ycor() > 290:
		ball.sety(290) #reverse direction
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290) #reverse direction
		ball.dy *= -1

	#if goes outside left or right, bring back to center
	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		#if hits right side, A scores 1 point
		score_a += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 18, "normal"))

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1 #basically reverses direction 
		score_b += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 18, "normal"))

	### ball and paddle collision, based on the pixel size of the paddle and ball
	if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
		#for enhancing speed
		# ball.dx *= -1.5#reverse
		# ball.dy *= 1.5

	if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
		# ball.dx *= -1.5 #reverse
		# ball.dy *= 1.5