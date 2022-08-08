from tkinter import *
import random

GAME_SIZE = 500
CUBE_SIZE = 25
SPEED = 50
START_LENGTH = 3
BLACK = "#000000"
RED = "#FF0000"
GREEN = "#00FF00"


class Snake:
    def __init__(self):
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

    if dir == 'left':
        x -= CUBE_SIZE
    elif dir == 'right':
        x += CUBE_SIZE
    elif dir == 'up':
        y += CUBE_SIZE
    elif dir == 'down':
        y -= CUBE_SIZE

    snake.coordinates.insert(0, (x, y))
    # Add coordinates for block to head of snake

    head = canvas.create_rectangle(x, y, x + CUBE_SIZE, y + CUBE_SIZE, fill=GREEN)
    # Create block to add to snake

    snake.blocks.insert(0, head)
    # Add block to list of current blocks of snake

    if x == cube.coordinates[0]:
        if y == cube.coordinates[1]:
            global points
            points += 1
            label.config(text="Points: {}".format(points))
            # If head of snake eats the cube, then add a point

            canvas.delete("cube")
            cube = Cube()
            # Delete the current cube object and create a new one
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.blocks[-1])
        del snake.blocks[-1]
        # Delete the last block in snake if no cube eaten

    window.after(SPEED, turn, snake, cube)
    # Put change into effect on window


def switch_direction(new_dir):
    global dir

    if new_dir == 'up':
        if dir != 'down':
            dir = new_dir
            # Change direction to down if it isn't already up
    elif new_dir == 'down':
        if dir != 'up':
            dir = new_dir
            # Change direction to up if it isn't already down
    elif new_dir == 'left':
        if dir != 'right':
            dir = new_dir
            # Change direction to left if it isn't already right
    elif new_dir == 'right':
        if dir != 'left':
            dir = new_dir
            # Change direction to right if it isn't already left


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

window.bind('<Left>', lambda event: switch_direction('left'))
window.bind('<a>', lambda event: switch_direction('left'))
window.bind('<Right>', lambda event: switch_direction('right'))
window.bind('<d>', lambda event: switch_direction('right'))
window.bind('<Up>', lambda event: switch_direction('up'))
window.bind('<w>', lambda event: switch_direction('up'))
window.bind('<Down>', lambda event: switch_direction('down'))
window.bind('<s>', lambda event: switch_direction('down'))
# Set key binds for switching direction of snake

snake = Snake()
cube = Cube()
# Snake and Cube objects are created

turn(snake, cube)
# Call turn to begin movement

window.mainloop()
# Run the main loop for the window
