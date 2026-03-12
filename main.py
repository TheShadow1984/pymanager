import os
import tkinter as tk
from functools import partial

window = tk.Tk()
window.title("File Manager")
window.geometry("860x460")
window.configure(bg="black")

button_y=30
element_x = 10
element_y = 30
mode = "folder"

def quit():
    window.destroy()

def clean():
    global button_y
    button_y = 30

    for widget in window.winfo_children():
        widget.destroy()

def backBtn():
    if mode == "folder":
        os.chdir("../")
        load()
    else: 
        clean()
        load()

def top():
    back = tk.Button(window, text="back", command=backBtn, bg="black", fg="#07E300")
    exit = tk.Button(window, text="exit", command=quit, bg="black", fg="#FF0303")
    nav = tk.Label(window, text=os.getcwd(), bg="black", fg="#07E300")
    back.place(x=40, y=1)
    exit.place(x=10, y=1)
    nav.place(x=90, y=2.5)


def load():
    global button_y
    global element_x
    global mode

    clean()
    top()
    mode = "folder"

    files = []
    dirs = []


    for item in os.listdir():
        if os.path.isdir(item):
            dirs.append(item)
        else:
            files.append(item)
    
    for j in dirs:
        dirsBtn=tk.Button(window, text=f"/{j}", command=partial(open_dir, j), bg="black", fg="#00DFE3")
        dirsBtn.place(x=element_x, y=button_y)
        button_y += 30

    for i in files:
        filesBtn=tk.Button(window, text=i, command=partial(open_file, i), bg="black", fg="#07E300")
        filesBtn.place(x=element_x, y=button_y)
        button_y += 30


def open_file(filepath):
    global element_x
    global mode

    clean()
    top()
    mode = "file"

    try:
        with open(filepath, "r", encoding="utf-8") as readFile:
            text = readFile.read()
            fileContent = tk.Label(window, text=text, anchor="w", justify="left", bg="black", fg="#07E300")
            fileContent.place(x=element_x, y=element_y)

    except Exception as e:
        errorMessage = f"Error while reading file: {e}"
        errorHandler = tk.Label(window, text=errorMessage, bg="black", fg="#07E300")
        errorHandler.place(x=element_x, y=element_y)


def open_dir(dirpath):
    global mode

    mode = "folder"
    os.chdir(dirpath)
    load()
    top()



if __name__ == "__main__":
    try:
        load()
    except Exception as e:
        print("Error: ",e )

window.mainloop()