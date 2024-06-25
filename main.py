from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)     # Setup the screen height and width
screen.bgcolor("black")                     # Background color
screen.title("Snake game")                  # popup screen title

starting_position = [(0,0), (-20,0), (-40,0)]
segment = []

# Create a 20px heigt and 60px width snake 
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)              # Createing each segment with it's axis value (starting_position)
    segment.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)                          # Slow down 1 second
    for seg_num in range (len(segment)-1, 0, -1):
        new_x = segment[seg_num - 1].xcor()               
        new_y = segment[seg_num - 1].ycor() 
        segment[seg_num].goto(new_x, new_y)         # Give axis values each time it moves it follows the first square                

    segment[0].forward(20) 
      
screen.exitonclick()