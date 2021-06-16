from tkinter import *

# Main window
root = Tk()
root.title("Jaffa Code | GUI")
root.geometry("500x500")

click = PhotoImage(file='click.png')

button = Button(root, image=click, borderwidth=0, width=100, height=50)
button.pack(pady=20)

root.mainloop()