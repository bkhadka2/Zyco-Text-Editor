import tkinter as tk
from tkinter import ttk
import socket
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Frame
import os
import sys


class ZycoEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x900')
        self.root.title("Zyco@{}".format(socket.gethostbyaddr(socket.gethostname())[0]))
        self.canvas = None
        self.text = tk.Text(self.root, width=400, height=100)

    # def textInsertion(self):
    #     self.text = tk.Text(self.root, width=400, height=100)
    #     self.text.pack()

    def textDisplayed(self):
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
        filename = filedialog.askopenfile()
        text = filename.read()
        dataClearance = messagebox.askyesnocancel(title="Clearing data...", message='''screen will be cleared
                                                                                   'and uploaded''')

        if text and dataClearance:
            self.clearTheScreen()
            self.beginningText.insert('1.0', text)

    def clearTheScreen(self):
        self.beginningText.delete('1.0', 'end')

    def undoEditorFunction(self):
        print("undo done")

    def saveasFile(self):
        print("saved as called")

    def searchword(self):

        # self.beginningText.get(self.root, )
        print("Search command called")

    def exitCommand(self):
        a = messagebox.askyesnocancel(title="Exiting...", message='Are you sure want to exit')
        if a:
            self.root.quit()

    def insertPictures(self):
        print("insert")
        image = tk.PhotoImage(file="~/Desktop/Extras/SkydiveJuly4(2019)/G0269357.JPG")
        self.text.image_create('insert', image=image)

    def capturingMouseEvent(self, event):
        global prev
        prev = event

    def creatingCanvas(self):
        self.root = tk.Tk()
        self.root.title("Draw your STUFF here")
        self.NavigationForDrawCommand()
        self.canvas = tk.Canvas(self.root, width=640, height=480, background='white')
        self.canvas.pack()
        self.canvas.bind('<ButtonPress>', self.capturingMouseEvent)
        self.canvas.bind('<B1-Motion>', self.drawOnTheScreen)

    def drawOnTheScreen(self, event):
        global prev
        self.canvas.create_line(prev.x, prev.y, event.x, event.y, width=5)
        prev = event

    def navigation(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file = tk.Menu(menu)
        file.add_command(label="Upload File", command=self.uploadNewFile, font=20)
        menu.add_cascade(label="File", menu=file, font=30)
        file.add_command(label="Save as..", command=self.saveasFile, font=20)
        file.add_command(label="Draw", command=self.creatingCanvas, font=20)
        file.add_command(label="Insert Pictures", command=self.insertPictures, font=20)

        editmenu = tk.Menu(menu)
        editmenu.add_command(label='Clear Screen', command=self.clearTheScreen, font=20)
        editmenu.add_command(label="Undo", command=self.undoEditorFunction, font=20)
        menu.add_cascade(label="Edit", menu=editmenu, font=30)

        exitmenu = tk.Menu(menu)
        exitmenu.add_command(label='Exit', command=self.exitCommand, font=20)
        menu.add_cascade(label="Exit", menu=exitmenu, font=30)

        searchmenu = tk.Menu(menu)
        searchmenu.add_command(label='Search', command=self.searchword, font=20)
        menu.add_cascade(label="Search", menu=searchmenu, font=30)

        terminal = tk.Menu(menu)
        terminal.add_command(label='Terminal', command=self.integratedTerminal, font=20)
        menu.add_cascade(label="Terminal", menu=terminal, font=30)

    def integratedTerminal(self):
        self.root = tk.Tk()
        hostname = socket.gethostbyaddr(socket.gethostname())[0]
        self.root.title("Terminal@{}".format(hostname))
        terminalUbuntu = Frame(self.root, height=600, width=700)
        terminalUbuntu.pack(fill='both', expand='yes')
        wid = terminalUbuntu.winfo_id()
        if sys.platform == 'linux':
            os.system('xterm -into %d -geometry 400x600 -sb &' % wid)
        else:
            os.system('iTerm -into %d -geometry 400x600 -sb &' % wid)

    def shortcut(self, action):
        print(action)

    def KeyboardEvent(self):
        self.root.bind('<Control-z>', lambda ran: self.shortcut('Undo'))

    def NavigationForDrawCommand(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file, font=30)
        file.add_command(label="Save as..", command=self.saveasFile, font=20)


if __name__ == '__main__':
    editorObj = ZycoEditor()
    editorObj.navigation()
    editorObj.ProgressBar()
    editorObj.textDisplayed()
    # editorObj.textInsertion()
    editorObj.KeyboardEvent()
    editorObj.mainLoopHandling()
