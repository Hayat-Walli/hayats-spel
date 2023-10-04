# Importerar slumpmässighetsmodulen
import random

# Definierar tecken
STEN = 1
SAX = 2
PASE = 3

# Definierar en funktion för att spela en omgång
def spela_omgang():
    # Begär spelarens val
    val = input("Sten, sax eller påse? ")

    # Genererar datorns val
    dator_val = random.choice([STEN, SAX, PÅSE])

    # Beräknar resultatet
    if val == dator_val:
        print("Oavgjort!")
    elif val == STEN and dator_val == SAX:
        print("Du vann!")
    elif val == SAX and dator_val == PÅSE:
        print("Du vann!")
    elif val == PÅSE and dator_val == STEN:
        print("Du vann!")
    else:
        print("Datorn vann!")

# Startar spelet
while True:
    spela_omgang()
    val = input("Vill du spela igen? (j/n) ")
    if val == "n":
        break
