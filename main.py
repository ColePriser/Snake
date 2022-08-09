from tkinter import *
import random

GAME_SIZE = 500
CUBE_SIZE = 25
SPEED = 50
BLACK = "#000000"
RED = "#FF0000"
GREEN = "#00FF00"


class Snake:
    def __init__(self):
        self.coordinates = []
        # List for coordinates of snake's head

        self.blocks = []
        # List for blocks attached to snake

        for i in range(0, 3):
            self.coordinates.append([0, 0])
            # Starting position of snake

        for x, y in self.coordinates:
            head = canvas.create_rectangle(x, y, x + CUBE_SIZE, y + CUBE_SIZE, fill=GREEN)
            # Block's that act as snake's body

            self.blocks.append(head)


class Cube:
    def __init__(self):
        x = random.randint(0, GAME_SIZE - CUBE_SIZE)
        y = random.randint(0, GAME_SIZE - CUBE_SIZE)
        # Find random x and y coordinates for cube

        self.coordinates = [x, y]
        # Assign these random coordinates to self

        canvas.create_rectangle(x, y, x + CUBE_SIZE, y + CUBE_SIZE, fill=RED)
        # Draw rectangle at these coordinates


def turn(snake, cube):
    x, y = snake.coordinates[0]
    # Coordinates for head of snake

    if cur_direction == 'left':
        x -= CUBE_SIZE
    elif cur_direction == 'right':
        x += CUBE_SIZE
    elif cur_direction == 'up':
        y -= CUBE_SIZE
    elif cur_direction == 'down':
        y += CUBE_SIZE

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

    if hit_wall(snake):
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                           font=('Times', 50), text="Game Over!", fill="red")
        # End game
    elif hit_body(snake):
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                           font=('Times', 50), text="Game Over!", fill="red")
        # End game
    else:
        window.after(SPEED, turn, snake, cube)
        # Put change into effect on window


def switch_direction(new_direction):
    global cur_direction

    if new_direction == 'up':
        if cur_direction != 'down':
            cur_direction = new_direction
            # Change direction to down if it isn't already up
    elif new_direction == 'down':
        if cur_direction != 'up':
            cur_direction = new_direction
            # Change direction to up if it isn't already down
    elif new_direction == 'left':
        if cur_direction != 'right':
            cur_direction = new_direction
            # Change direction to left if it isn't already right
    elif new_direction == 'right':
        if cur_direction != 'left':
            cur_direction = new_direction
            # Change direction to right if it isn't already left


def hit_wall(snake):
    x, y = snake.coordinates[0]
    # Coordinates for head of snake
    if x < 0 or x > GAME_SIZE - 1:
        return True
        # Head of snake has gone out of bounds in x direction
    elif y < 0 or y > GAME_SIZE - 1:
        return True
        # Head of snake has gone out of bounds in y direction
    else:
        return False
        # Head of snake has NOT gone out of bounds


def hit_body(snake):
    x, y = snake.coordinates[0]
    # Coordinates for head of snake

    for block in snake.coordinates[1:]:
        if x == block[0]:
            if y == block[1]:
                return True
                # If block hits head, then snake has hit itself

    return False
    # Otherwise, snake has NOT hit itself


window = Tk()
# Create window for game

window.title("SNAKE")
# Name it 'SNAKE'

window.resizable(False, False)
# Don't allow it to be resized

points = 0
cur_direction = "down"
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