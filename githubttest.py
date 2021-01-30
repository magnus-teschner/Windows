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

spieler = 0

def check_stand(counter):
    if counter == 3:
        return 0



def abruch(spielfeld, spieler):
    counter = 0
    # dann ablauf für spieler 1
    if spieler % 2:
        # horizontalen linien abgehandelt:
        for i in range(3):
            for e in range(2):
                if spielfeld[i][e] == spielfeld[i][e +1]:
                    counter += 1
        check_stand(counter)
        counter = 0
        e = 0
        #vertikale  Linien oben unten abgehandelt
        for i  in range(2):
            if spielfeld[i][e] == spielfeld[i+1][e+1]:
                counter += 1
            e += 1
        check_stand(counter)
        counter = 0
        e = 2
        #vertikale Linien unten oben abgehandelt
        for i in range(2, 0, -1):
            if spielfeld[i][e] == spielfeld[i-1][e-1]:
                counter += 1
            e -= 1
        check_stand(counter)
        counter = 0


while abruch != 0:
    spieler += 1
    liste = conversion(spieler)
    eingabe(spielfeld, liste, spieler)
    abruch = abruch(spielfeld, spieler)

