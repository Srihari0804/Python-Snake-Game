import turtle
from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
import time
from food import Food

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #detecting the collision
    if snake.segments[0].xcor()>295 or snake.segments[0].xcor()< -295 or snake.segments[0].ycor() >295 or snake.segments[0].ycor() < -295:
        game_is_on=False
        score.game_over()
        continue

    for segments in snake.segments[1:]:
        if snake.segments[0].distance(segments)<10:
            game_is_on = False
            score.game_over()
            continue

    if snake.segments[0].distance(food)<15:
        score.change_score()
        food.refresh()
        snake.extend()
score.reset_high_score()

turtle.mainloop()
