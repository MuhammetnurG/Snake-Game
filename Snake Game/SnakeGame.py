from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
speed=0.1

snake=Snake(5)
food=Food()
scoreboard=Score()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    # -----------game over when crashes the border-----------------
    # if snake.segments[0].xcor() < -screen.window_width()/2 or snake.segments[0].xcor() > screen.window_width()/2:
    #     time.sleep(1)
    #     game_on=False
    #     scoreboard.rewrite_record()
    #     exit()
    #
    # elif snake.segments[0].ycor() == -screen.window_height()/2 or snake.segments[0].ycor() == screen.window_height()/2:
    #     time.sleep(1)
    #     game_on=False
    #     scoreboard.rewrite_record()
    #     exit()
# ---------------------------------------------------

# --------------continue from orther side when crashed the border--------------
    if snake.segments[0].xcor() > 290:
        snake.segments[0].setx(-290)
    elif snake.segments[0].xcor() < -290:
        snake.segments[0].setx(290)
    elif snake.segments[0].ycor() > 290:
        snake.segments[0].sety(-290)
    elif snake.segments[0].ycor() < -290:
        snake.segments[0].sety(290)
# ------------------------------------------------------------------

    elif snake.segments[0].distance(food)<15:
        food.go_somewhere()
        speed -= 0.005
        snake.add_body()
        scoreboard.update_score()


    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg)<10:
            game_on=False
            scoreboard.rewrite_record()
            time.sleep(1)
            exit()





screen.exitonclick()