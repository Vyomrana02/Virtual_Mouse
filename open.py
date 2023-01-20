import sys
import os
import tkinter as tk
from tkinter import *

window=Tk()

window.title("Running Python Script")
window.geometry('250x250')
def callback():
    with open("AiVirtualMouseProject.py", "r", encoding="utf-8") as file:
        exec(file.read())
b = tk.Button(window,text="Run the Face Detection",command=callback)
b.pack()

window.mainloop()
