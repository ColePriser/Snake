from tkinter import *

window = Tk()
window.title("SNAKE")
window.resizable(False, False)

points = 0

text = Label(window, text="Points: {}".format(points), font=('Times', 30))
text.pack()

window.mainloop()