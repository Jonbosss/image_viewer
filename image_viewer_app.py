import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Image Viewer")
root.iconbitmap(
    "c:/Users/jonat/Documents/Coding Practice/image_viewer/Icon.ico")

my_img = ImageTk.PhotoImage(Image.open("Beginnings.png"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
