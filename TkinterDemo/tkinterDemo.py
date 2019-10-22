import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title("Welcome to tkinter demo")
mainWindow.geometry("700x600")
myLabel = tkinter.Label(mainWindow, text="Hello Team")
myLabel.pack()
mainWindow.mainloop()

