""" 
LIBRARY CREATED BY ZIWENLIN

"""

import tkinter
import tkinter.ttk


class Application(tkinter.Tk):
    def createOverlay(self, widgetclass):
        self.overlays += [widgetclass(self)]

    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.overlays = []

class Window(tkinter.Toplevel):
    def createOverlay(self, widgetclass):
        self.overlays += [widgetclass(self)]
        
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.overlays = []


class Notebook(tkinter.ttk.Notebook):
    def switchGroup(self, group):
        for _group in self.groups:
            if _group is not group:
                self.hideGroup(_group)
        self.showGroup(group)

    def hideGroup(self, group):
        for widget in self.groups[group]:
            self.hide(widget)

    def showGroup(self, group):
        for widget in self.groups[group]:
            self.add(widget)
        self.select(self.groups[group][0])

    def createTab(self, frameclass, text, group=None):
        widget = frameclass(self)
        self.add(widget, text=text)
        if group is not None:
            self.hide(widget)
        try:
            self.groups[group] += [widget]
        except:
            self.groups[group] = [widget]

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.pack(fill='both', expand=True)
        self.groups = {}


class Frame(tkinter.ttk.Frame):
    """ Basis voor alle standaard frames widgets.
    
        Tabel widget:
        createList, setList, clearList

        Invoer widgets:
        createEntry, createEntryChoices, getEntries, clearEntries, createEntryClear
        
        Invoerknop widget:
        createButtonEntry, getButtenEntry

        Overige widgets:
        createButton, createLabel """

    def __init__(self, master, *args, **kwargs):
        """ Construct a Ttk Frame with parent master. \n
            STANDARD OPTIONS
            class, cursor, style, takefocus \n
            WIDGET-SPECIFIC OPTIONS
            borderwidth, relief, padding, width, height """
        super().__init__(master, *args, **kwargs)
        self.entries = {}
        self.labels = {}

    def createTable(self, columns):
        ''' Maakt een tabel aan. Er kan maar één tabel 
        aanwezig zijn in een Frame. \n
        Columns moet een 'list' of 'tuple' zijn. \n
        Returns List '''
        self.list = tkinter.ttk.Treeview(self)
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

    def createEntryClear(self, buttontext):
        """ Maak een knop om alle invoervelden te wissen. \n
        Returns Button. """
        return self.createButton(buttontext, self.clearEntries)

    def clearEntries(self):
        """ Wis alle invoervelden. """
        for entry in self.entries:
            string = self.entries[entry]
            string.set(string.standard)

    def createEntry(self, text, shortname="None", standard=None):
        ''' Maakt een tekstvak en invoerveld aan. \n
        Text beschrijft wat de invoer is. 
        Shortname is de type invoer. \n
        Returns Entry. '''
        if standard is None:
            standard = ""
        string = tkinter.StringVar(value=standard)
        string.standard = standard
        holder = tkinter.ttk.Frame(self)
        label = tkinter.ttk.Label(holder, text=text, width=20)
        entry = tkinter.ttk.Entry(holder, textvariable=string)
        holder.pack(side='top', fill='both')
        label.pack(side='left', fill='both', expand=True, padx=10)
        entry.pack(side='right', fill='both', expand=True)
        self.entries[shortname] = string
        return entry

    def createEntryChoice(self, text, choices=[], shortname="None", standard=None):
        ''' Maakt een tekstvak met keuzevak aan. \n
        Text is de beschrijving van de keuzes.
        Choices zijn de mogelijke keuzes. 
        Shortname is de type invoer.
        Standard is de begin waarde. \n
        Returns EntryChoice. '''
        if standard is None:
            standard = choices[0]
        string = tkinter.StringVar(value=standard)
        string.standard = standard
        holder = tkinter.ttk.Frame(self)
        label = tkinter.ttk.Label(holder, text=text, width=10)
        entry = tkinter.ttk.OptionMenu(holder, string, standard, *choices)
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
        button = tkinter.ttk.Button(self, text=text, command=function)
        button.pack(side='top', fill='both', padx=10, pady=10)
        return button

    def createLabel(self, label):
        ''' Maakt een informatiepaneel aan. In deze paneel 
        kan informatie worden weergeven. \n
        Returns Label. '''
        self.labels[label] = tkinter.ttk.Label(self, wraplength=400)
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
