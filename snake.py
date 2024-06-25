from turtle import Turtle

STRATING_POSITION = [(0,0), (-20,0), (-40,0)]       # Create a constant (block capital)
MOVE_DISTANCE = 20  

class Snake:
    
    def __init__(self):
        self.segment = []
        self.create_snake()
    
    def create_snake(self):
        # Create a 20px heigt and 60px width snake 
        for position in STRATING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)              # Createing each segment with it's axis value (starting_position)
            self.segment.append(new_segment)

    def move(self):
        for seg_num in range (len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()               
            new_y = self.segment[seg_num - 1].ycor() 
            self.segment[seg_num].goto(new_x, new_y)         # Give axis values each time it moves it follows the first square
        self.segment[0].forward(MOVE_DISTANCE) 
