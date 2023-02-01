from tkinter import *

root = Tk()
root.title('Flip The Switch')
# root.iconbitmap()
root.geometry("500x300")

my_label = Label(root, text="The Switch is On!", fg="green", font=("Helvetica", 32))
my_label.pack(pady=20)

on = PhotoImage(file="images/on.png")
off = PhotoImage(file="images/off.png")

on_button = Button(root, image=on)
on_button.pack(pady=50)

root.mainloop()