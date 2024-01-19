# simple snake game in python 3.12

import random
import time

def SnakeGame():
    width = 60
    height = 20

    # snake and food
    snake = [(4, 10), (4, 9), (4, 8)]
    food = (10, 20)

    # game logic
    score = 0

    ESC = 27
    key = "RIGHT"

    while key != ESC:
        print("Score:", score)

        prev_key = key
        event = input()
        key = event if event != "" else prev_key

        if key not in ["LEFT", "RIGHT", "UP", "DOWN", ESC]:
            key = prev_key

        # calculate the next coordinates for snake
        y = snake[0][0]
        x = snake[0][1]

        if key == "DOWN":
            y += 1
        if key == "UP":
            y -= 1
        if key == "LEFT":
            x -= 1
        if key == "RIGHT":
            x += 1

        snake.insert(0, (y, x))

        # check if we hit the border
        if y == 0: break
        if y == height-1: break
        if x == 0: break
        if x == width-1: break

        # if snake runs over itself
        if snake[0] in snake[1:]: break

        if snake[0] == food:
            # eat the food
            score += 1
            food = ()
            while food == ():
                food = (random.randint(1, height-2), random.randint(1, width-2))
                if food in snake:
                    food = ()
        else:
            # move snake
            last = snake.pop()
            print(" ", end="")
            print("\033[F", end="")  # move cursor up

        print("#", end="")
        print("\033[F", end="")  # move cursor up

    print(f"Final score = {score}")
SnakeGame()