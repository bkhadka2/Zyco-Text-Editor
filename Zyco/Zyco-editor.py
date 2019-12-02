import tkinter as tk
from tkinter import ttk
import socket
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Frame
import os
import sys
from tkinter.scrolledtext import ScrolledText
from tkinter import simpledialog

fontFlag = False

class ZycoEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x900')
        self.root.title("Zyco@{}".format(socket.gethostbyaddr(socket.gethostname())[0]))
        self.canvas = None
        self.text = tk.Text(self.root, width=400, height=100, undo=True, autoseparators=True, maxundo=-1)
        self.text.config(wrap='word')
        self.wordsList = []
        self.spaces = 4
        self.image = None
        self.restoringImage = []
        self.fileName = None
        self.filePathStatus = None

    def textDisplayed(self):
        self.text = tk.Text(self.root, width=400, height=100, font=40, undo=True, autoseparators=True, maxundo=-1)
        self.text.insert('1.0 ', 'Welcome to Zyco')
        self.text.insert('1.0 lineend', "\nCreated by Bishal Khadka, Rupesh Panta, and Jose Cervantes")
        self.text.pack()

    def ProgressBar(self):
        myProgressBar = ttk.Progressbar(self.root, orient="horizontal", length=200)
        myProgressBar.pack()
        myProgressBar.config(mode='determinate', maximum=11.0, value=4.2)
        value = tk.DoubleVar()
        myProgressBar.config(variable=value)
        scale = ttk.Scale(self.root, orient='horizontal', length=200, variable=value, from_=0.0, to=11.0)
        scale.pack()

    def scrollBar(self):
        self.textBox = ScrolledText(self.root, borderwidth=3, relief='sunken')

    def mainLoopHandling(self):
        self.root = tk.mainloop()

    def uploadNewFile(self):
        self.filePathStatus = False
        filename = filedialog.askopenfile(title="Select Zyco file")
        textInEditor = filename.read()
        dataClearance = messagebox.askyesnocancel(title="Clearing data...", message='''screen will be cleared
                                                                                   'and uploaded''')

        if textInEditor and dataClearance:
            self.clearTheScreen()
            self.text.insert('1.0', textInEditor)

    def clearTheScreen(self):
        self.text.delete('1.0', 'end')

    def saveasFile(self):
        print("saved as called")
        self.filePathStatus = True
        fileContent = self.text.get('1.0', 'end')
        print(fileContent)
        file = filedialog.asksaveasfile(title='Save as')
        self.fileName = file.name
        print(self.fileName)
        if self.fileName:
            with open(self.fileName, 'w') as W:
                W.write(fileContent)

            W.close()
        else:
            print("Could not find a file to Save")

    def save(self):
        print("Save called")
        fileContent = self.text.get('1.0', 'end')
        if self.fileName and self.filePathStatus:
            with open(self.fileName, 'w') as W:
                W.write(fileContent)
            W.close()
        else:
            self.saveasFile()

    def searchword(self):
        print("Search command called")
        self.text.tag_config("red_tag", foreground="red")
        AllList = self.text.get('1.0', 'end')
        response = simpledialog.askstring("Search For Word", " Enter the name to search")
        if response.lower() in AllList.lower():
            messagebox.showinfo("Found", "Word Found")
            offset = '+%dc' % len(response)
            pos_start = self.text.search(response, '1.0', 'end')
            while pos_start:
                pos_end = pos_start + offset
                self.text.tag_add('red_tag', pos_start, pos_end)
                pos_start = self.text.search(response, pos_end, 'end')

        else:
            messagebox.showinfo("Not Found", "Sorry, word not found")

    # def highlightPython(self):
    #     print("Search command called")
    #     self.text.tag_config("red_tag", foreground="red")
    #     AllList = self.text.get('1.0', 'end')
    #     response = simpledialog.askstring("Search For Word", " Enter the name to search")
    #     if response.lower() in AllList.lower():
    #         messagebox.showinfo("Found", "Word Found")
    #         offset = '+%dc' % len(response)
    #         pos_start = self.text.search(response, '1.0', 'end')
    #         while pos_start:
    #             pos_end = pos_start + offset
    #             self.text.tag_add('red_tag', pos_start, pos_end)
    #             pos_start = self.text.search(response, pos_end, 'end')
    #
    #     else:
    #         messagebox.showinfo("Not Found", "Sorry, word not found")

    def exitCommand(self):
        a = messagebox.askyesnocancel(title="Exiting...", message='Are you sure want to exit')
        if a:
            self.root.quit()

    def insertPictures(self):
        print("insert")
        filename = filedialog.askopenfile()
        print(filename.name)
        messagebox.showinfo("File Path Name Info", "File path name is printed on console, copy and paste in box")
        response = simpledialog.askstring("File Path Entry", prompt='Enter file path')
        self.image = tk.PhotoImage(file=response)
        self.restoringImage.append(self.image)
        if self.image in self.restoringImage:
            self.text.image_create('insert', image=self.image)
        print("Displayed")

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

    def deleteCanvasImage(self):
        self.canvas.delete('all')

    def drawOnTheScreen(self, event):
        global prev
        self.canvas.create_line(prev.x, prev.y, event.x, event.y, width=5)
        prev = event

    def navigation(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file = tk.Menu(menu)
        file.add_command(label="Upload File(Ctrl-O)", command=self.uploadNewFile, font=20)
        menu.add_cascade(label="File", menu=file, font=30)
        file.add_command(label="Save(Ctrl-S)", command=self.saveasFile, font=20)
        file.add_command(label="Save as..(Ctrl-S)", command=self.saveasFile, font=20)
        file.add_command(label="Draw", command=self.creatingCanvas, font=20)
        file.add_command(label="Insert Pictures", command=self.insertPictures, font=20)

        editmenu = tk.Menu(menu)
        editmenu.add_command(label='Clear Screen', command=self.clearTheScreen, font=20)
        editmenu.add_command(label='Select All(Ctrl-A)', command=self.selectAll, font=20)
        editmenu.add_command(label="Unselect All(Ctrl-Q)", command=self.unSelectAll, font=20)
        editmenu.add_command(label="Highlight/unHighlight", command=self.highlightWord, font=20)
        editmenu.add_command(label="Delete Highlighted", command=self.justDeleteTheHiglightedWord, font=20)
        menu.add_cascade(label="Edit", menu=editmenu, font=30)

        exitmenu = tk.Menu(menu)
        exitmenu.add_command(label='Exit', command=self.exitCommand, font=20)
        menu.add_cascade(label="Exit", menu=exitmenu, font=30)

        searchmenu = tk.Menu(menu)
        searchmenu.add_command(label='Search(Ctrl-F)', command=self.searchword, font=20)
        searchmenu.add_command(label='Unhighlight Searched word(Ctrl-P)', command=self.unhighlightSearchedWord)
        menu.add_cascade(label="Search", menu=searchmenu, font=30)

        fontMenu = tk.Menu(menu)
        fontMenu.add_command(label='Courier font', command=self.changingFontCourier, font=20)
        fontMenu.add_command(label='Halvetica font', command=self.changingFontHelvetica, font=20)
        fontMenu.add_command(label='Times font', command=self.changingFontTimes, font=20)
        fontMenu.add_command(label='Default font', command=self.defaultFont, font=20)
        menu.add_cascade(label="Change-Font", menu=fontMenu, font=30)

        textWeight = tk.Menu(menu)
        textWeight.add_command(label='Bold', command=self.makingBold, font=20)
        textWeight.add_command(label='Remove bold', command=self.removeBold, font=20)
        textWeight.add_command(label='Underline', command=self.underline, font=20)
        textWeight.add_command(label='Remove Underline', command=self.removeUnderline, font=20)
        menu.add_cascade(label="Change-Text-Weight", menu=textWeight, font=30)

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

    def changingFontCourier(self):
        print('Courier called')
        tags = self.text.tag_names()
        if 'selectAllTag' in tags:
            self.text.tag_add('fontChangeCourier', '1.0', 'end')
            self.text.tag_config('fontChangeCourier', font="Courier")
        # if 'highlight' in tags:
        else:
            self.text.tag_add('fontChangeCourier', 'insert', 'insert wordend')
            self.text.tag_config('fontChangeCourier', font="Courier")

    def changingFontHelvetica(self):
        print('Halvetica')
        tags = self.text.tag_names()
        if 'selectAllTag' in tags:
            self.text.tag_add('fontChangeHelvetica', '1.0', 'end')
            self.text.tag_config('fontChangeHelvetica', font="Helvetica")
        else:
            self.text.tag_add('fontChangeHelvetica', 'insert', 'insert wordend')
            self.text.tag_config('fontChangeHelvetica', font="Helvetica")

    def changingFontTimes(self):
        print('Times called')
        tags = self.text.tag_names()
        if 'selectAllTag' in tags:
            self.text.tag_add('fontChangeTimes', '1.0', 'end')
            self.text.tag_config('fontChangeTimes', font="Times")
        # if 'highlight' in tags:
        else:
            self.text.tag_add('fontChangeTimes', 'insert', 'insert wordend')
            self.text.tag_config('fontChangeTimes', font="Times")

    def defaultFont(self):
        print('Symbol font called')
        tags = self.text.tag_names()
        if 'selectAllTag' in tags:
            self.text.tag_add('fontChangeSymbol', '1.0', 'end')
            self.text.tag_config('fontChangeSymbol', font="Symbol")
        # if 'highlight' in tags:
        else:
            self.text.tag_add('fontChangeSymbol', 'insert', 'insert wordend')
            self.text.tag_config('fontChangeSymbol', font="Symbol")

    def makingBold(self):
        print("Bold called")
        tags = self.text.tag_names()
        if 'selectAllTag' in tags:
            self.text.tag_add('tagbold', '1.0', 'end')
            self.text.tag_config('tagbold', font='Symbol 15 bold')
        # if 'highlight' in tags:
        else:
            self.text.tag_add('tagbold', 'insert', 'insert wordend')
            self.text.tag_config('tagbold', font='Symbol 15 bold')

    def removeBold(self):
        tags = self.text.tag_names()
        print(tags)
        if 'selectAllTag' in tags:
            self.text.tag_remove('tagbold', '1.0', 'end')
        else:
            self.text.tag_remove('tagbold', 'insert', 'insert wordend')

    def underline(self):
        tags = self.text.tag_names()
        if 'selectAllTag' in tags:
            self.text.tag_add('underline', '1.0', 'end')
            self.text.tag_config('underline', underline=True)
        # if 'highlight' in tags:
        else:
            self.text.tag_add('underline', 'insert', 'insert wordend')
            self.text.tag_config('underline', underline=True)

    def removeUnderline(self):
        tags = self.text.tag_names()
        print(tags)
        if 'selectAllTag' in tags:
            self.text.tag_remove('underline', '1.0', 'end')
        else:
            self.text.tag_remove('underline', 'insert', 'insert wordend')

    def defaultFontForALL(self):
        print('Symbol font called')
        tags = self.text.tag_names()
        if 'selectAllTag' in tags:
            self.text.tag_add('fontChangeSymbol', '1.0', 'end')
            self.text.tag_config('fontChangeSymbol', font="Symbol")

    def selectAll(self):  # Selects and deletes if necessary
        print("Select All")
        print(self.text.tag_names())
        self.text.tag_add('selectAllTag', '1.0', 'end')
        self.text.tag_config('selectAllTag',  background='yellow')
        self.text.bind('<BackSpace>', lambda ran: self.justDeleteTheHiglightedWord())
        print(self.text.tag_names())

    def backspaceBinding(self):
        print("Backspace binding called")
        tagsList = self.text.tag_names()
        print(tagsList)
        if 'selectAllTag' in tagsList:
            print("delete for all")
            # self.clearTheScreen()
            self.text.bind('<BackSpace>', lambda ran: self.justDeleteTheHiglightedWord())
            print("successful")
            # self.clearTheScreen()
        elif 'highlight' in tagsList:
            print("delete for selected")
            # self.justDeleteTheHiglightedWord()
            self.text.bind('<BackSpace>', lambda ran: self.justDeleteTheHiglightedWord())
        else:
            print("default delete")
            # self.defaultDelete()
            self.text.bind('<BackSpace>', lambda ran: self.defaultDelete())
            # pass

    def defaultDelete(self):  # gaining default delete of tkinter
        print("default delete")
        self.text.delete('insert', 'insert')

    def unSelectAll(self):
        print("Unselect all")
        self.text.tag_delete('selectAllTag')

    def highlightWord(self):
        print("highlightword called")
        print(self.text.tag_names())
        self.text.tag_config("highlight", background="yellow")
        tags = self.text.tag_names("insert wordstart")
        if "highlight" in tags:
            self.text.tag_remove("highlight", "insert wordstart", "insert wordend")
        # elif 'fontChange' in tags and fontFlag == True:
        #     self.text.tag_remove('fontChange', 'insert wordstart', 'insert wordend')
        else:
            self.text.tag_add("highlight", "insert wordstart", "insert wordend")
        print(self.text.tag_names())

    def justDeleteTheHiglightedWord(self):
        print("deleted highlight")
        tags = self.text.tag_names("insert wordstart")
        if 'selectAllTag' in tags:
            self.text.delete('1.0', 'end')
        elif 'highlight' in tags:
            self.text.delete('insert wordstart', 'insert wordend')
        else:
            self.defaultDelete()

    def tab(self):
        print("tab pressed")
        self.text.insert('insert', " " * self.spaces)
        return 'break'

    def forFontTag(self):
        self.text.tag_delete('fontChange')

    def unhighlight(self):
        print("unhighlight called")
        tags = self.text.tag_names('insert wordstart')
        print(tags)
        if 'selectAllTag' in tags:
            self.text.tag_remove('selectAllTag', '1.0', 'end')
        # elif 'highlight' in tags:
        else:
            self.text.tag_remove('highlight', 'insert wordstart', 'insert wordend')
        self.unSelectAll()
        # if 'fontChange' in tags:
        # else:
            # self.text.tag_delete('fontChange')

        print(tags)

        # if 'highlight' in tags and fontFlag == True:
        #     self.text.
        # else:
        #     self.text.tag_remove('red_tag', '1.0', 'end')

    def unhighlightSearchedWord(self):
        self.text.tag_remove('red_tag', '1.0', 'end')

    def KeyboardEvent(self):
        self.text.bind('<Control-a>', lambda ran: self.selectAll())
        self.text.bind('<Control-q>', lambda ran: self.unSelectAll())
        self.text.bind('<Control-s>', lambda ran: self.save())
        self.text.bind('<Double-Button-1>', lambda ran: self.highlightWord())
        self.text.bind('<Tab>', lambda ran: self.tab())
        self.text.bind('<BackSpace>', lambda ran: self.backspaceBinding())
        self.text.bind('<Button-1>', lambda ran: self.unhighlight())
        self.text.bind('<Control-f>', lambda ran: self.searchword())
        self.text.bind('<Control-p>', lambda ran: self.unhighlightSearchedWord())
        self.text.bind('<Control-o>', lambda ran: self.uploadNewFile())
        self.text.bind('<Control-b>', lambda ran: self.makingBold())
        self.text.bind('<Control-u>', lambda ran: self.underline())

    def NavigationForDrawCommand(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file, font=30)
        file.add_command(label="Save as..", command=self.saveasFile, font=20)

        clear = tk.Menu(menu)
        menu.add_cascade(label="Clear", menu=clear, font=30)
        clear.add_command(label="clear", command=self.deleteCanvasImage, font=20)


if __name__ == '__main__':
    editorObj = ZycoEditor()
    editorObj.navigation()
    editorObj.ProgressBar()
    editorObj.textDisplayed()
    editorObj.scrollBar()
    editorObj.KeyboardEvent()
    editorObj.mainLoopHandling()
