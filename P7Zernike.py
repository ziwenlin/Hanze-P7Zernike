import datetime
import time

# from connector import connector
import tkinterplus
import settings
brands = settings.brands
fueltype = settings.fueltype


class P7Entrance(tkinterplus.Notebook):
    def __init__(self, master):
        super().__init__(master)
        self.createTab(ParkStatus, "Parkeerplaatsen")
        self.createTab(ParkCheckIn, "Ingang A")
        self.createTab(ParkCheckIn, "Ingang B")
        self.createTab(ParkCheckOut, "Uitgang A")
        self.createTab(ParkCheckOut, "Uitgang B")


class P7Zernike(tkinterplus.Notebook):
    def __init__(self, master):
        super().__init__(master)
        user = "Gebruiker"
        visor = "Beheerder"
        self.createTab(SignIn, "Aanmelden")
        self.createTab(SignUp, "Registreren")
        self.createTab(UserCarStatus, "Status", user)
        self.createTab(UserInvoices, "Betalen", user)
        self.createTab(ParkStatus, "Parkeerplaatsen", user)
        self.createTab(SignOut, "Afmelden", user)
        self.createTab(ParkStatus, "Parkeerplaats", visor)
        self.createTab(ParkCheckIn, "Inchecken", visor)
        self.createTab(ParkCheckOut, "Uitchecken", visor)
        self.createTab(VisorParkedCarsList, "Lijst parkeerplaats", visor)
        self.createTab(VisorParkedCarsHistory, "Geschiedenis parkeerplaats", visor)
        self.createTab(VisorParkedCarsOverview, "Overzicht parkeerplaats", visor)
        self.createTab(VisorUsersInvoices, "Alle facturen", visor)
        self.createTab(VisorUnpaidInvoices, "Onbetaalde facturen", visor)
        self.createTab(VisorParkPrices, "Prijzen", visor)
        self.createTab(SignOut, "Afmelden", visor)


class P7Super(tkinterplus.Notebook):
    def __init__(self, master):
        super().__init__(master)
        self.createTab(ParkStatus, "Parkeerplaats")
        self.createTab(ParkCheckIn, "Inchecken")
        self.createTab(ParkCheckOut, "Uitchecken")
        self.createTab(VisorParkedCarsList, "Lijst parkeerplaats")
        self.createTab(VisorParkedCarsHistory, "Geschiedenis parkeerplaats")
        self.createTab(VisorParkedCarsOverview, "Overzicht parkeerplaats")
        self.createTab(VisorUsersInvoices, "Alle facturen")
        self.createTab(VisorUnpaidInvoices, "Onbetaalde facturen")
        self.createTab(VisorParkPrices, "Prijzen")



