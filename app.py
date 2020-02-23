import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(', ')
        apps = [x for x in tempApps if x.strip()]

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
                                            filetypes=(("executables", "*.exe"), ("PDF", "*.pdf"), ("all files", "*.*")))
    
    apps.append(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()

def runApps():
    for app in apps:
        app = app.rstrip(',')
        app = app.rstrip(' ')
        open_file(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=10, highlightbackground='#263D42', command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=10, highlightbackground='#263D42', command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')