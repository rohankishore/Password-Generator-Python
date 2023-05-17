import tkinter.messagebox
from tkinter import *
import random, string
import pyperclip

root = Tk()
root.resizable(0,0)
root.title("Password Generator")

Label(root, text="PASSWORD GENERATOR", font='arial 15 bold').pack()
Label(root, text="Codify Python", font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(root , text="PASSWORD LENGTH", font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_=8, to=32, textvariable=pass_len, width=15).pack()

pass_str = StringVar()

def Generator():
    password = ""

    for x in range(0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)

    for y in range(pass_len.get() - 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        pass_str.set(password)

Button(root , text="GENERATE PASSWORD", command=Generator).pack(pady=5)

Entry(root, textvariable=pass_str).pack()

def copyPassword():
    pyperclip.copy(pass_str.get())
    tkinter.messagebox.Message("Copied!")

Button(root , text="COPY TO CLIPBOARD", command=copyPassword).pack(pady=5)

root.mainloop()
