from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 600)     # Setup the screen height and width
screen.bgcolor("black")                     # Background color
screen.title("Snake game")                  # popup screen title

starting_position = [(0,0), (-20,0), (-40,0)]

# Create a 20px heigt and 60px width snake 
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)              # Createing each segment with it's axis value (starting_position)

screen.exitonclick()