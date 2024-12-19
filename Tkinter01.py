#Se trabaja con frames, mientras que Tk() es la ventana, los frames son como secciones dentro de la ventana
#Mientras que no podemos mesclar place, pack, y grid en una sola ventana, si podemos usar frames que usen diferentes

from tkinter import *

def main():
    root=Tk()
    root.title('Ejemplo con 2 Frames')
    root.geometry('200x70')

    frame1=Frame(root, bg='dark blue')
    frame1.pack(expand=True, fill='both')

    frame2=Frame(root, bg='dark green', cursor='heart')
    frame2.pack(expand=True, fill=BOTH)

    redbtn=Button(frame1, text='Red', fg='red')
    brownbtn=Button(frame1, text='Brown', fg='brown')
    bluebtn=Button(frame1, text='Blue', fg='blue')
    redbtn.place(relx=0.05, rely=0.05, relwidth=0.25, relheight=0.9)
    brownbtn.place(relx=0.35, rely=0.05, relwidth=0.25, relheight=0.9)
    bluebtn.place(relx=0.65, rely=0.05, relwidth=0.25, relheight=0.9)

    blackbtn=Button(frame2, text='Black', fg='black')
    blackbtn.pack()

    root.mainloop()

if __name__=='__main__':
    main()