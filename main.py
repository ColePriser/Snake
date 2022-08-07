from tkinter import *
import random

GAME_SIZE = 500
CUBE_SIZE = 25


class Cube:
    def __init__(self):
        x = random.randint(0, (GAME_SIZE / CUBE_SIZE) - 1) * CUBE_SIZE
        y = random.randint(0, (GAME_SIZE / CUBE_SIZE) - 1) * CUBE_SIZE
        self.coordinates = [x, y]

        canvas.create_rectangle(x, y, x + CUBE_SIZE, y + CUBE_SIZE, fill="#00FF00", tag="cube")


# Create window for game
# Name it 'SNAKE'
# Don't allow it to be resized
window = Tk()
window.title("SNAKE")
window.resizable(False, False)

# Points represents the number of cubes on snake
points = 0

# Label for the score
label = Label(window, text="Points: {}".format(points), font=('Times', 30))
label.pack()

# Canvas for the snake
canvas = Canvas(window, bg="#000000", height=500, width=500)
canvas.pack()

# Update window so it renders
window.update()

cube = Cube()


# Run the main loop for the window
window.mainloop()
