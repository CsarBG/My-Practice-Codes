import tkinter as tk

class MyWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master=master
        self.pack()
        self.create_widgets()

    def suma(self):
        n1=self.textNum1.get()
        n2=self.textNum2.get()
        r=int(n1)+int(n2)
        self.textNum3.delete(0, 'end')
        self.textNum3.insert(0, r)

    def create_widgets(self):
        self.lblNum1=tk.Label(self, text='Primer numero: ', bg='yellow')
        self.textNum1=tk.Entry(self, bg='pink')
        self.lblNum2=tk.Label(self, text='Segundo numero: ', bg='yellow')
        self.textNum2=tk.Entry(self, bg='pink')
        self.btn1=tk.Button(self, text='Sumar', command=self.suma)
        self.lblNum3=tk.Label(self, text='Resultado: ', bg='yellow')
        self.textNum3=tk.Entry(self, bg='cyan')

        self.lblNum1.place(x=10, y=10, width=100, height=30)
        self.textNum1.place(x=120, y=10, width=100, height=30)
        self.lblNum2.place(x=10, y=50, width=100, height=30)
        self.textNum2.place(x=120, y=50, width=100, height=30)
        self.btn1.place(x=230, y=50, width=100, height=30)
        self.lblNum3.place(x=10, y=120, width=100, height=30)
        self.textNum3.place(x=120, y=120, width=100, height=30)

def main():
    root=tk.Tk()
    root.title('Sumador de numeros enteros')
    app=MyWindow(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()

"""""
import tkinter as tk

class Name(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=320, height=170, bg='#F1F8EC')
        self.master=master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        pass

def main():
    root=tk.Tk()
    root.title('Titulo')
    app=Name(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
"""