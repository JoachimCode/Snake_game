from turtle import Screen
from snake import Snake, Turtle
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.listen()
screen.tracer(0)

game = True

snake = Snake()
food = Food()
score = Scoreboard()


screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")


while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.update()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].ycor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280:
        game = False
        score.game_over()
    for segments in snake.segments[1:]:
        if snake.segments[0].distance(segments) < 10:
            game = False
            score.game_over()



screen.exitonclick()