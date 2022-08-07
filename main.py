from tkinter import *
import random

GAME_SIZE = 500
CUBE_SIZE = 25
BLACK = "#000000"
RED = "#FF0000"
GREEN = "#00FF00"


class Snake:
    def __init__(self):
        self.coordinates = []
        # List for coordinates of snake's head

        self.blocks = []
        # List for blocks attached to snake

        self.coordinates.append([0, 0])
        # Starting position of snake

        for x, y in self.coordinates:
            block = canvas.create_rectangle(x, y, x + CUBE_SIZE, y + CUBE_SIZE, fill=GREEN, tag="snake")
            # Block's that act as snake's body

            self.blocks.append(block)

class Cube:
    def __init__(self):
        x = random.randint(0, (GAME_SIZE / CUBE_SIZE) - 1) * CUBE_SIZE
        y = random.randint(0, (GAME_SIZE / CUBE_SIZE) - 1) * CUBE_SIZE
        # Find random x and y coordinates for cube

        self.coordinates = [x, y]
        # Assign these random coordinates to self

        canvas.create_rectangle(x, y, x + CUBE_SIZE, y + CUBE_SIZE, fill=RED, tag="cube")
        # Draw rectangle at these coordinates


window = Tk()
# Create window for game

window.title("SNAKE")
# Name it 'SNAKE'

window.resizable(False, False)
# Don't allow it to be resized

points = 0
# Points represents the number of cubes on snake

label = Label(window, text="Points: {}".format(points), font=('Times', 30))
# Label for the score

label.pack()
# Pack changes

canvas = Canvas(window, bg=BLACK, height=GAME_SIZE, width=GAME_SIZE)
# Canvas for the snake

canvas.pack()
# Pack changes

window.update()
# Update window so it renders

cube = Cube()
# Cube object is created

snake = Snake()
# Snake object is created

window.mainloop()
# Run the main loop for the window
