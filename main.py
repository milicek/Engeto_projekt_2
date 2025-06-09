"""
projekt_2.py: první projekt do Engeto Online Python Akademie

author: Michal Uryč
email: michal.uryc@seznam.cz
"""
#Bull & Cows - hra postavená na hádání 4 ciferného čísla

"""_program pozdraví užitele a vypíše úvodní text  (viz. níže v ukázkách),
    program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)hráč hádá číslo. 
    Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, 
    pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky,program vyhodnotí tip uživatele,
    program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), 
    příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). 
    Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. 
    Tedy 1 bull a 2 bulls (stejně pro cow/cows),zápis organizovaný do krátkých a přehledných funkcí.
    Tvoje řešení nahraješ do souboru main.py (pokud pojmenuješ soubor jinak, nebude uznaný),
    repozitář bude obsahovat jedinný .py soubor s výstupem (pokud jej třeba rozdělíš jako main_1.py a main_2.py, nebude uznaný).
    každý projekt má svůj vlastní, oddělený repozitář (zvlášť repozitář pro 1. projekt, zvlášť repozitář pro další projekt, ...).
    
    Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------

Příklad hry s číslem 2017
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
>>> 1234
0 bulls, 2 cows
-----------------------------------------------
>>> 6147
1 bull, 1 cow
-----------------------------------------------
>>> 2417
3 bulls, 0 cows
-----------------------------------------------
>>> 2017
Correct, you've guessed the right number
in 4 guesses!
-----------------------------------------------
That's amazing!

Program toho může umět víc. Můžeš přidat například:
počítání času, za jak dlouho uživatel uhádne tajné číslo
uchovávat statistiky počtu odhadů jednotlivých her
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



#hlavička
print("Hi there !")
print(oddelovac)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(oddelovac)
print("Enter a number:")
print(oddelovac)

vzor = vytvor_ctyrmistne_cislo()
hodnoceni = {"bull": 0, "pocitadlo": 0}
while hodnoceni["bull"] != 4:
    vstup = input(">>> ")
    if zkontroluj_vstup(vstup):
        hodnoceni = vyhodnot_vstup(vstup, vzor)
        hodnoceni["pocitadlo"] += 1
        print(hodnoceni["bull"], " Bulls,", hodnoceni["cow"], "Cows")
        print(oddelovac)
print("Correct, you've guessed the right number in ", hodnoceni["pocitadlo"],  "guesses!")
print(oddelovac)
print("That's amazing!")
    


