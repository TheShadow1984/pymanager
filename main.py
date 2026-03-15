import os
import tkinter as tk
from functools import partial

window = tk.Tk()
window.title("File Manager")
window.geometry("860x460")
window.resizable(False,False)
window.configure(bg="lightgray")

list = tk.Frame(window, bg="white", width="120", height="418")
list.place(x=5, y=37)

topBar = tk.Frame(window, bg="white", width="700", height="30")
topBar.pack(pady=3)

textSpace = tk.Frame(window, bg="white", width="716", height="418")
textSpace.place(x="135", y="37" )

button_y= 1
element_x = 1
element_y = 30

def quit():
    window.destroy()

def home():
    user = os.getlogin()
    os.chdir(f"C:\\Users\\{user}\\Desktop")
    load()

def saveFile():
    global fileDestination
    newContent = fileContent.get(1.0, tk.END)

    with open(fileDestination, "w", encoding="utf-8") as newFile:
        newFile.write(newContent)

def errorHandeling(e):
        errorMessage = f"Error occured while running: {e}"
        errorHandler = tk.Label(textSpace, text=errorMessage, bg="white", fg="black")
        errorHandler.place(x=element_x)

def chDir():
    path = nav.get()
    try:
        os.chdir(path)
        load()
    except Exception as e:
        errorHandeling(e)

def clean():
    global button_y
    button_y = 1

    for widget in list.winfo_children():
        widget.destroy()

    for widget in topBar.winfo_children():
        widget.destroy()

def cleanText():

    for widget in textSpace.winfo_children():
        widget.destroy()

def backBtn():
    os.chdir("../")
    load()

def top():
    global nav
    global saveBtn

    back = tk.Button(topBar, text="🢁", command=backBtn, bg="lightgray", fg="black", width="4")
    exit = tk.Button(topBar, text="➜]", command=quit, bg="lightgray", fg="black", width="4")
    cleanBtn = tk.Button(topBar, text="❌", command=cleanText, bg="lightgray", fg="black")
    homeBtn = tk.Button(topBar, text="🏠", command=home, bg="lightgray", fg="black")
    saveBtn = tk.Button(topBar, text="✓", command=saveFile, bg="lightgray", fg="black")
    
    nav = tk.Entry(topBar, bg="lightgray", fg="black", width="70")

    back.place(x=50, y=1)
    exit.place(x=6, y=1)
    nav.place(anchor="center", relx="0.5", rely="0.5")
    cleanBtn.place(x=670, y=1)
    saveBtn.place(x=640, y=1)
    homeBtn.place(x=95, y=1)

    nav.insert(0, os.getcwd())
    nav.bind("<Return>", chDir)


def load():
    global button_y
    global element_x

    clean()
    top()

    files = []
    dirs = []


    for item in os.listdir():
        if os.path.isdir(item):
            dirs.append(item)
        else:
            files.append(item)
    
    for j in dirs:
        dirsBtn=tk.Button(list, text=f"☰ {j}", command=partial(open_dir, j), bg="lightgray", fg="black")
        dirsBtn.place(x=element_x, y=button_y)
        button_y += 30

    for i in files:
        filesBtn=tk.Button(list, text=i, command=partial(open_file, i), bg="lightgray", fg="black")
        filesBtn.place(x=element_x, y=button_y)
        button_y += 30


def open_file(filepath):
    global element_x
    global fileContent
    global fileDestination

    fileDestination = filepath

    cleanText()
    top()

    try:
        with open(filepath, "r", encoding="utf-8") as readFile:
            text = readFile.read()
            fileContent = tk.Text(textSpace, bg="white", fg="black", width="716", height="418")

            fileContent.place(x=element_x)
            fileContent.insert('1.0', text)
            fileContent.bind(saveBtn)

    except Exception as e:
        errorHandeling(e)


def open_dir(dirpath):

    try:
        os.chdir(dirpath)
        load()
    except Exception as e:
        errorHandeling(e)
        load()
    

if __name__ == "__main__":
    try:
        load()
    except Exception as e:
        print("Error: ",e )

window.mainloop()
