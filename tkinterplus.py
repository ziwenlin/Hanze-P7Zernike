""" 
LIBRARY CREATED BY ZIWENLIN

"""

import tkinter
import tkinter.ttk


class Application:
    """ Regelaar voor tkinter hoofdvenster. """
    def createOverlay(self, widgetclass):
        overlay = widgetclass(self.app)
        overlay.pack(fill='both', expand=True)
        self.overlays += [overlay]

    def mainloop(self):
        self.app.mainloop()

    def __init__(self, title):
        """ Maakt een hoofdvenster aan. """
        self.app = tkinter.Tk()
        self.app.title(title)
        self.overlays = []

class Window:
    """ Regelaar voor tkinter toplevel venster. """
    def createOverlay(self, widgetclass):
        overlay = widgetclass(self.app)
        overlay.pack(fill='both', expand=True)
        self.overlays += [overlay]
        
    def __init__(self, title):
        """ Maakt een nieuwe venster aan. """
        self.app = tkinter.Toplevel()
        self.app.title(title)
        self.overlays = []
    

class Notebook:
    """ Notebook is een widget die een collectie 
        van vensters beheerd. Deze weergeeft hij een voor een.
        Een venster kan worden weergeven door een van de tabbladen 
        te selecteren. Deze notebook kan de tabbladen groeperen. """
    def switchGroup(self, group):
        """ Wissel van tabblad groep 
        en weergeef het eerste tabblad. """
        for _group in self.groups:
            if _group != group:
                self.hideGroup(_group)
        self.showGroup(group)

    def hideGroup(self, group):
        """ Verberg tabblad groep. """
        for widget in self.groups[group]:
            self.app.hide(widget.app)

    def showGroup(self, group):
        """ Weergeef tabblad groep en weergeef 
        het eerste tabblad van de groep. """
        for widget in self.groups[group]:
            self.app.add(widget.app)
        self.app.select(self.groups[group][0].app)

    def createGroup(self, group):
        """ Maak een nieuwe groep aan 
        en ga verwijs de volgende nieuwe tabbladen aan deze groep. """
        self.groups[group] = list()
        self.group = group

    def selectGroup(self, group):
        """ Verwijs de volgende nieuwe tabbladen aan deze groep """
        if group in self.groups:
            self.group = group
            return
        print("Group %s is onbekend." % group)

    def createTab(self, frameclass, text):
        """ Maak een nieuw tabblad aan.
        Voordat een tabblad aan een groep kan worden gebonden,
        moet de groep eerst worden gemaakt. """
        widget = frameclass(self.app)
        self.app.add(widget.app, text=text)
        if self.group is not None:
            self.app.hide(widget.app)
        self.groups[self.group] += [widget]

    def pack(self, cnf={}, **kwargs):
        """ Pack a widget in the parent widget. """
        self.app.pack(cnf=cnf, **kwargs)

    def initialisatie(self):
        """ Overschrijf deze functie in plaats van __init__(). """

    def __init__(self, master, *args, **kwargs):
        """ Notebook is een widget die een collectie 
        van vensters beheerd. Deze weergeeft hij een voor een.
        Een venster kan worden weergeven door een van de tabbladen 
        te selecteren. Deze notebook kan de tabbladen groeperen. """
        self.app = tkinter.ttk.Notebook(master, *args, **kwargs)
        self.app.app = self
        self.groups = {None:list()}
        self.group = None
        self.initialisatie()


