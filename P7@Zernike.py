import tkinter
import tkinter.ttk
import datetime
import time

# from connector import connector
from tkinterplus import Frame


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("P7@Zernike")
        self.menu = Tabbladen(self)


class Tabbladen(tkinter.ttk.Notebook):
    def createTab(self, frameclass, text):
        self.add(frameclass(self), text=text)

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill='both', expand=True)
        self.createTab(CarStatus, "Parkeerstatus")
        self.createTab(CheckIn, "Inchecken")
        self.createTab(CheckOut, "Uitchecken")
        self.createTab(Registration, "Registreren")
        self.createTab(ParkingPlaceStatus, "Parkeerplaats")
        self.createTab(Invoices, "Betalen")


class ParkingPlaceStatus(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createLabel("ParkeerAantal")


class CarStatus(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButtonEntry("Zoeken op kenteken", "Zoeken", self.zoeken)
        self.createLabel("AutoStatus")
        self.createList(("Datum", "Tijd", "Prijs", "Betaald"))

    def displayAutoStatus(self, text):
        ''' Weergeeft de status van het parkeren in de informatiepaneel. '''
        if text is not None:
            text = "Uw huidige parkeertijd is %s uur." % text
        else:
            text = "De auto is niet geparkeerd."
        self.labels["AutoStatus"].config(text=text)

    def displayAutoGeschiedenis(self, data):
        ''' Voegt de data toe in de tabel. \n
        Data moet een 'list' of 'tuple' zijn. '''
        # Verwijder alle data in de tabel
        self.list.delete(*self.list.get_children())
        for values in data:
            self.list.insert("", "end", text=values[:1], values=values[1:])

    def verwerkingAutoStatus(self, opdracht):
        ''' TODO Verbinding maken met de database. '''
        random = time.time() * 100 % 10
        if random < 9:
            if random < 1:
                return datetime.time(hour=0, minute=int(60*random))
            return datetime.time(hour=int(random), minute=int(6*random))
        return None

    def zoeken(self):
        """ Functie van de knop. \n
        Invoerveld uitlezen en daarmee in de database kijken. 
        Data van de database wordt gelezen en verwerkt. 
        De geschiedenis wordt in de tabel weergeven en
        de eventuele huidige parkeersessie wordt 
        in de informatiepaneel weergeven. """
        kenteken = self.getButtonEntry()
        status = self.verwerkingAutoStatus(kenteken)
        self.displayAutoStatus(status)
        geschiedenis = [
            (1000, 10, 3242, 3),
            (1000, 93, 2380, 3),
            (1902, 193, 392, 3),
            (21, 31, 3243, 324),
            (21, 312, 932, 324),
        ]
        self.displayAutoGeschiedenis(geschiedenis)


class CheckOut(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButtonEntry("Kenteken", "Uitchecken", self.uitchecken)

    def uitchecken(self):
        ''' Invoerveld uitlezen. \n 
        Returns het kenteken. '''
        text = self.getButtonEntry()
        print("Zoeken naar '%s'" % text)


class CheckIn(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButtonEntry("Kenteken", "Inchecken", self.inchecken)

    def inchecken(self):
        ''' Uitvoerveld uitlezen. \n 
        Returns het kenteken. '''
        text = self.getButtonEntry()
        print("Zoeken naar '%s'" % text)


class Invoices(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButtonEntry("Zoeken op kenteken", "Zoeken", self.zoeken)

    def zoeken(self):
        ''' Invoerveld uitlezen. \n 
        Returns het kenteken. '''
        text = self.getButtonEntry()
        print("Zoeken naar '%s'" % text)


class Registration(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createEntry("Kenteken", "License")
        self.createEntry("Naam", "Name")
        self.createEntry("Telefoonnummer", "Phone")
        self.createEntry("E-mail", "Mail")
        self.createEntry("Student-/personeelcode", "Code")
        self.createEntry("Automerk + type", "Brand")
        self.createEntry("Brandstof", "Fuel")
        self.createButton("Registreren", self.registreren)
        self.createLabel("Registratie")
        # self.createClearEntries("Leegmaken")

    def displayRegistratie(self, code):
        self.labels["Registratie"].config(text=code)

    def registreren(self):
        ''' Registratie '''
        data = self.getEntries()
        # code = connector.register(data)
        self.displayRegistratie(data)


def main():
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
