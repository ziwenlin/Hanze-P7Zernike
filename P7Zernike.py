import datetime
import time

# from connector import connector
import tkinterplus
import settings
brands = settings.brands
fueltype = settings.fueltype


class P7Entrance(tkinterplus.Notebook):
    def initialisatie(self):
        self.createTab(ParkStatus, "Parkeerplaatsen")
        self.createTab(ParkCheckIn, "Ingang A")
        self.createTab(ParkCheckIn, "Ingang B")
        self.createTab(ParkCheckOut, "Uitgang A")
        self.createTab(ParkCheckOut, "Uitgang B")


class P7Zernike(tkinterplus.Notebook):
    def initialisatie(self):
        self.createTab(SignIn, "Aanmelden")
        self.createTab(SignUp, "Registreren")

        self.createGroup("Gebruiker")
        self.createTab(UserCarStatus, "Status")
        self.createTab(UserInvoices, "Betalen")
        self.createTab(ParkStatus, "Parkeerplaatsen")
        self.createTab(SignOut, "Afmelden")

        self.createGroup("Beheerder")
        self.createTab(ParkStatus, "Parkeerplaats")
        self.createTab(ParkCheckIn, "Inchecken")
        self.createTab(ParkCheckOut, "Uitchecken")
        self.createTab(VisorParkedCarsList, "Lijst parkeerplaats")
        self.createTab(VisorParkedCarsHistory, "Geschiedenis parkeerplaats")
        self.createTab(VisorParkedCarsOverview, "Overzicht parkeerplaats")
        self.createTab(VisorUsersInvoices, "Alle facturen")
        self.createTab(VisorUnpaidInvoices, "Onbetaalde facturen")
        self.createTab(VisorParkPrices, "Prijzen")
        self.createTab(SignOut, "Afmelden")


class P7Super(tkinterplus.Notebook):
    def initialisatie(self):
        self.createTab(ParkStatus, "Parkeerplaats")
        self.createTab(ParkCheckIn, "Inchecken")
        self.createTab(ParkCheckOut, "Uitchecken")
        self.createTab(VisorParkedCarsList, "Lijst parkeerplaats")
        self.createTab(VisorParkedCarsHistory, "Geschiedenis parkeerplaats")
        self.createTab(VisorParkedCarsOverview, "Geschiedenis overzicht")
        self.createTab(VisorUsersInvoices, "Alle facturen")
        self.createTab(VisorUnpaidInvoices, "Onbetaalde facturen")
        self.createTab(VisorParkPrices, "Prijzen")

class ParkCheckOut(tkinterplus.Frame):
    def initialisatie(self):
        self.createButtonEntry("Kenteken", "Uitrijden", self.uitchecken)

    def uitchecken(self):
        ''' Invoerveld uitlezen. \n 
        Returns het kenteken. '''
        text = self.getButtonEntry()
        self.app.after(100, print, "Kenteken uit de database ophalen...")
        self.app.after(1600, print, "Kenteken gegevens afmelden...")
        self.app.after(2000, print, "Slagboom openen...")
        return text


class ParkCheckIn(tkinterplus.Frame):
    def initialisatie(self):
        self.createButtonEntry("Kenteken", "Inrijden", self.inchecken)

    def inchecken(self):
        ''' Uitvoerveld uitlezen. \n 
        Returns het kenteken. '''
        text = self.getButtonEntry()
        self.app.after(100, print, "Kenteken uit de database ophalen...")
        self.app.after(1600, print, "Kenteken gegevens goedkeuren...")
        self.app.after(2000, print, "Slagboom openen...")
        return text


class SignOut(tkinterplus.Frame):
    def uitloggen(self):
        self.master.switchGroup(None)

    def initialisatie(self):
        self.createButton("Uitloggen", self.uitloggen)

class SignIn(tkinterplus.Frame):
    def inloggen(self):
        kenteken = self.getButtonEntry()
        if kenteken == "super":
            self.master.switchGroup("Beheerder")
            return
        self.master.switchGroup("Gebruiker")

    def initialisatie(self):
        self.createButtonEntry("Kenteken", "Inloggen", self.inloggen)

class SignUp(tkinterplus.Frame):
    def initialisatie(self):
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
        self.createLabel("Registratie")
        self.createButton("Registreren", self.registreren)
        self.createEntryClear("Leegmaken")

    def displayRegistratie(self, code):
        self.labels["Registratie"].config(text=code)

    def registreren(self):
        ''' Registratie '''
        data = self.getEntries()
        # code = connector.register(data)
        self.displayRegistratie(data)


class ParkStatus(tkinterplus.Frame):
    def initialisatie(self):
        self.createLabel("ParkeerStatus")
        self.createLabel("ParkeerAantal")
        self.createButton("Bijwerken", self.updaten)
        self.updaten()
    
    def updaten(self):
        self.labels["ParkeerStatus"].config(text="Parkeerplaats is open.")
        self.labels["ParkeerAantal"].config(text="Er zijn nog 53 parkeerplekken over.")


class VisorParkedCarsList(tkinterplus.Frame):
    def initialisatie(self):
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
    def initialisatie(self):
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
    def initialisatie(self):
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
        print("Filter op %s" % filterkeuze[None])
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
    def initialisatie(self):
        self.createButton("Bijwerken", self.updaten)
        self.createTable(("Naam", "Datum", "Kenteken", "Prijs", "Korting", "Betaald"))

    def updaten(self):
        ''' Gegevens uit de database ophalen. '''
        facturen = [
            ("Pietje Pluk", "10-2-2019", "XX-213-P", 50.50, 50, "Ja")
        ]
        self.setTable(facturen)

class VisorUnpaidInvoices(tkinterplus.Frame):
    def initialisatie(self):
        self.createButton("Bijwerken", self.updaten)
        self.createTable(("Naam", "Datum", "Kenteken", "Prijs", "Korting"))

    def updaten(self):
        ''' Gegevens uit de database ophalen. '''
        facturen = [
            ("Jan Bever", "24-2-2019", "MR-213-T", 12.50, 0)
        ]
        self.setTable(facturen)


class VisorParkPrices(tkinterplus.Frame):
    def initialisatie(self):
        self.createButton("Bijwerken", self.updaten)
        self.createEntry("Prijs", "Price")
        self.createEntry("Korting", "Discount")
        self.createButton("Wijzigen", self.prijs)
        self.createLabel("Prijzen")
        self.createEntryClear("Leegmaken")

    def prijs(self):
        pass

    def updaten(self):
        pass

class VisorUserDiscount(tkinterplus.Frame):
    def initialisatie(self):
        self.createButton("Bijwerken", self.updaten)
        self.createEntry("Student-/personeelcode", "Code")
        self.createEntry("Korting", "iDiscount")
        self.createButton("Wijzigen", self.korting)
        self.createEntryClear("Leegmaken")

    def korting(self):
        pass

    def updaten(self):
        pass


class UserCarStatus(tkinterplus.Frame):
    def initialisatie(self):
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
    def initialisatie(self):
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
