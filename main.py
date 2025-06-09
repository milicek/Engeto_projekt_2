"""
projekt_2.py: první projekt do Engeto Online Python Akademie

author: Michal Uryč
email: michal.uryc@seznam.cz
"""

#import knihoven
from random import randint


#funkce
def vytvor_ctyrmistne_cislo() -> str:
    """
    Vytvoří náhodné číslo, které bude mít 4 číslice.
    Číslo nebude začínat nulou a číslice se nebudou opakovat.

    návrat: str
    """
    vyber_cislic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    prvni_cislice = randint(1,9)
    cislo = vyber_cislic[prvni_cislice]
    del vyber_cislic[prvni_cislice]
    for c in range(3):
        dalsi_cislice = randint(0,(len(vyber_cislic)-1))
        cislo = str(cislo) + str(vyber_cislic[dalsi_cislice])
        del vyber_cislic[dalsi_cislice]
    return str(cislo)

def zkontroluj_vstup(vstup_uzivatele: str) -> bool:
    """
    Zkontroluj jestli vstup obsahuje čtyřmístné číslo, 
    jestli nezačíná nulou, nebo jestli neobsahuje stejné číslice,
    pokud ne, vypiš komentář

    návrat: bool
    """
    if not vstup_uzivatele.isnumeric():
        print("Musíš zadat celé číslo")
        vystup = False 
    elif len(vstup_uzivatele) > 4 or len(vstup_uzivatele) < 4:
        print("číslo není čtyřciferné")
        vystup = False
    elif vstup_uzivatele[0] == "0":
        print("Číslo nesmí začínat nulou")
        vystup = False
    else:
        vystup = True
        for cislice in vstup_uzivatele:
            if vstup_uzivatele.count(cislice) > 1:
                print("číslo nesmí obsahovat stejné číslice")
                vystup = False
                break        
            else:
                vystup = True 
    
    return vystup

    
def vyhodnot_vstup(vstup: str, vzor: str) -> dict:  
    """
    Zkontroluj jestli vstup obsahuje cislo jako vzor index po indexu,
    pokud ano ale je na jiné pozici přičti jednu cow,
    pokud je na stejné pozici přičti jeden bull

    návrat: dict
    """
    vystup = {"bull": 0,
              "cow": 0}
    for index, cislice in enumerate(vstup):
        if cislice in vzor:
            if cislice == vzor[index]:
                vystup["bull"] += 1
            else:
                vystup["cow"] += 1
    return vystup


#pomocné proměnné
oddelovac = 30 * "-"


def jednotne_mnozne(slovnik: dict) -> str:
    """
    Zkontroluj jestli hodnoty jednotlivých klíčů slovníku
    obsahují větší hodnotu než 1 a pokud ano přidají
    za klíč písmeno "s" jako množné číslo
    Nakonec vypíší všechny vyhodnocené klíča a za ně hodnoty
    oddělené čárkou na jeden řádek jako string

    návrat: str
    """
    
    vystup = ""
    for text, hodnota in slovnik.items():
        if hodnota <= 1:
            pomocne = str(hodnota) + " " + text
        else:
            pomocne = str(hodnota) + " " + text + "s"
        if vystup == "":
            vystup = pomocne
        else:        
            vystup = vystup + ", " + pomocne
    return vystup



#hlavička
print("Hi there !")
print(oddelovac)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(oddelovac)
print("Enter a number:")
print(oddelovac)

vzor = vytvor_ctyrmistne_cislo()
hodnoceni = {"bull": 0}
pocitadlo = 0
while hodnoceni["bull"] != 4:
    vstup = input(">>> ")
    if zkontroluj_vstup(vstup):
        hodnoceni = vyhodnot_vstup(vstup, vzor)
        pocitadlo += 1
#        print(hodnoceni["bull"], " Bulls,", hodnoceni["cow"], "Cows")
        print(jednotne_mnozne(hodnoceni))
        print(oddelovac)
print("Correct, you've guessed the right number in ", pocitadlo,  "guesses!")
print(oddelovac)
print("That's amazing!")
    


