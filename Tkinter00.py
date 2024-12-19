#Se ven las bases para generar una ventana, usar extensión .pyw en vez de .py para abrír la ventana de modo automático

import tkinter as tk

def miFuncion():
    print('El botón funciona')

ventana=tk.Tk()
ventana.title("Mi primer ventana")
ventana.geometry('380x380')
ventana.config(background='dark turquoise')

etiqueta1=tk.Label(ventana, text='Texto de prueba', bg='red', fg='white')
etiqueta1.pack()
#pack está siendo usado para poner el objeto en la ventana:
    #place(x,y,width,height) | también acepta relx, rely, relwidth, relheight para valores relativos con la ventana
    #pack() acepta: side=tk.(LEFT, RIGHT, TOP, o BOTTOM), after/before=objeto,
        #padx y pady son distancias externas, ipadx e ipady son las distancias internas
            #expand=True/False el control expande el margen exterior (padx y pady) para llenarlo todo
            #fill=tk.(BOTH, X, Y) expande los margenes internos (ipadx e ipady) a su máximo 
    #grid(row=y, column=x) los coloca como si fuera una tabla
        #columnspan/rowspan=[Numero de columnas/filas a usar]
        #self.(rowconfigure/columnconfigure)([Numero de fila/columna], weigth=[Cuantas veces aumenta su tamaño]]) 
        #sticky() con n, s, w, e para indicar a qué parte se va a pegar

btn=tk.Button(ventana, text='Botón de prueba', command=miFuncion)
btn.pack()

ventana.mainloop()