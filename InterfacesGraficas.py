#PyQT
#PYGTK
#Tkinter
#WXPython

from tkinter import *
raiz = Tk()
raiz.title("Nueva ventana")
raiz.config(bg="blue", bg=10, relief="groove", cursor="hand1")
#raiz.resizable(True, 0)
raiz.resizable(True, True)
raiz.geometry("100x900")
raiz.config(bg="blue")
#raiz.iconbitmap("imagen.ico")
miFrame = Frame()
miFrame.pack(fill="both", expand="True")
miFrame.config(width="450", height="650", bg="green")
miFrame.config(relief="sunken", bd = 40, cursor="hand2")

miImagen = PhotoImage(file="android.png")
miLabel= Label(miFrame, image=miImagen, width=150, heigth=200)
miLabel.place(x=150, y= 200)
#miLabel= Label(miFrame, text="Hola como estas?",fg="red", font=())

raiz.mainloop()



