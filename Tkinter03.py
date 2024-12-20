import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.maker=master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.hi_there=tk.Button(self)
        self.hi_there['text']='Hello world\n(Click me)'
        self.hi_there['command']=self.say_hi
        self.hi_there.pack(side='top')
        self.quit=tk.Button(self, text='Quit', fg='red', command=self.master.destroy)
        self.quit.pack(side='bottom')
    def say_hi(self):
        print('Hi there, everyone!')

def main():
    root=tk.Tk()
    app=Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()