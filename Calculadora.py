from tkinter import *

class myFrames(Frame):

    def __init__(self, master=None):
        self.numPan=StringVar()
        self.op=''
        self.aux=''
        self.r=0
        super().__init__(master, bg='#BDD7EE')
        self.master=master
        self.pack()
        self.create_widgets()

    def btnPress(self, num):
            if self.numPan.get()=='0':
                 self.op='aux'
            if self.op!='':
                 self.numPan.set(num)
                 self.op=''
            else:
                self.numPan.set(self.numPan.get()+num)
    
    def operation(self,op):
        if self.aux=='' or self.aux=='=':
            self.r=int(self.numPan.get())
        if self.aux=='/' and self.r!=0:
             self.r/=int(self.numPan.get())
             if self.r==int(self.r):
                  self.r=int(self.r)
             self.numPan.set(str(self.r))
        elif self.aux=='*' and self.r!=0:
             self.r*=int(self.numPan.get())
             self.numPan.set(str(self.r))
        elif self.aux=='-' and self.r!=0:
             self.r-=int(self.numPan.get())
             self.numPan.set(str(self.r))
        elif self.aux=='+' and self.r!=0:
             self.r+=int(self.numPan.get())
             self.numPan.set(str(self.r))
        if op=='=' and self.r!=0:
             self.numPan.set(str(self.r))
             self.aux=''
             self.r=0
        self.op=op
        self.aux=op

    def create_widgets(self):
        if self.r==0:
             self.numPan.set(0)
        self.Screen=Label(self, width=6, height=3, textvariable=self.numPan , bg='#000000', fg='#FFFFFF', anchor='e', justify='right', font='18')
        self.Screen.grid(row=0, column=0,columnspan=4, sticky=EW)
        self.btn7=Button(self, text='7', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('7'))
        self.btn7.grid(row=1, column=0)
        self.btn8=Button(self, text='8', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('8'))
        self.btn8.grid(row=1, column=1)
        self.btn9=Button(self, text='9', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('9'))
        self.btn9.grid(row=1, column=2)
        self.btnDiv=Button(self, text='/', width=6, height=3, bg='#BDD7EE', command=lambda:self.operation('/'))
        self.btnDiv.grid(row=1, column=3)
        self.btn4=Button(self, text='4', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('4'))
        self.btn4.grid(row=2, column=0)
        self.btn5=Button(self, text='5', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('5'))
        self.btn5.grid(row=2, column=1)
        self.btn6=Button(self, text='6', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('6'))
        self.btn6.grid(row=2, column=2)
        self.btnMul=Button(self, text='*', width=6, height=3, bg='#BDD7EE', command=lambda:self.operation('*'))
        self.btnMul.grid(row=2, column=3)
        self.btn1=Button(self, text='1', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('1'))
        self.btn1.grid(row=3, column=0)
        self.btn2=Button(self, text='2', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('2'))
        self.btn2.grid(row=3, column=1)
        self.btn3=Button(self, text='3', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('3'))
        self.btn3.grid(row=3, column=2)
        self.btnSub=Button(self, text='-', width=6, height=3, bg='#BDD7EE', command=lambda:self.operation('-'))
        self.btnSub.grid(row=3, column=3)
        self.btnPtn=Button(self, text='.', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('.'))
        self.btnPtn.grid(row=4, column=0)
        self.btn0=Button(self, text='0', width=6, height=3, bg='#BDD7EE', command=lambda:self.btnPress('0'))
        self.btn0.grid(row=4, column=1)
        self.btnEq=Button(self, text='=', width=6, height=3, bg='#BDD7EE', command=lambda:self.operation('='))
        self.btnEq.grid(row=4, column=2)
        self.btnAdd=Button(self, text='+', width=6, height=3, bg='#BDD7EE', command=lambda:self.operation('+'))
        self.btnAdd.grid(row=4, column=3)


def main():
    root=Tk()
    root.geometry('380x380')
    taskBar=Menu(root)
    root.config(menu=taskBar)    
    task=Menu(taskBar, tearoff=0)
    task.add_command(label='Comando 1')
    task.add_separator()
    task.add_command(label='Comando 2')
    taskBar.add_cascade(label='Comandos', menu=task)
    root.title('Calculadora')
    app=myFrames(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()