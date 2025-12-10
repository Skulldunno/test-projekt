import random
from datetime import *


class Kunde:
    Kundenliste = {}
    Kundennummern = []

    def __init__(self, nachname = "NA", vorname = "NA", geburtsdatum = "NA",  bestellung_liste = None, kundennummer = None):
        if None == nachname or nachname == "NA":
            nachname = input("Nachname :\n")
            self.nachname = nachname
        else:
            self.nachname = nachname
        if None == vorname or vorname == "NA":
            vorname = input("Vorname :\n")
            self.vorname = vorname
        else:
            self.vorname = vorname
        if None ==geburtsdatum or geburtsdatum == "NA":
            while True:
                geburtsdatum = input("Geburtsdatum : YYYYMMDD\n")
                try:
                    self.geburtsdatum = datetime.strptime(geburtsdatum, "%Y%m%d")
                    break
                except ValueError:
                    print(f"Date {geburtsdatum} not valid (Falsches Format)")
        else:
            while True:
                try:
                    self.geburtsdatum = geburtsdatum
                    break
                except ValueError:
                    print(f"Date: {geburtsdatum} not valid (Falsches Format)")
                    geburtsdatum = input("Geburtsdatum : YYYYMMDD\n")
        if bestellung_liste is None:
            self.bestellung_liste = {}
        else:
            self.bestellung_liste = bestellung_liste
        if None == kundennummer:
            x = random.randint(1, 100) + random.randint(1000, 9899)
            while x in Kunde.Kundennummern:
                x = random.randint(1, 100) + random.randint(1000, 9899)
            self.__kundennummer = x
            Kunde.Kundennummern.append(x)
        else:
            self.__kundennummer = kundennummer
        Kunde.Kundenliste[self.__kundennummer] = self

    def get_kundennummer(self):
        return self.__kundennummer

    def add_bestellung(self, bestellung):
        self.bestellung_liste[bestellung] = Bestellung.Bestellungsliste[bestellung]

    def get_preis(self):
        for bestellung in self.bestellung_liste :
            print(bestellung.rechnungsbetrag)

    def kunden_upgrade(self):
        nachname = self.nachname
        vorname = self.vorname
        geburtsdatum = self.geburtsdatum
        bestellung_liste = self.bestellung_liste
        kundennummer = self.__kundennummer
        Kunde.Kundennummern.remove(self.__kundennummer)
        Kunde.Kundenliste.pop(self.__kundennummer)
        Premiumkunde(nachname,vorname,str(geburtsdatum),bestellung_liste,kundennummer)
        Premiumkunde.kundenliste[self.__kundennummer] = self
        Kunde.Kundenliste.pop(self.__kundennummer)


class Premiumkunde(Kunde):
    kundenliste = {}

    def get_preis(self):
        for bestellung in self.bestellung_liste :
            print(bestellung.rechnungsbetrag * 0.95)


class Bestellung:
    Bestellungsliste = {}
    Bestellungsnummern = []

    def __init__(self, rechnungsbetrag, artikel_liste = None):
        if len(Bestellung.Bestellungsnummern) not in Bestellung.Bestellungsnummern :
            self.__bestellnummer = len(Bestellung.Bestellungsnummern)
        else:
            for neue_nummer in range(len(Bestellung.Bestellungsnummern)):
                print(neue_nummer)
                if neue_nummer not in Bestellung.Bestellungsnummern:
                    self.__bestellnummer = neue_nummer
        if artikel_liste is None:
            self.artikel_liste = []
        self._bestelldatum = date.today()
        self.rechnungsbetrag = rechnungsbetrag
        Bestellung.Bestellungsliste[self.__bestellnummer] = self
        Bestellung.Bestellungsnummern.append(self.__bestellnummer)

    def get_bestellnummer(self):
        return self.__bestellnummer

    def get_date(self):
        datum = str(self._bestelldatum)
        return datum


class UI:

    def __init__(self):
        self.run()

    def run(self):
        print(f"Starte {self}")
        while True:
            auswahl = input(
"""
1 um einen Neuen Kunden hinzuzufügen
2 um Kunden anzuzeigen
3 um einen Kunden zu entfern
4 um eine neue Bestellung zu erstellen
5 um Bestellungen anzuzeigen
6 um Bestellungen Kunden zuzuweisen
7 um Kunden auf Premiumkunden zu befördern
8 QUIT
""")
            if auswahl == "1":
                neuer_kunde()
            elif auswahl == "2":
                kunden_auflisten()
            elif auswahl == "3":
                kunde_entfernen()
            elif auswahl == "4":
                neue_bestellung()
            elif auswahl == "5":
                bestellungen_auflisten()
            elif auswahl == "6":
                bestellung_zuweisen()
            elif auswahl == "7":
                kunde_premium()
            elif auswahl == "8":
                break



