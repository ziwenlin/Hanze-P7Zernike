import tkinter
import tkinter.ttk

class Frame(tkinter.ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.entries = {}
        self.labels = {}

    def createList(self, columns):
        ''' Maakt een tabel aan. Er kan maar één tabel 
        aanwezig zijn in een Frame. \n
        Columns moet een 'list' of 'tuple' zijn. \n
        Returns List '''
        self.list = tkinter.ttk.Treeview(self)
        self.list.pack(side='top', fill='both', expand=True)
        self.list["columns"] = columns[1:]
        self.list.heading("#0", text=columns[:1])
        self.list.column("#0", width=80)
        for column in columns[1:]:
            self.list.heading(column, text=column)
            self.list.column(column, width=50)
        return self.list

    def getButtonEntry(self):
        ''' Invoerveld uitlezen.
        Verwijder de invoer van zoekveld. \n 
        Returns het kenteken. '''
        text = self.buttonEntry.get()
        self.buttonEntry.delete(0, "end")
        return text

    def createButtonEntry(self, entrytext, buttontext, function):
        ''' Maakt een invoerveld en een knop aan. 
        Er kan maar één invoerveld per Frame aanwezig zijn. \n 
        Entrytext beschrijft wat de gebruiker moet invoeren. \n
        Buttontext beschrijft wat de knop is. \n 
        Function is de functie die de knop uitvoert wanneer die wordt ingedrukt. \n
        Returns ButtonEntry. '''
        holder = tkinter.ttk.Frame(self)
        label = tkinter.ttk.Label(holder, text=entrytext)
        entry = tkinter.ttk.Entry(holder)
        button = tkinter.ttk.Button(holder, text=buttontext, command=function)
        holder.pack(side='top', fill='both')
        button.pack(side='bottom', fill='both', padx=10, pady=10)
        label.pack(side='left', fill='both', padx=10)
        entry.pack(side='left', fill='both')
        self.buttonEntry = entry
        return entry

    def getEntries(self):
        """ Lees alle invoervelden. \n
        Returns Dictonary of Entries """
        register = {}
        for entry in self.entries:
            register[entry] = self.entries[entry].get()
        return register

    def createClearEntries(self, buttontext):
        """ Maak een knop om alle invoervelden te wissen. \n
        Returns Button. """
        return self.createButton(buttontext, self.clearEntries)

    def clearEntries(self):
        """ Wis alle invoervelden. """
        for entry in self.entries:
            self.entries[entry].delete(0, 'end')

    def createEntry(self, text, shortname="None"):
        ''' Maakt een tekstvak en invoerveld aan. \n
        Text beschrijft wat de invoer is. \n
        Shortname is de type invoer. \n
        Returns Entry. '''
        holder = tkinter.ttk.Frame(self)
        label = tkinter.ttk.Label(holder, text=text)
        entry = tkinter.ttk.Entry(holder)
        holder.pack(side='top', fill='both')
        label.pack(side='right', fill='both', expand=True, padx=10)
        entry.pack(side='left', fill='both')
        self.entries[shortname] = entry
        return entry

    def createButton(self, text, function):
        ''' Maakt een knop aan. \n 
        Text beschrijft wat de knop is. \n 
        Function is de functie die de knop uitvoert wanneer die is ingedrukt. \n
        Returns Button. '''
        button = tkinter.ttk.Button(self, text=text, command=function)
        button.pack(side='top', fill='both', padx=10, pady=10)
        return button

    def createLabel(self, label):
        ''' Maakt een informatiepaneel aan. In deze paneel 
        kan informatie worden weergeven. \n
        Returns Label. '''
        self.labels[label] = tkinter.ttk.Label(self)
        self.labels[label].pack(fill="both")

class Grid(tkinter.ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
