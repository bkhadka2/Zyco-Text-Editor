# Canvas is mainly used for drawing graphs and other kinds of drawings
# I have made two boxes in this example where you can draw anything or write any text

import tkinter as tk

class tkinterdemo:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    def label(self):
        mylabel = tk.Label(self.mainWindow, text='tkinter is fun')
        mylabel.pack(side='top')
        self.canvas1()
        self.canvas2()

    def canvas1(self):
        mycanvas = tk.Canvas(self.mainWindow, relief='raised', borderwidth=4, bg='green')
        mycanvas.create_text(100, 10, fill='darkblue', font="Times 20 italic bold", text='\n Canvas number 1')
        mycanvas.pack(side='left')

    def canvas2(self):
        mycanvas2 = tk.Canvas(self.mainWindow, relief='raised', borderwidth=4, bg='red')
        mycanvas2.create_text(100, 10, fill='darkblue', font="Times 20 italic bold", text='\n Canvas number 2')
        mycanvas2.pack(side='right')


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('700x600')
    p = tkinterdemo(root)
    p.label()
    root.mainloop()
