from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TASK LIST PROJECT")

Tasklist = [
    ("Task Number 1", "Eat apple."),
    ("Task Number 2", "Eat banana."),
    ("Task Number 2", "Do the dishes."),
    ("Task Number 3", "Cut the grass."),
    ("Task Number 4", "Take the dog out."),
    ("Task Number 5", "Take the cat out.")
]

tasks = StringVar()
tasks.set("Task Number 1")

for text, mode in Tasklist:
    Radiobutton(root, text=text, variable=tasks, value=mode).pack(anchor=W)

def klikattu(value):
    taskLabel = Label(root, text=value)
    taskLabel.pack()

