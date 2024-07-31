from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)     # Setup the screen height and width
screen.bgcolor("black")                     # Background color
screen.title("Snake game")                  # popup screen title

segment = []

snake = Snake()                             # Create a snake object
food = Food()                               # Create a food object
scoreboard = Scoreboard()                   # Create scoreboard object

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()                          # Update screen in every move(show snake as a )
    time.sleep(0.1)                          # Slow down 1 second                
    snake.move()                             # Move method in Snake class

    # Detect collution with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # Detect collution with wall (xcor - x cordinent, ycor - y cordinent)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    
    # Detect collution with tail
    for segments in snake.segment:
        if segments == snake.head:
            pass

        elif snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()
 
screen.exitonclick()