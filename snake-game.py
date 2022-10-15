# Importing libraries
import turtle
import random
import time


# Creating turtle screen
screen = turtle.Screen()
screen.title('DATAFLAIR-SNAKE GAME')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('turquoise')


# Create border
turtle.speed(5) # Speed of the turtle
turtle.pensize(4) # Border color
turtle.penup()  # penup() method is used to pull the pen up – no drawing when moving.
turtle.goto(-310,250) # Move turtle to an absolute position.
turtle.pendown() # pendown() method is used to pull the pen down – drawing when moving.
turtle.color('black')
turtle.forward(600) # Move the turtle forward by the specified distance, in the direction the turtle is headed.
turtle.right(90) # Turn turtle right by angle units.
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle() # Hides the turtle cursor


# Score
score = 0 # Initial score
delay = 0.1 # Snake body parts (list) 


# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0,0) # Initial position of the snake
snake.direction = 'stop' 


# Snake food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30,30)

old_fruit=[]


# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :",align="center",font=("Courier",24,"bold")) # Write text on the turtle window


# Keyboard bindings
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")


# Main loop
while True:
        screen.update() 
        # Snake and fruit coliisions
        if snake.distance(fruit)< 20:
            x = random.randint(-290,270) # Random x coordinate
            y = random.randint(-240,240) # Random position of the fruit
            fruit.goto(x,y) # Move fruit to a random spot
            scoring.clear()
            score+=1
            scoring.write("Score:{}".format(score),align="center",font=("Courier",24,"bold"))
            delay-=0.001
            
            ## Creating new_ball
            new_fruit = turtle.Turtle()
            new_fruit.speed(0)
            new_fruit.shape('square')
            new_fruit.color('red')
            new_fruit.penup()
            old_fruit.append(new_fruit)
                

        # Adding ball to snake    
        for index in range(len(old_fruit)-1,0,-1): # Loop through the list backwards
            a = old_fruit[index-1].xcor() # Get the x coordinate of the previous ball
            b = old_fruit[index-1].ycor() 

            old_fruit[index].goto(a,b) # Move the current ball to the previous ball's position
                                     
        if len(old_fruit)>0: # If there is at least one ball
            a= snake.xcor() # Get the snake's x coordinate
            b = snake.ycor()
            old_fruit[0].goto(a,b)
        snake_move()


        ## Snake and border collision    
        if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240: # If the snake hits the border
            time.sleep(1) # Pause the game for 1 second
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0,0)
            scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


        ## Snake collision
        for food in old_fruit: # Loop through the list of balls
            if food.distance(snake) < 20: 
                time.sleep(1)
                screen.clear()
                screen.bgcolor('turquoise')
                scoring.goto(0,0)
                scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


                
        time.sleep(delay)
        turtle.Terminator()