class ParkCheckOut(tkinterplus.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButtonEntry("Kenteken", "Uitrijden", self.uitchecken)

    def uitchecken(self):
        ''' Invoerveld uitlezen. \n 
        Returns het kenteken. '''
        text = self.getButtonEntry()
        self.after(100, print, "Kenteken uit de database ophalen...")
        self.after(1600, print, "Kenteken gegevens afmelden...")
        self.after(2000, print, "Slagboom openen...")
        return text


class ParkCheckIn(tkinterplus.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButtonEntry("Kenteken", "Inrijden", self.inchecken)

    def inchecken(self):
        ''' Uitvoerveld uitlezen. \n 
        Returns het kenteken. '''
        text = self.getButtonEntry()
        self.after(100, print, "Kenteken uit de database ophalen...")
        self.after(1600, print, "Kenteken gegevens goedkeuren...")
        self.after(2000, print, "Slagboom openen...")
        return text


class SignOut(tkinterplus.Frame):
    def uitloggen(self):
        self.master.switchGroup(None)

    def __init__(self, master):
        super().__init__(master)
        self.createButton("Uitloggen", self.uitloggen)

class SignIn(tkinterplus.Frame):
    def inloggen(self):
        kenteken = self.getButtonEntry()
        if kenteken == "super":
            self.master.switchGroup("Beheerder")
            return
        self.master.switchGroup("Gebruiker")

    def __init__(self, master):
        super().__init__(master)
        self.createButtonEntry("Kenteken", "Inloggen", self.inloggen)

class SignUp(tkinterplus.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createEntry("Kenteken", "License")
        self.createEntry("Voornaam", "Firstname")
        self.createEntry("Tussenvoegsel", "Prefix")
        self.createEntry("Achternaam", "Lastname")
        self.createEntry("Telefoonnummer", "Phone")
        self.createEntry("E-mail", "Mail")
        self.createEntry("Student-/personeelcode", "Code")
        self.createEntryChoice("Rol", ["Student", "Werknemer"], "Role")
        self.createEntryChoice("Automerk", brands, "Brand", "Volkswagen")
        self.createEntry("Automodel", "Model")
        self.createEntryChoice("Brandstof", fueltype, "Fuel", "Benzine")
        self.createButton("Registreren", self.registreren)
        self.createLabel("Registratie")
        self.createEntryClear("Leegmaken")

    def displayRegistratie(self, code):
        self.labels["Registratie"].config(text=code)

    def registreren(self):
        ''' Registratie '''
        data = self.getEntries()
        # code = connector.register(data)
        self.displayRegistratie(data)


class ParkStatus(tkinterplus.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createLabel("ParkeerStatus")
        self.createLabel("ParkeerAantal")
        self.createButton("Bijwerken", self.updaten)
        self.updaten()
    
    def updaten(self):
        self.labels["ParkeerStatus"].config(text="Parkeerplaats is open.")
        self.labels["ParkeerAantal"].config(text="Er zijn nog 53 parkeerplekken over.")


class VisorParkedCarsList(tkinterplus.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButton("Bijwerken", self.updaten)
        self.createTable(("Kenteken", "Merk", "Model", "Brandstof", "Tijd"))

    def updaten(self):
        """ Functie van de knop. \n
        Invoerveld uitlezen en daarmee in de database kijken. 
        Data van de database wordt gelezen en verwerkt. 
        De geschiedenis wordt in de tabel weergeven en
        de eventuele huidige parkeersessie wordt 
        in de informatiepaneel weergeven. """
        geschiedenis = [
            ("KL-432-P", "Renault", "Clio", "Benzine", "2:40"),
            ("HZ-619-R", "BMW", "218I Gran Tourer", "Diesel", "1:32"),
        ]
        self.setTable(geschiedenis)


class VisorParkedCarsHistory(tkinterplus.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButton("Bijwerken", self.updaten)
        self.createLabel("Totaal")
        self.createTable(("Kenteken", "Merk", "Model", "Brandstof", "Inrijden", "Uitrijden", "Tijd"))

    def updaten(self):
        """ Functie van de knop. \n
        Invoerveld uitlezen en daarmee in de database kijken. 
        Data van de database wordt gelezen en verwerkt. 
        De geschiedenis wordt in de tabel weergeven en
        de eventuele huidige parkeersessie wordt 
        in de informatiepaneel weergeven. """
        geschiedenis = [
            ("KL-432-P", "Renault", "Clio", "Benzine", "12-5-2019 7:55", "12-5-2019 16:21", "8:26"),
            ("HZ-619-R", "BMW", "218I Gran Tourer", "Diesel", "12-5-2019 12:32", "12-5-2019 15:12", "2:40"),
        ]
        self.setTable(geschiedenis)


class VisorParkedCarsOverview(tkinterplus.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButton("Bijwerken", self.updaten)
        self.createEntryChoice("Filter op per: ", ["Uur", "Dag", "Week", "Maand", "Jaar"])
        self.createTable(("Aantal", "Interval"))

    def updaten(self):
        """ Functie van de knop. \n
        Invoerveld uitlezen en daarmee in de database kijken. 
        Data van de database wordt gelezen en verwerkt. 
        De geschiedenis wordt in de tabel weergeven en
        de eventuele huidige parkeersessie wordt 
        in de informatiepaneel weergeven. """
        filterkeuze = self.getEntries()
        print("Filter op %s" % filterkeuze)
        geschiedenis = [
            (2, "00:00"),
            (2, "01:00"),
            (2, "02:00"),
            (2, "03:00"),
            (2, "04:00"),
            (2, "05:00"),
            (7, "06:00"),
            (31, "07:00"),
            (63, "08:00"),
            (97, "09:00"),
            (114, "10:00"),
            (132, "11:00"),
            (141, "12:00"),
            (113, "13:00"),
            (96, "14:00"),
            (85, "15:00"),
            (38, "16:00"),
            (16, "17:00"),
            (12, "18:00"),
            (4, "19:00"),
            (4, "20:00"),
            (3, "21:00"),
            (1, "22:00"),
            (0, "23:00"),
            (0, "24:00"),
        ]
        self.setTable(geschiedenis)

class VisorUsersInvoices(tkinterplus.Frame):
    pass


class VisorUnpaidInvoices(tkinterplus.Frame):
    pass


class VisorParkPrices(tkinterplus.Frame):
    pass


class UserCarStatus(tkinterplus.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButton("Bijwerken", self.updaten)
        self.createLabel("AutoStatus")
        self.createTable(("Datum", "Transactie"))

    def displayAutoStatus(self, text):
        ''' Weergeeft de status van het parkeren in de informatiepaneel. '''
        if text is not None:
            text = "Uw huidige parkeertijd is %s uur." % text
        else:
            text = "De auto is niet geparkeerd."
        self.labels["AutoStatus"].config(text=text)

    def verwerkingAutoStatus(self, opdracht):
        ''' TODO Verbinding maken met de database. '''
        random = time.time() * 100 % 10
        if random < 9:
            if random < 1:
                return datetime.time(hour=0, minute=int(60*random))
            return datetime.time(hour=int(random), minute=int(6*random))
        return None

    def updaten(self):
        """ Functie van de knop. \n
        Invoerveld uitlezen en daarmee in de database kijken. 
        Data van de database wordt gelezen en verwerkt. 
        De geschiedenis wordt in de tabel weergeven en
        de eventuele huidige parkeersessie wordt 
        in de informatiepaneel weergeven. """
        status = self.verwerkingAutoStatus(None)
        geschiedenis = [
            ("10-1-2018 10:12", "Inrijden"),
            ("10-1-2018 16:43", "Uitrijden"),
        ]
        self.displayAutoStatus(status)
        self.setTable(geschiedenis)


class UserInvoices(tkinterplus.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createButton("Ophalen", self.updaten)
        self.createLabel("Gebruiker")
        self.createTable(("Inrijden", "Uitrijden", "Parkeertijd", "Tarief", "Prijs", "Korting"))

    def displayGegevens(self, text):
        ''' Weergeeft de status van het parkeren in de informatiepaneel. '''
        if text is not None:
            text = "Naam: %s" % text
        else:
            text = "De auto is niet geparkeerd."
        self.labels["Gebruiker"].config(text=text)

    def updaten(self):
        ''' Gegevens uit de database ophalen. '''
        geschiedenis = [
            ("10-2-2019 15:10", "10-2-2019 19:15", "4:05", 0.50, 2.02, 50.00)
        ]
        self.displayGegevens("Gebruiker")
        self.setTable(geschiedenis)


def main():
    app = tkinterplus.Application("P7@Zernike")
    app.createOverlay(P7Zernike)
    sup = tkinterplus.Window("P7@Supervisor")
    sup.createOverlay(P7Super)
    cam = tkinterplus.Window("P7@Entrance")
    cam.createOverlay(P7Entrance)
    app.mainloop()


if __name__ == "__main__":
    main()
