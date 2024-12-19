import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont

class Name(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=868, height=297, bg='#F1F8EC')
        self.bold=tkfont.Font(self, family='Helvetica', weight='bold')
        self.italic=tkfont.Font(self, family='Helvetica', slant='italic')
        self.boldtalic=tkfont.Font(self, family='Helvetica', weight='bold', slant='italic')
        self.master=master
        self.pack()
        self.create_widgets()
    
    def duplicate(self):
        self.moneytxt.config(state=tk.NORMAL)
        self.champagnetxt.config(state=tk.NORMAL)
        self.diamondstxt.config(state=tk.NORMAL)
        self.money=float(self.moneytxt.get())
        self.money*=0.9
        self.champagne=int(self.champagnetxt.get())
        self.champagne*=2
        self.diamonds=int(self.diamondstxt.get())
        self.diamonds*=2
        self.moneytxt.delete(0, tk.END)
        self.champagnetxt.delete(0, tk.END)
        self.diamondstxt.delete(0, tk.END)
        self.moneytxt.insert(0, str(int(self.money)))
        self.champagnetxt.insert(0, str(int(self.champagne)))
        self.diamondstxt.insert(0, str(int(self.diamonds)))
        self.moneytxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
        self.champagnetxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
        self.diamondstxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
        self.svetlanatxt.config(state=tk.NORMAL)
        self.storetxt.config(state=tk.NORMAL)
    
    def TimeForBooze(self):
        self.svetlana=int(self.svetlanatxt.get())
        if (self.champagne>0 and self.champagne>=self.svetlana):
            self.champagne=self.champagne-self.svetlana
            self.diamonds=self.diamonds+self.svetlana
            self.champagnetxt.config(state=tk.NORMAL)
            self.diamondstxt.config(state=tk.NORMAL)
            self.champagnetxt.delete(0, tk.END)
            self.diamondstxt.delete(0, tk.END)
            self.champagnetxt.insert(0, str(int(self.champagne)))
            self.diamondstxt.insert(0, str(int(self.diamonds)))
            self.champagnetxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
            self.diamondstxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
        elif (self.champagne!=0 and self.champagne<self.svetlana):
            self.diamonds=self.diamonds+self.champagne
            self.champagne=0
            self.champagnetxt.config(state=tk.NORMAL)
            self.diamondstxt.config(state=tk.NORMAL)
            self.champagnetxt.delete(0, tk.END)
            self.diamondstxt.delete(0, tk.END)
            self.champagnetxt.insert(0, str(int(self.champagne)))
            self.diamondstxt.insert(0, str(int(self.diamonds)))
            self.champagnetxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
            self.diamondstxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
        else:
            messagebox.showerror("Not possible", "You don't have any Brand Champagne to deliver")
    
    def Sell(self):
        self.store=int(self.storetxt.get())
        if (self.diamonds>0 and self.diamonds>=self.store):
            self.diamonds=self.diamonds-self.store
            self.money=self.money+(self.store*991)
            self.moneytxt.config(state=tk.NORMAL)
            self.diamondstxt.config(state=tk.NORMAL)
            self.moneytxt.delete(0, tk.END)
            self.diamondstxt.delete(0, tk.END)
            self.moneytxt.insert(0, str(int(self.money)))
            self.diamondstxt.insert(0, str(int(self.diamonds)))
            self.moneytxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
            self.diamondstxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
        elif (self.diamonds!=0 and self.diamonds<self.store):
            self.money=self.money+(self.diamonds*991)
            self.diamonds=0
            self.moneytxt.config(state=tk.NORMAL)
            self.diamondstxt.config(state=tk.NORMAL)
            self.moneytxt.delete(0, tk.END)
            self.diamondstxt.delete(0, tk.END)
            self.moneytxt.insert(0, str(int(self.money)))
            self.diamondstxt.insert(0, str(int(self.diamonds)))
            self.moneytxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
            self.diamondstxt.config(state=tk.DISABLED, font=self.boldtalic, disabledbackground="gray", disabledforeground="white")
        else:
            messagebox.showerror("Not possible", "You don't have any Diamonds to sell")

    def create_widgets(self):
        tk.Label(self, text='Money:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=33, width=124, height=33)
        tk.Label(self, text='Champagne:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=66, width=124, height=33)
        tk.Label(self, text='Diamonds:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=99, width=124, height=33)
        tk.Label(self, text='Svetlana:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=165, width=124, height=33)
        tk.Label(self, text='Store:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=231, width=124, height=33)
        self.moneytxt=tk.Entry(self, font=self.italic, justify='left', fg='gray')
        self.champagnetxt=tk.Entry(self, font=self.italic, justify='left', fg='gray')
        self.diamondstxt=tk.Entry(self, font=self.italic, justify='left', fg='gray')
        self.svetlanatxt=tk.Entry(self, font=self.italic, justify='left', fg='gray')
        self.storetxt=tk.Entry(self, font=self.italic, justify='left', fg='gray')
        self.moneytxt.bind('<FocusIn>', on_entry_click)
        self.moneytxt.bind('<FocusOut>', on_entry_focusout)
        self.moneytxt.bind('<Return>', on_entry1_keypress)
        self.moneytxt.bind('<Tab>', on_entry1_keypress)
        self.champagnetxt.bind('<FocusIn>', on_entry_click)
        self.champagnetxt.bind('<FocusOut>', on_entry_focusout)
        self.champagnetxt.bind('<Return>', on_entry1_keypress)
        self.champagnetxt.bind('<Tab>', on_entry1_keypress)
        self.diamondstxt.bind('<FocusIn>', on_entry_click)
        self.diamondstxt.bind('<FocusOut>', on_entry_focusout)
        self.diamondstxt.bind('<Return>', on_entry2_keypress)
        self.diamondstxt.bind('<Tab>', on_entry2_keypress)
        self.svetlanatxt.bind('<FocusIn>', on_entry_click)
        self.svetlanatxt.bind('<FocusOut>', on_entry_focusout)
        self.svetlanatxt.bind('<Return>', on_entry1_keypress)
        self.svetlanatxt.bind('<Tab>', on_entry1_keypress)
        self.storetxt.bind('<FocusIn>', on_entry_click)
        self.storetxt.bind('<FocusOut>', on_entry_focusout)
        self.storetxt.bind('<Return>', on_entry1_keypress)
        self.storetxt.bind('<Tab>', on_entry1_keypress)
        self.moneytxt.insert(0, 'Type here')
        self.champagnetxt.insert(0, 'Type here')
        self.diamondstxt.insert(0, 'Type here')
        self.svetlanatxt.insert(0, 'Type here')
        self.storetxt.insert(0, 'Type here')
        self.moneytxt.place(x=248, y=33, width=124, height=33)
        self.champagnetxt.place(x=248, y=66, width=124, height=33)
        self.diamondstxt.place(x=248, y=99, width=124, height=33)
        self.svetlanatxt.place(x=248, y=165, width=124, height=33)
        self.storetxt.place(x=248, y=231, width=124, height=33)
        self.svetlanatxt.config(state=tk.DISABLED, disabledbackground="gray", disabledforeground="darkgray")
        self.storetxt.config(state=tk.DISABLED, disabledbackground="gray", disabledforeground="darkgray")
        tk.Button(self, text='Duplicate', bg='#7030A0', fg='white', font=self.boldtalic, command=lambda: self.duplicate()).place(x=496, y=66, width=248, height=33)
        tk.Button(self, text='Svetlana', bg='#7030A0', fg='white', font=self.boldtalic, command=lambda: self.TimeForBooze()).place(x=496, y=165, width=248, height=33)
        tk.Button(self, text='Sell', bg='#7030A0', fg='white', font=self.boldtalic, command=lambda: self.Sell()).place(x=496, y=231, width=248, height=33)

def on_entry_click(event):
    if event.widget.get()=='Type here':
            event.widget.delete(0, 'end')
            event.widget.configure(fg='black')

def on_entry_focusout(event):
    if event.widget.get() == '':
        event.widget.insert(0, 'Type here')
        event.widget.configure(fg='grey')

def on_entry1_keypress(event):
    event.widget.tk_focusNext().focus()

def on_entry2_keypress(event):
    app.focus()

def main():
    root=tk.Tk()
    root.title('Sumador de numeros enteros')
    global app
    app=Name(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()