#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 400
startx = -100
starty = -100
turtle_scale = 1.5
lastMove = None
lastValidPos = None

#------ robot commands
def moveUp():
  global lastMove, lastValidPos
  lastValidPos = robot.position()
  robot.dot(10)
  robot.seth(90)
  robot.fd(50)
  lastMove = "up"
  checkSquare()

def moveDown():
  global lastMove, lastValidPos
  lastValidPos = robot.position()
  robot.dot(10)
  robot.seth(270)
  robot.fd(50)
  lastMove = "down"
  checkSquare()

def moveLeft():
  global lastMove, lastValidPos
  lastValidPos = robot.position()
  robot.dot(10)
  robot.seth(180)
  robot.fd(50)
  lastMove = "left"
  checkSquare()
  
def moveRight():
  global lastMove, lastValidPos
  lastValidPos = robot.position()
  robot.dot(10)
  robot.seth(0)
  robot.fd(50)
  lastMove = "right"
  checkSquare()

invalid_squares = [(-100,100),(-100,50),(-100,0),(-50,-100),(0,0),(0,-50),(50,0),(50,100),(100,-100),(100,100)]
def checkSquare():
  global lastValidPos
  current_pos = (round(robot.xcor()), round(robot.ycor()))
  if current_pos in invalid_squares or abs(robot.xcor()) > 101 or abs(robot.ycor()) > 101:
    print(f"Collision detected at {current_pos}! Moving back to {lastValidPos}")
    robot.goto(lastValidPos[0], lastValidPos[1])
  elif robot.position() == (0, -100):
    print("Maze completed!")
    robot.hideturtle()
  else:
    lastValidPos = robot.position()
    
#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "assets\\robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("assets\\maze4.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# Use arrow keys to move the robot
wn.onkey(moveUp, "Up")
wn.onkey(moveDown, "Down")
wn.onkey(moveLeft, "Left")
wn.onkey(moveRight, "Right")

#---- end robot movement 

wn.listen()
wn.mainloop()
