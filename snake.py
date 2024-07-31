from turtle import Turtle

STRATING_POSITION = [(0,0), (-20,0), (-40,0)]       # Create a constant (block capital)
MOVE_DISTANCE = 20 
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 

class Snake:
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]                 # To get the snake direction on key press
    
    def create_snake(self):
        # Create a 20px heigt and 60px width snake 
        for position in STRATING_POSITION:
            self.add_segment(position)              # position - inbuild function in turtle to find the position
           
    
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)                  # Createing each segment with it's axis value (starting_position)
        self.segment.append(new_segment)
    
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0] 

    def extend(self):                               # extend the snake 
        tim = Turtle()
        tim._tracer(False)                          # Remove the animation of the new adding part                               
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range (len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()               
            new_y = self.segment[seg_num - 1].ycor() 
            self.segment[seg_num].goto(new_x, new_y)         # Give axis values each time it moves it follows the first square
        self.head.forward(MOVE_DISTANCE) 

    # To get the snake direction on key press    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)                  # snake can't go up when it going down
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
