# Import module
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import shutil


filetypes = (
    ('PDF files', '*pdf' ),
    ('All files', '*.*'),
    ('Text files', '*.TXT')
)
  
# Create object
root = tk.Tk()

# Adjust size of windows
root.geometry('500x500')
root.wm_title("South Ransit - Movefile")

# gui.geometry("500x200")


w1 = PhotoImage(file = 'E:\Workspace_Python\image1.png')
root.tk.call('wm', 'iconphoto', root._w, w1)

# img = tk.Image('photo',file="E:\Workspace_Python\image1.png")
# root.tk.call('wm', 'iconphoto', root._w, img)

# Create Label
Label( root , text = "Welcome" ).pack()

# Choose File
filename = tk.filedialog.askopenfilename(
        # Directory file
        initialdir=r" Directory folder/file ",
        title='Select a file...',
        filetypes=filetypes,
    )
source = filename

# Target to save file
# (Get directory of there computer)
destws = r' Directory folder/file '
destjn = r' Directory folder/file '
destbt = r' Directory folder/file '

# Function button choose target
def button1():
    shutil.move(source, destws)
    messagebox.showinfo("...Name of window...","Success")
def button2():
    shutil.move(source, destjn)
    messagebox.showinfo("...Name of window...","Success")
def button3():
    shutil.move(source, destbt)
    messagebox.showinfo("...Name of window...","Success")

# Function to do again
def showaskAgain():
    msg = tk.messagebox.askquestion('Do again', "Do you want to do it again?", icon = 'question')
    if msg == 'yes':
        loopAgain()
        return msg
    else:
        root.destroy()

# Function to Exit
def exit():
    root.destroy()

# Button choose target
but1 = ttk.Button(root, text = "...", command = button1).pack()
but2 = ttk.Button(root, text = "...", command = button2).pack()
but3 = ttk.Button(root, text = "...", command = button3).pack()

# Button 'Do again' and 'Exit'
butAsk = Button(root, text="Again", command = showaskAgain ).pack()
butexit = Button(root, text="Exit", command = exit ).pack()

# 'Loop for do again'
def loopAgain():
    while True:
        global source
        filename = tk.filedialog.askopenfilename(
            initialdir=r" Directory folder/file ",
            title='Select a file...',
            filetypes=filetypes
        )
        source = filename 
        break

root.mainloop()