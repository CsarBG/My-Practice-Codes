import tkinter as tk

help(tk.Tk.geometry)
'''

Este codigo nos muestra como hacer para que pase de un entry al otro al pulsar enter o tab
también, al pasar del ultimo este simplemente no selecciona nada

root = tk.Tk()
root.geometry('300x100')

# Creamos los Entry
entry1 = tk.Entry(root, font=('italic', 12))
entry2 = tk.Entry(root, font=('italic', 12))

# Función que se ejecuta cuando se pulsa Enter o Tab en el primer Entry
def on_entry1_keypress(event):
    if event.keysym == 'Return' or event.keysym == 'Tab':
        entry2.focus_set()

# Función que se ejecuta cuando se pulsa Enter o Tab en el segundo Entry
def on_entry2_keypress(event):
    if event.keysym == 'Return' or event.keysym == 'Tab':
        root.focus()

# Asociamos las funciones al evento <KeyPress> de los Entry
entry1.bind('<KeyPress>', on_entry1_keypress)
entry2.bind('<KeyPress>', on_entry2_keypress)

# Empaquetamos los Entry en la ventana
entry1.pack(pady=10)
entry2.pack(pady=10)

root.mainloop()

'''
#---------------------------------------------------------------------------------------------------------------------------#
'''

Este codigo nos muestra como poner un texto provicional en una casilla de entry

root = tk.Tk()

# Creamos la variable de control para el entry
entry_text = tk.StringVar()

# Creamos la función que se ejecuta cuando se hace clic en el entry
def on_entry_click(event):
    # Borramos el texto que hay en el entry si es el texto de ayuda
    if entry.get() == 'Escriba aquí':
        entry.delete(0, 'end')
        entry.configure(fg='black', font=('Arial', 12))

# Creamos la función que se ejecuta cuando se sale del entry
def on_entry_focusout(event):
    # Si no se ha escrito nada, volvemos a poner el texto de ayuda
    if entry.get() == '':
        entry.insert(0, 'Escriba aquí')
        entry.configure(fg='grey', font=('Arial italic', 12))

# Creamos el entry
entry = tk.Entry(root, textvariable=entry_text, width=30, font=('Arial italic', 12), fg='grey')

# Ponemos el texto de ayuda
entry.insert(0, 'Escriba aquí')

# Configuramos el entry para que cambie el texto cuando se hace clic
entry.bind('<FocusIn>', on_entry_click)

# Configuramos el entry para que vuelva a poner el texto de ayuda si no se ha escrito nada
entry.bind('<FocusOut>', on_entry_focusout)

entry.pack()

root.mainloop()

'''