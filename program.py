import datetime

def main():
    logo()
    jahr, monat, tag = abfrage()
    datum = geburtsdatum(jahr, monat, tag)
    restlichetage(datum)



def logo():
    print("-----------------------------------------")
    print("               GEBURTSTAG    ")
    print("-----------------------------------------")


def abfrage():
    print("Wann wurdest du geboren? ")
    jahr = int(input("In welchem Jahr [JJJJ]: "))
    monat = int(input("In welchem Monat [MM]: "))
    tag = int(input("An welchem Tag [TT]: "))
    return jahr, monat, tag


def geburtsdatum(jahr, monat, tag):
    datum = datetime.date(jahr, monat, tag)
    print(f"Du wurdest also am {datum} geboren.")
    return datum


def restlichetage(datum):
    heute = datetime.date.today()
    delta = heute - datum
    print(f"Du lebst seid {delta.days} Tagen!")
# WIR MÜSSEN DIE DIFFERENZ VON DEN TAGEN OHNE JAHR HABEN

main()