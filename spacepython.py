import tkinter

mainWindow=tkinter.Tk()
mainWindow.title("SPACE PYTHON")
mainWindow.geometry("800x800")
mainWindow.minsize(width=800, height=800)
mainWindow.maxsize(width=800, height=800)

mainWindow.columnconfigure(0, weight=5)
mainWindow.columnconfigure(1, weight=5)
mainWindow.columnconfigure(2, weight=5)
mainWindow.rowconfigure(0, weight=5)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)

scoreFrame = tkinter.Frame(mainWindow)
shootyFrame = tkinter.Frame(mainWindow)
shipFrame = tkinter.Frame(mainWindow)

scoreFrame.pack(side='top')
shootyFrame.pack(side='top')
shipFrame.pack(side='bottom')
enemy = tkinter.Canvas(shootyFrame, width=800, height=600)
ally = tkinter.Canvas(shipFrame, width=800, height=100)
enemy.pack()
ally.pack()

xa = 0
ya = 100
xb = 50
yb = 0
xc = 100
yc = 100
ship = ally.create_polygon(xa, ya, xb, yb, xc, yc, fill='red', width=4)
ship.pack()

mainWindow.mainloop()


x = False
while x == False:
    for i in range(0, 800):
        if i == 800:
            ship = ally.create_polygon(xa, ya, xb, yb, xc, yc, fill='red', width=4)
            ship.pack()
        else:
            ally.move(ship, 1, 0)
            ship.pack()