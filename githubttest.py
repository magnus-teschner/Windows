spielfeld = [[None,None,None],
             [None,None,None],
             [None,None,None]]


print("")



def ausgabe_feld(spielfeld):
    for i in range(3):
        print(spielfeld[i])

abruch = 1
def conversion(spieler):
    ausgabe_feld(spielfeld)
    print("")
    if spieler %2:
        eingabe = int(input("Wohin wollen Sie setzen Spieler 1: \n"))
    else:
        eingabe = int(input("Wohin wollen Sie setzen Spieler 2: \n"))
    print("")
    if eingabe == 1:
        row = 0
        column = 0
    elif eingabe == 2:
        row = 0
        column = 1
    elif eingabe == 3:
        row = 0
        column = 2
    elif eingabe == 4:
        row = 1
        column = 0
    elif eingabe == 5:
        row = 1
        column = 1
    elif eingabe == 6:
        row = 1
        column = 2
    elif eingabe == 7:
        row = 2
        column = 0
    elif eingabe == 8:
        row = 2
        column = 1
    elif eingabe == 9:
        row = 2
        column = 2
    liste = [row, column]
    return liste

def eingabe(spielfeld, liste, spieler):
    if spieler %2:
        spielfeld[liste[0]][liste[1]] = "X"
    else:
        spielfeld[liste[0]][liste[1]] = "0"

def abbruch(spielfeld):
    #checken von welchem drei
    #abruchbedingung verändern durch global
    #rückgabe welcher spieler
spieler = 0


while abruch != 0:
    spieler += 1
    liste = conversion(spieler)
    eingabe(spielfeld, liste, spieler)
    abruch(spielfeld)

