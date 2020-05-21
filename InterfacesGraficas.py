#PyQT
#PYGTK
#Tkinter
#WXPython

from tkinter import *

raiz = Tk()
raiz.title("Nueva ventana")
raiz.resizable(True, True)
raiz.config(bg="blue", bd=10, relief="groove", cursor="hand1")
#raiz.resizable(True, 0)
#raiz.iconbitmap("imagen.ico")

miFrame = Frame(raiz)
miFrame.pack(fill="y", expand="True")
miFrame.config(width="450", height="650", bg="green")
miFrame.config(relief="sunken", bd=40, cursor="hand2")

miImagen = PhotoImage(file="android.png")
Label(miFrame, image=miImagen).place(x=0, y=0)
#miLabel=Label(miFrame, text="Hola como estas?", fg="red", font=("Arial", 20))
#miLabel.place(x=150, y=200)

raiz.mainloop()



