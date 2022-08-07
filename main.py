from tkinter import *
import random

GAME_SIZE = 500
CUBE_SIZE = 25
SPEED = 50
START_LENGTH = 2
BLACK = "#000000"
RED = "#FF0000"
GREEN = "#00FF00"


class Snake:
    def __init__(self):
        self.length = START_LENGTH
        self.coordinates = []
        # List for coordinates of snake's head

        self.blocks = []
        # List for blocks attached to snake

        for i in range(0, START_LENGTH):
            self.coordinates.append([0, 0])
            # Starting position of snake

        for x, y in self.coordinates:
            head = canvas.create_rectangle(x, y, x + CUBE_SIZE, y + CUBE_SIZE, fill=GREEN, tag="snake")
            # Block's that act as snake's body

            self.blocks.append(head)


class Cube:
    def __init__(self):
        x = random.randint(0, (GAME_SIZE / CUBE_SIZE) - 1) * CUBE_SIZE
        y = random.randint(0, (GAME_SIZE / CUBE_SIZE) - 1) * CUBE_SIZE
        # Find random x and y coordinates for cube

        self.coordinates = [x, y]
        # Assign these random coordinates to self

        canvas.create_rectangle(x, y, x + CUBE_SIZE, y + CUBE_SIZE, fill=RED, tag="cube")
        # Draw rectangle at these coordinates


def turn(snake, cube):
    x, y = snake.coordinates[0]
    if dir == "left":
        x -= CUBE_SIZE
    elif dir == "right":
        x += CUBE_SIZE
    elif dir == "up":
        y += CUBE_SIZE
    elif dir == "down":
        y -= CUBE_SIZE

    # Add coordinates for block to head of snake
    snake.coordinates.insert(0, (x, y))

    # Create block to add to snake
    head = canvas.create_rectangle(x, y, x + CUBE_SIZE, y + CUBE_SIZE, fill=RED)

    # Add block to list of current blocks of snake
    snake.blocks.insert(0, head)

    # Delete the last block in snake
    del snake.coordinates[-1]
    canvas.delete(snake.blocks[-1])
    del snake.blocks[-1]

    # Put change into effect on window
    window.after(SPEED, turn, snake, cube)


window = Tk()
# Create window for game

window.title("SNAKE")
# Name it 'SNAKE'

window.resizable(False, False)
# Don't allow it to be resized

points = 0
dir = 'down'
# Points represents the number of cubes on snake

label = Label(window, text="Points: {}".format(points), font=('Times', 30))
label.pack()
# Label for the score

canvas = Canvas(window, bg=BLACK, height=GAME_SIZE, width=GAME_SIZE)
canvas.pack()
# Canvas for the snake

window.update()
# Update window so it renders

snake = Snake()
cube = Cube()
# Snake and Cube objects are created

turn(snake, cube)

window.mainloop()
# Run the main loop for the window
