def main():
    logo()
    abfrage()


def logo():
    print("-----------------------------------------")
    print("               GEBURTSTAG    ")
    print("-----------------------------------------")


def abfrage():
    print("Wann wurdest du geboren? ")
    jahr = input("In welchem Jahr [JJJJ]: ")
    monat = input("In welchem Monat [MM]: ")
    tag = input("An welchem Tag [TT]: ")

main()