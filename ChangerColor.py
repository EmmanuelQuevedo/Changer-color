from tkinter import*
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser

def comprobar():
    respuesta = red.get() + green.get() + blue.get()
    print(respuesta)
    respuesta2=(len(respuesta))

    if (respuesta2==6):
        root.config(bg=("#" + respuesta))
        titulo1.config(bg=("#" + respuesta))
        colored.config(bg=("#" + respuesta))
        colorgreen.config(bg=("#" + respuesta))
        colorblue.config(bg=("#" + respuesta))
        
    else:
          MessageBox.showwarning("Alerta", "El numero de caracteres no es el adecuado\n Por favor verifiquelo")


root = Tk()
root.geometry("320x150")
root.title("Changer Color")
root.grid()
root.iconbitmap("colorHEX.ico")

red=StringVar()
green=StringVar()
blue=StringVar()




titulo1=Label(root, text="Cambiar Color", font=("Roboto", 20), fg="#000000")
titulo1.grid(row=1, column=4)


        
colored= Label(root, text="Red:", font="Roboto", fg="#f51e05")
colored.grid(row=5, column=3)
redTexto= Entry(root,textvariable=red)
redTexto.grid(row=5, column=4)

colorgreen= Label(root, text="Green:", font="Roboto",  fg="#27AE60")
colorgreen.grid(row=7, column=3)
greenTexto= Entry(root,textvariable=green)
greenTexto.grid(row=7, column=4)

colorblue= Label(root, text="Blue:", font="Roboto", fg="#1113db")
colorblue.grid(row=10, column=3)
blueTexto= Entry(root,textvariable=blue)
blueTexto.grid(row=10, column=4)


boton1=Button(root,text="Set Color", fg="#000000", bg="#fff", font=("Roboto", 12), command=comprobar)
boton1.grid(row=13, column=4)


root.mainloop()
