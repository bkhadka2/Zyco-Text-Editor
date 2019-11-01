import tkinter as tk
from tkinter import ttk
import socket

class ZycoEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x900')
        self.root.title("Zyco@{}".format(socket.gethostbyaddr(socket.gethostname())[0]))

    def textInsertion(self):
        text = tk.Text(self.root, width=400, height=100)
        text.pack()

    def textDisplayedAtTheBeginning(self):
        beginningText = tk.Text(self.root, width=400, height=100, font=40)
        beginningText.insert('1.0 ', 'Welcome to Zyco')
        beginningText.insert('1.0 lineend', "\nCreated by Bishal Khadka")
        beginningText.pack()

    def ProgressBar(self):
        myProgressBar = ttk.Progressbar(self.root, orient="horizontal", length=200)
        myProgressBar.pack()
        myProgressBar.config(mode='determinate', maximum=11.0, value=4.2)
        value = tk.DoubleVar()
        myProgressBar.config(variable=value)
        scale = ttk.Scale(self.root, orient='horizontal', length=400, variable=value, from_=0.0, to=11.0)
        scale.pack()

    def mainLoopHandling(self):
        self.root = tk.mainloop()

    def uploadNewFile(self):
        print("uploaded new file")

    def undoEditorFunction(self):
        print("undo done")

    def navigation(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        filemenu = tk.Menu(menu)
        filemenu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Upload File", command=self.uploadNewFile)
        filemenu.add_command(label="Exit", command=self.root.quit())
        filemenu.add_separator()

        undomenu = tk.Menu(menu)
        undomenu.add_cascade(label="Undo", menu=undomenu)
        undomenu.add_command(label="undo")


if __name__ == '__main__':
    editorObj = ZycoEditor()
    editorObj.navigation()
    editorObj.ProgressBar()
    editorObj.textDisplayedAtTheBeginning()
    editorObj.textInsertion()
    editorObj.mainLoopHandling()