class Frame:
    """ Basis voor alle standaard frames widgets. \n
    Gebruik   initialisatie()   in plaats van __init__(). \n
    Tabel widget:
    createList, setList, clearList \n
    Invoer widgets:
    createEntry, createEntryChoices, getEntries, clearEntries \n
    Invoer knop: 
    createEntryClear \n
    Invoerknop widget:
    createButtonEntry, getButtenEntry \n
    Overige widgets:
    createButton, createLabel """

    def __init__(self, master, *args, **kwargs):
        """ Construct a Ttk Frame with parent master. \n
        STANDARD OPTIONS
        class, cursor, style, takefocus \n
        WIDGET-SPECIFIC OPTIONS
        borderwidth, relief, padding, width, height """
        self.app = tkinter.ttk.Frame(master, *args, **kwargs)
        self.master = master.app
        self.entries = {}
        self.labels = {}
        self.initialisatie()

    def initialisatie(self):
        """ Overschrijf deze functie in plaats van __init__(). """

    def pack(self, cnf={}, **kwargs):
        """ Pack a widget in the parent widget. """
        self.app.pack(cnf=cnf, **kwargs)

    def createTable(self, columns):
        ''' Maakt een tabel aan. Er kan maar één tabel 
        aanwezig zijn in een Frame. \n
        Columns moet een 'list' of 'tuple' zijn. \n
        Returns List '''
        self.list = tkinter.ttk.Treeview(self.app)
        self.list.pack(side='top', fill='both', expand=True)
        self.list["show"] = "headings"
        self.list["columns"] = columns
        for column in columns:
            self.list.heading(column, text=column, anchor='center')
            self.list.column(column, width=90, anchor='center')
        return self.list

    def clearTable(self):
        """ Verwijder alle data in de tabel """
        self.list.delete(*self.list.get_children())

    def setTable(self, data):
        ''' Voegt de data toe in de tabel. \n
        Data moet een 'list' of 'tuple' zijn. '''
        self.clearTable()
        for values in data:
            self.list.insert("", "end", values=values)

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
        holder = tkinter.ttk.Frame(self.app)
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

    def createEntryClear(self, buttontext):
        """ Maak een knop om alle invoervelden te wissen. \n
        Returns Button. """
        return self.createButton(buttontext, self.clearEntries)

    def clearEntries(self):
        """ Wis alle invoervelden. """
        for entry in self.entries:
            string = self.entries[entry]
            string.set(string.std)

    def createEntry(self, text, shortname="None", std=None):
        ''' Maakt een tekstvak en invoerveld aan. \n
        Text beschrijft wat de invoer is. 
        Shortname is de type invoer. \n
        Returns Entry. '''
        if std is None:
            std = ""
        string = tkinter.StringVar(value=std)
        string.std = std
        holder = tkinter.ttk.Frame(self.app)
        label = tkinter.ttk.Label(holder, text=text, width=20)
        entry = tkinter.ttk.Entry(holder, textvariable=string)
        holder.pack(side='top', fill='both')
        label.pack(side='left', fill='both', expand=True, padx=10)
        entry.pack(side='right', fill='both', expand=True)
        self.entries[shortname] = string
        return entry

    def createEntryChoice(self, text, choices=[], shortname="None", std=None):
        ''' Maakt een tekstvak met keuzevak aan. \n
        Text is de beschrijving van de keuzes.
        Choices zijn de mogelijke keuzes. 
        Shortname is de type invoer.
        Standard is de begin waarde. \n
        Returns EntryChoice. '''
        if std is None:
            std = choices[0]
        string = tkinter.StringVar(value=std)
        string.std = std
        holder = tkinter.ttk.Frame(self.app)
        label = tkinter.ttk.Label(holder, text=text, width=10)
        entry = tkinter.ttk.OptionMenu(holder, string, std, *choices)
        holder.pack(side='top', fill='both')
        label.pack(side='left', fill='both', expand=True, padx=10)
        entry.pack(side='right', fill='both', expand=True)
        self.entries[shortname] = string
        return entry

    def createButton(self, text, function):
        ''' Maakt een knop aan. \n 
        Text beschrijft wat de knop is. \n 
        Function is de functie die de knop uitvoert wanneer die is ingedrukt. \n
        Returns Button. '''
        button = tkinter.ttk.Button(self.app, text=text, command=function)
        button.pack(side='top', fill='both', padx=10, pady=10)
        return button

    def createLabel(self, label):
        ''' Maakt een informatiepaneel aan. In deze paneel 
        kan informatie worden weergeven. \n
        Returns Label. '''
        self.labels[label] = tkinter.ttk.Label(self.app, wraplength=400)
        self.labels[label].pack(fill="both", padx=10, pady=10)


class Grid(tkinter.ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)


if __name__ == "__main__":
    import P7Zernike as pz
    tk = tkinter.Tk()
    # registratie = pz.SignUp(tk)
    # registratie.pack(fill='both', expand=True)
    autostatus = pz.UserCarStatus(tk)
    autostatus.pack(fill='both', expand=True)

    tk.mainloop()
