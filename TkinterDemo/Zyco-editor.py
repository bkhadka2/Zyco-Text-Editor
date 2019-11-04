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
        self.beginningText = tk.Text(self.root, width=400, height=100, font=40)
        self.beginningText.insert('1.0 ', 'Welcome to Zyco')
        self.beginningText.insert('1.0 lineend', "\nCreated by Bishal Khadka")
        self.beginningText.pack()

    def ProgressBar(self):
        myProgressBar = ttk.Progressbar(self.root, orient="horizontal", length=200)
        myProgressBar.pack()
        myProgressBar.config(mode='determinate', maximum=11.0, value=4.2)
        value = tk.DoubleVar()
        myProgressBar.config(variable=value)
        scale = ttk.Scale(self.root, orient='horizontal', length=200, variable=value, from_=0.0, to=11.0)
        scale.pack()

    def mainLoopHandling(self):
        self.root = tk.mainloop()

    def uploadNewFile(self):
        print("uploaded new file")

    def clearTheScreen(self):
        self.beginningText.delete('1.0', 'end')

    def undoEditorFunction(self):
        print("undo done")

    def navigation(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        file = tk.Menu(menu)
        file.add_command(label="Upload File", command=self.uploadNewFile)
        file.add_command(label="")
        menu.add_cascade(label="File", menu=file)

        editmenu = tk.Menu(menu)
        editmenu.add_command(label='Clear Screen', command=self.clearTheScreen)
        editmenu.add_command(label="Undo", command=self.undoEditorFunction)
        menu.add_cascade(label="Edit", menu=editmenu)

        exitmenu = tk.Menu(menu)
        exitmenu.add_command(label='Exit', command=self.root.quit)
        menu.add_cascade(label="Exit", menu=exitmenu)


if __name__ == '__main__':
    editorObj = ZycoEditor()
    editorObj.navigation()
    editorObj.ProgressBar()
    editorObj.textDisplayedAtTheBeginning()
    editorObj.textInsertion()
    editorObj.mainLoopHandling()