def neuer_kunde():
    Kunde()


def kunden_auflisten():
    print("Premiumkunden")
    print("_"*32)
    for Kunden in Premiumkunde.kundenliste:
        x = Premiumkunde.kundenliste[Kunden]
        print(f"{x.nachname:<10}|{x.get_kundennummer():>10}")
        for bestellung in x.bestellung_liste:
            print(
                f"{Bestellung.Bestellungsliste[bestellung].get_bestellnummer():<10}|{Bestellung.Bestellungsliste[bestellung].rechnungsbetrag:>10}")
    print("_"*32)
    print("Kunden")
    print("_"*32)
    for Kunden in Kunde.Kundenliste:
        x = Kunde.Kundenliste[Kunden]
        print(f"{x.nachname:<10}|{x.get_kundennummer():>10}")
        for bestellung in x.bestellung_liste :
            print(f"{Bestellung.Bestellungsliste[bestellung].get_bestellnummer():<10}|{Bestellung.Bestellungsliste[bestellung].rechnungsbetrag:>10}")


def kunde_entfernen():
    kunde = get_kunde()
    if kunde is False:
        return print("Tschüss")
    if double_check():
        Kunde.Kundennummern.remove(kunde)
        Kunde.Kundenliste.pop(kunde)
        return print("Done, Boss")
    else:
        return print("OK zurück zum Hauptmenü")


def neue_bestellung():
    manuell_preis = input("Preis")
    Bestellung(manuell_preis)


def bestellungen_auflisten():
    for bestellung in Bestellung.Bestellungsliste:
        x = Bestellung.Bestellungsliste[bestellung]
        print(f"{x.get_date():<10}|{x.get_bestellnummer():^15}|{x.rechnungsbetrag:>10}")
        for kunde in Kunde.Kundenliste:
            if bestellung in Kunde.Kundenliste[kunde].bestellung_liste:
                print(f"{Kunde.Kundenliste[kunde].get_kundennummer():<10}|{x.get_bestellnummer():^15}")


def get_kunde():
    while True:
        kunden_auflisten()
        kunde = input("Welcher Kunde? (Kundennummer)\n Zurück mit 0\n")
        try:
            kunde = int(kunde)
        except ValueError:
            pass
        if kunde in Premiumkunde.kundenliste:
            print(f"{Premiumkunde.kundenliste[kunde].nachname:<10}|{Premiumkunde.kundenliste[kunde].get_kundennummer():>10}")
            return kunde
        elif kunde in Kunde.Kundennummern:
            print(f"{Kunde.Kundenliste[kunde].nachname:<10}|{Kunde.Kundenliste[kunde].get_kundennummer():>10}")
            return kunde
        elif kunde == 0:
            return False
        else:
            print("Diesen Kunden gibt es nicht? (Falsche Kundennummer)")


def get_bestellung():
    while True:
        bestellungen_auflisten()
        bestellung = input("Welcher Bestellung? (Bestellungsnummer)\n Zurück mit X\n")
        try:
            bestellung = int(bestellung)
        except ValueError:
            pass
        if bestellung in Bestellung.Bestellungsnummern:
            print(f"{Bestellung.Bestellungsliste[bestellung].rechnungsbetrag:<10}|{Bestellung.Bestellungsliste[bestellung].get_bestellnummer():>10}")
            return bestellung
        elif bestellung == "X" or bestellung == "x":
            return False
        else:
            print("Diese Bestellung gibt es nicht? (Falsche Bestellungsnummer)")


def bestellung_zuweisen():
    kunde = get_kunde()
    if kunde is False:
        return print("Abgebrochen")
    bestellung = get_bestellung()
    if bestellung is False:
        return print("Abgebrochen")
    if kunde in Kunde.Kundenliste:
        Kunde.Kundenliste[kunde].add_bestellung(bestellung)
        return print("Done")
    elif kunde in Premiumkunde.kundenliste:
        Premiumkunde.kundenliste[kunde].add_bestellung(bestellung)
        return print("Done")
    else:
        return print("Gooner")


def kunde_premium():
    kunde = get_kunde()
    if kunde is False:
        return print("Abgebrochen")
    if double_check():
        Kunde.Kundenliste[kunde].kunden_upgrade()
        return print("Done")
    else:
        return print("Ok zurück zum Hauptmenü")


def double_check():
    sure = input("Sind Sie sich sicher? (Y/N)\n")
    if sure == "Y" or sure == "y":
        return True
    else:
        return False

if __name__ == "__main__":
    UI()

unwichtig = True

wichtig = True