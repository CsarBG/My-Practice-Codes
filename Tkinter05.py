from tkinter import Tk, Frame, Label, Button, Entry, messagebox
from tkinter.ttk import Combobox
import libFraccion as Frac
import libFracMix as FracM

class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master=master
        self.pack()
        self.create_widgets()
        
    def fCalcular(self):
        e1=int(self.text1E.get())
        n1=int(self.text1N.get())
        d1=int(self.text1D.get())
        f1=FracM.FracMix(e1,n1,d1)
        e2=int(self.text2E.get())
        n2=int(self.text2N.get())
        d2=int(self.text2D.get())
        f2=FracM.FracMix(e2,n2,d2)

        if self.cmb1.get()==self.opciones[4]:
            if f1==f2:
                messagebox.showinfo(title='Fracciones mixtas', message='Las fracciones son iguales')
            else:
                messagebox.showinfo(title='Fracciones mixtas', message='Las fracciones son diferentes') 
        else:
            if self.cmb1.get()==self.opciones[0]:
                f3=f1+f2
            elif self.cmb1.get()==self.opciones[1]:
                f3=f1-f2
            elif self.cmb1.get()==self.opciones[2]:
                f3=f1*f2
            elif self.cmb1.get()==self.opciones[3]:
                f3=f1/f2
            self.textRes.delete(0,'end')
            self.textRes.insert(0,f3)

    def create_widgets(self):
        fFrac1=Frame(self, width=100, height=60)
        fFrac1.place(x=30, y=30)
        fx1=Frame(fFrac1, width=42, height=27)
        fx1.grid(row=0, column=0, rowspan=2)
        Label(fx1, text='Ent').pack(side='left')
        self.text1E=Entry(fx1, width=4)
        self.text1E.pack(side='right')
        Label(fFrac1, text='Num').grid(row=0, column=2)
        Label(fFrac1, text='Den').grid(row=1, column=2)
        self.text1N=Entry(fFrac1, width=4)
        self.text1N.grid(row=0, column=1)
        self.text1D=Entry(fFrac1, width=4)
        self.text1D.grid(row=1, column=1)

        fFrac2=Frame(self, width=100, height=60)
        fFrac2.place(x=180, y=30)
        fx2=Frame(fFrac2, width=42, height=27)
        fx2.grid(row=0, column=0, rowspan=2)
        Label(fx2, text='Ent').pack(side='left')
        self.text2E=Entry(fx2, width=4)
        self.text2E.pack(side='right')
        Label(fFrac2, text='Num').grid(row=0, column=2)
        Label(fFrac2, text='Den').grid(row=1, column=2)
        self.text2N=Entry(fFrac2, width=4)
        self.text2N.grid(row=0, column=1)
        self.text2D=Entry(fFrac2, width=4)
        self.text2D.grid(row=1, column=1)

        Label(self, text='Fracción 1:').place(x=48, y=8)
        Label(self, text='Fracción 2:').place(x=198, y=8)
        Label(self, text='Operación:').place(x=30, y=90)
        Label(self, text='Resultado:').place(x=30, y=120)
        self.textRes=Entry(self, width=15)
        self.textRes.place(x=100, y=120)
        self.btn1=Button(self, text='Calcular', command=self.fCalcular)
        self.btn1.place(x=210, y=90)

        self.opciones=['Suma', 'Resta', 'Multiplicación', 'División', 'Igualar']
        self.cmb1=Combobox(self, width='10', values=self.opciones,state='readonly')
        self.cmb1.place(x=100, y=90)
        self.cmb1.current(0)

        # con .current() si ponemos un numero entre el parentesis se selecciona esa opción, si está vacio nos da el valor del indice



def main():
    root=Tk()
    root.title('Fracciones Mixtas')
    app=MainFrame(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()