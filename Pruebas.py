import tkinter as tk
import tkinter.font as tkfont
import tkinter.ttk as ttk
import sqlite3 as sql

class MyFrames(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master, width=992, height=330, bg='#E2EFDA')
        #Se crean unas ayudas especiales para control de texto
        self.bold=tkfont.Font(self, family='Helvetica', weight='bold')
        self.italic=tkfont.Font(self, family='Helvetica', slant='italic')
        self.boldtalic=tkfont.Font(self, family='Helvetica', weight='bold', slant='italic')
        self.master=master
        self.pack()
        self.mainMenu()

    def addDLC(self):
        self.miConexion=sql.connect("DBD.db")
        self.miCursor=self.miConexion.cursor()
        self.info=(self.txtDLC.get(),self.txtDLCCost.get(),self.txtDLCSale.get())
        self.dlc='"{}"'.format(self.info[0])
        self.miCursor.execute('INSERT INTO DLC VALUES (NULL,?,0,?,?,0)',self.info)
        self.miConexion.commit()
        self.miConexion.close()
    
    def addCharacter(self):
        self.miConexion=sql.connect("DBD.db")
        self.miCursor=self.miConexion.cursor()
        self.table=self.Roll.get()
        self.addingdlc=self.miCursor.execute('SELECT ID FROM DLC WHERE Name='+self.dlc).fetchone()
        self.info=(self.txtCharacter.get(), self.txtPerk1.get(), self.txtValue1.get(), self.txtPerk2.get(), self.txtValue2.get(), self.txtPerk3.get(), self.txtValue3.get())
        self.intConvenience=int(str(self.info[2]))+int(str(self.info[4]))+int(str(self.info[6]))
        try:
            self.inttotalConvenience=self.inttotalConvenience+self.intConvenience
        except AttributeError:
            self.inttotalConvenience=0
        self.totalconvenience='{}'.format(self.intConvenience)
        self.totalconvenience='{}'.format(self.inttotalConvenience)
        self.miCursor.execute('INSERT INTO ' + self.table +' VALUES (NULL,?,?,?,?,?,?,?,'+self.convenience+','+str(self.addingdlc[0])+')', self.info)
        self.miCursor.execute('UPDATE DLC SET Convenience='+self.totalConvenience+'WHERE ID='+str(self.addingdlc[0]))
        self.miConexion.commit()
        self.miConexion.close()
        self.txtCharacter.delete(0, tk.END)
        self.txtPerk1.delete(0, tk.END)
        self.txtValue1.delete(0, tk.END)
        self.txtPerk2.delete(0, tk.END)
        self.txtValue2.delete(0, tk.END)
        self.txtPerk3.delete(0, tk.END)
        self.txtValue3.delete(0, tk.END)
        self.txtCharacter.insert(0, 'Type here')
        self.txtCharacter.config(fg='grey')
        self.txtPerk1.insert(0, 'Type here')
        self.txtPerk1.config(fg='grey')
        self.txtValue1.insert(0, 'Type here')
        self.txtValue1.config(fg='grey')
        self.txtPerk2.insert(0, 'Type here')
        self.txtPerk2.config(fg='grey')
        self.txtValue2.insert(0, 'Type here')
        self.txtValue2.config(fg='grey')
        self.txtPerk3.insert(0, 'Type here')
        self.txtPerk3.config(fg='grey')
        self.txtValue3.insert(0, 'Type here')
        self.txtValue3.config(fg='grey')
        app.focus()

    def readCharacter(self, roll):
        self.miConexion=sql.connect("DBD.db")
        self.miCursor=self.miConexion.cursor()
        self.Characer=self.miCursor.execute('''SELECT Killers.Name, Killers.Perk1, Killers.Value1, Killers.Perk2, Killers.Value2, Killers.Perk3, Killers.Value3
                                                FROM Killers
                                                JOIN DLC ON Killers.DLC = DLC.ID
                                                WHERE DLC.Owned = 1
                                                ORDER BY DLC.Convenience DESC
                                                LIMIT 1''')
        self.miConexion.commit()
        self.miConexion.close()
        

    def readDLC(self):
        self.miConexion=sql.connect("DBD.db")
        self.miCursor=self.miConexion.cursor()
        self.DLCList=self.miCursor.execute('SELECT Name,Convenience Conv FROM DLC').fetchone()
        print(self.DLCList)
        self.miConexion.commit()
        self.miConexion.close()
        return self.DLCList

    def windowChange(self, window):
        for widget in app.winfo_children():
            widget.destroy()
        if window=='DLC1':
            self.DLC1(0)
        elif window=='DLC2':
            self.DLC1(1)
        else:
            window=getattr(self, window)
            window()
    
    def mainMenu(self):
        tk.Button(self, text='Prestige', bg='#7030A0', font=self.boldtalic, fg='white', command=lambda: self.windowChange('Prestige')).place(x=124, y=66, width=248, height=66)
        tk.Button(self, text='Purchases', bg='#7030A0', font=self.boldtalic, fg='white', command=lambda: self.windowChange('Purchases')).place(x=620, y=66, width=248, height=66)
        tk.Button(self, text='Add new DLC', bg='#7030A0', font=self.boldtalic, fg='white', command=lambda: self.windowChange('DLC1')).place(x=124, y=198, width=248, height=66)
        tk.Button(self, text='Modify DLC', bg='#7030A0', font=self.boldtalic, fg='white', command=lambda: self.windowChange('DLC2')).place(x=620, y=198, width=248, height=66)

    def Prestige(self):
        tk.Label(self, text='Jugando:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=33, width=248, height=33)
        self.cmbPlaying=ttk.Combobox(self, values=['Survivor','Killer'], state='readonly', font=self.italic, justify='center')
        self.cmbPlaying.current(0)
        self.cmbPlaying.place(x=372, y=33, width=248, height=33)
        self.cmbPlaying.bind('<<ComboboxSelected>>', selectPlaying)
        tk.Label(self, text='Personaje:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=66, width=248, height=33)
        self.character=self.readCharacter(self.cmbPlaying.get())
        tk.Label(self, text=self.character, bg='#8EA9DB', relief=tk.SOLID, fg='black', font=self.italic).place(x=372, y=66, width=248, height=33)
        tk.Label(self, text='Perks', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=132, width=744, height=33)
        self.perks=self.getPerks(self.character)
        tk.Label(self, text=self.perks[0], bg=self.perks[1], relief=tk.SOLID, fg='white', font=self.italic).place(x=124, y=165, width=248, height=33)
        tk.Label(self, text=self.perks[2], bg=self.perks[3], relief=tk.SOLID, fg='white', font=self.italic).place(x=372, y=165, width=248, height=33)
        tk.Label(self, text=self.perks[4], bg=self.perks[5], relief=tk.SOLID, fg='white', font=self.italic).place(x=620, y=165, width=248, height=33)
        tk.Button(self, text='Prestige', bg='#7030A0', font=self.boldtalic, fg='white').place(x=372, y=231, width=248, height=66)
        

    def Purchases(self):
        tk.Label(self, text='DLC:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=99, width=248, height=33)
        self.selDLC=tk.StringVar()
        self.selDLC.set('Seleccionar')
        self.availableDLC=self.readDLC()
        print(self.availableDLC)
        self.cmbDLC=ttk.Combobox(self, values=[DLC[0] for DLC in self.availableDLC], state='readonly', font=self.italic, justify='center', textvariable=self.selDLC)
        self.cmbDLC.place(x=372, y=99, width=248, height=33)
        self.cmbDLC.bind('<<ComboboxSelected>>', selectPlaying)
        tk.Label(self, text='Conveniencia:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=132, width=248, height=33)
        tk.Label(self, text='Null', bg='#8EA9DB', relief=tk.SOLID, fg='black', font=self.italic).place(x=372, y=132, width=248, height=33)
        tk.Label(self, text='Precios:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=165, width=248, height=66)
        tk.Label(self, text='Null', bg='#8EA9DB', relief=tk.SOLID, fg='black', font=self.italic).place(x=372, y=165, width=248, height=33)
        tk.Label(self, text='Null', bg='#8EA9DB', relief=tk.SOLID, fg='black', font=self.italic).place(x=372, y=198, width=248, height=33)
        tk.Button(self, text='Purchased', bg='#7030A0', fg='white', font=self.boldtalic).place(x=744, y=132, width=124, height=66)
                                                                                               
    def DLC1(self, set):
        tk.Label(self, text='DLC:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=99, width=248, height=33)
        tk.Label(self, text='Precios:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=165, width=248, height=66)
        self.txtDLC=tk.Entry(self, font=self.italic, justify='center', fg='grey')
        self.txtDLCConvenience=tk.Entry(self, font=self.italic, justify='center', fg='grey')
        self.txtDLCCost=tk.Entry(self, font=self.italic, justify='center', fg='grey')
        self.txtDLCSale=tk.Entry(self, font=self.italic, justify='center', fg='grey')
        
        if set==0:
            self.txtDLC.insert(0, 'Type here')
            self.txtDLCCost.insert(0, 'Type here')
            self.txtDLCSale.insert(0, 'Type here')
            self.txtDLC.bind('<FocusIn>', on_entry_click)
            self.txtDLC.bind('<FocusOut>', on_entry_focusout)
            self.txtDLC.bind('<Return>', on_entry1_keypress)
            self.txtDLC.bind('<Tab>', on_entry1_keypress)
            self.txtDLCCost.bind('<FocusIn>', on_entry_click)
            self.txtDLCCost.bind('<FocusOut>', on_entry_focusout)
            self.txtDLCCost.bind('<Return>', on_entry1_keypress)
            self.txtDLCCost.bind('<Tab>', on_entry1_keypress)
            self.txtDLCSale.bind('<FocusIn>', on_entry_click)
            self.txtDLCSale.bind('<FocusOut>', on_entry_focusout)
            self.txtDLCSale.bind('<KeyPress>', on_entry2_keypress)
            self.txtDLC.place(x=372, y=99, width=248, height=33)
            self.txtDLCCost.place(x=372, y=165, width=248, height=33)
            self.txtDLCSale.place(x=372, y=198, width=248, height=33)
            tk.Button(self, text='Next Step', bg='#7030A0', fg='white', font=self.boldtalic, command=lambda: self.DLCCharacter(set)).place(x=744, y=132, width=124, height=66)
        elif set==1:
            self.selDLC=tk.StringVar()
            self.selDLC.set('Seleccionar')
            self.availableDLC
            self.cmbPlaying=ttk.Combobox(self, values=['Survivor','Killer'], state='readonly', font=self.italic, justify='center', textvariable=self.playing)
            self.cmbPlaying.place(x=372, y=33, width=248, height=33)
            self.cmbPlaying.bind('<<ComboboxSelected>>', selectPlaying)


    def DLCCharacter(self, set):
        self.addDLC()
        for widget in app.winfo_children():
            widget.destroy()
        tk.Label(self, text='Team:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=66, width=248, height=33)
        tk.Label(self, text='Name:', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=99, width=248, height=33)
        tk.Label(self, text='Perks | Value', bg='#305496', relief=tk.SOLID, fg='white', font=self.bold).place(x=124, y=165, width=744, height=33)
        if set==0:
            self.txtCharacter=tk.Entry(self, font=self.italic, justify='center', fg='grey')
            self.txtPerk1=tk.Entry(self, font=self.italic, justify='center', fg='grey')
            self.txtValue1=tk.Entry(self, font=self.italic, justify='center', fg='grey')
            self.txtPerk2=tk.Entry(self, font=self.italic, justify='center', fg='grey')
            self.txtValue2=tk.Entry(self, font=self.italic, justify='center', fg='grey')
            self.txtPerk3=tk.Entry(self, font=self.italic, justify='center', fg='grey')
            self.txtValue3=tk.Entry(self, font=self.italic, justify='center', fg='grey')
            self.txtCharacter.insert(0, 'Type here')
            self.txtPerk1.insert(0, 'Type here')
            self.txtValue1.insert(0, 'Type here')
            self.txtPerk2.insert(0, 'Type here')
            self.txtValue2.insert(0, 'Type here')
            self.txtPerk3.insert(0, 'Type here')
            self.txtValue3.insert(0, 'Type here')
            self.txtCharacter.bind('<FocusIn>', on_entry_click)
            self.txtCharacter.bind('<FocusOut>', on_entry_focusout)
            self.txtCharacter.bind('<Return>', on_entry1_keypress)
            self.txtPerk1.bind('<FocusIn>', on_entry_click)
            self.txtPerk1.bind('<FocusOut>', on_entry_focusout)
            self.txtPerk1.bind('<Return>', on_entry1_keypress)
            self.txtValue1.bind('<FocusIn>', on_entry_click)
            self.txtValue1.bind('<FocusOut>', on_entry_focusout)
            self.txtValue1.bind('<Return>', on_entry1_keypress)
            self.txtPerk2.bind('<FocusIn>', on_entry_click)
            self.txtPerk2.bind('<FocusOut>', on_entry_focusout)
            self.txtPerk2.bind('<Return>', on_entry1_keypress)
            self.txtValue2.bind('<FocusIn>', on_entry_click)
            self.txtValue2.bind('<FocusOut>', on_entry_focusout)
            self.txtValue2.bind('<Return>', on_entry1_keypress)
            self.txtPerk3.bind('<FocusIn>', on_entry_click)
            self.txtPerk3.bind('<FocusOut>', on_entry_focusout)
            self.txtPerk3.bind('<Return>', on_entry1_keypress)
            self.txtValue3.bind('<FocusIn>', on_entry_click)
            self.txtValue3.bind('<FocusOut>', on_entry_focusout)
            self.txtValue3.bind('<Return>', on_entry2_keypress)
            self.txtCharacter.place(x=372, y=99, width=248, height=33)
            self.txtPerk1.place(x=124, y=198, width=248, height=33)
            self.txtValue1.place(x=124, y=231, width=248, height=33)
            self.txtPerk2.place(x=372, y=198, width=248, height=33)
            self.txtValue2.place(x=372, y=231, width=248, height=33)
            self.txtPerk3.place(x=620, y=198, width=248, height=33)
            self.txtValue3.place(x=620, y=231, width=248, height=33)
            self.rollTxt=tk.StringVar()
            self.rollTxt.set('Seleccionar')
            self.Roll=ttk.Combobox(self, values=['Survivors','Killers'], state='readonly', font=self.italic, justify='center', textvariable=self.rollTxt)
            self.Roll.current(0)
            self.Roll.place(x=372, y=66, width=248, height=33)
            self.Roll.bind('<<ComboboxSelected>>', selectPlaying)
            tk.Button(self, text='Next', bg='#7030A0', fg='white', font=self.boldtalic, command=lambda: self.addCharacter()).place(x=744, y=66, width=124, height=66)

    def getPerks(self, character):
        if character=='Undefined':
            return ('Perk 1', '#5B0F00', 'Perk 2', '#5B0F00', 'Perk 3', '#5B0F00')
        else:
            return 'Nothing'

def selectPlaying(event):
    app.focus_force()


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
    root.geometry('992x330')
    root.resizable(False, False)
    root.title('My DBD Tracker')
    global app
    app=MyFrames(master=root)
    taskBar=tk.Menu(root)
    root.config(menu=taskBar)    
    windowMenu=tk.Menu(taskBar, tearoff=0)
    windowMenu.add_command(label='Prestige', command=lambda: MyFrames.windowChange(app,'Prestige'))
    windowMenu.add_command(label='Purchases')
    windowMenu.add_separator()
    windowMenu.add_command(label='Main Menu', command=lambda: MyFrames.windowChange(app,'mainMenu'))
    taskBar.add_cascade(label='Windows', menu=windowMenu)
    dlcMenu=tk.Menu(taskBar, tearoff=0)
    dlcMenu.add_command(label='Add new')
    dlcMenu.add_command(label='Modify')
    taskBar.add_cascade(label='DLC', menu=dlcMenu)
    app.mainloop()

if __name__ == '__main__':
    main()

'''
Fondo verde: #E2EFDA
Azul obscuro: #305496
Azul claro: #8EA9DB
Rojo: #5B0F00
Amarillo: #BF9000
Verde: #38761D
Azul: #1155CC
Morado: #7030A0
Blanco: #000000
Negro: #FFFFFF
'''