import tkinter as tk

root = tk.Tk()
print(tk.TkVersion)
print(tk.TclVersion)

def displayName():
    functionRoot = tk.Tk()
    functionRoot.geometry('700x500')
    newLabel = tk.Label(functionRoot, text="You are hacked", fg="Green")
    newLabel.pack()


root.geometry('700x500')
myLabel = tk.Label(root, text="Hello", fg="red")
myLabel.pack()
myBotton = tk.Button(root, text="PlayMultiplayer? Click here", command=displayName)
myBotton.pack()
root.mainloop()
