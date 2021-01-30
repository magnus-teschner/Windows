spielfeld = [[ 111 , 222 , 333 ],
             [ 444 , 555 , 666 ],
             [ 777 , 888 , 999 ]]
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
        spielfeld[liste[0]][liste[1]] = "O"


def abruchbedingung1(spielfeld, spieler):
    gewinn = 0
    if spieler %2:
        #spieler1
        checker = "X"
        punkte = 0
        a = horizontal(spielfeld, checker)
        b = vertikal(spielfeld, checker)
        c = quer1(spielfeld, checker)
        d = quer2(spielfeld, checker)



        if a == 1 or b == 1 or c == 1 or d == 1:
            ausgabe_feld(spielfeld)
            print("Spieler 1 hat gewonnen!")
            gewinn = 1
            return 0
    else:
        # spieler2
        checker = "O"
        punkte = 0
        a = horizontal(spielfeld, checker)
        b = vertikal(spielfeld, checker)
        c = quer1(spielfeld, checker)
        d = quer2(spielfeld, checker)

        if a == 1 or b == 1 or c == 1 or d == 1:
            ausgabe_feld(spielfeld)
            print("Spieler 2 hat gewonnen!")
            gewinn = 1
            return 0

    if gewinn == 0 and spieler == 9:
        ausgabe_feld(spielfeld)
        print("Unentschieden")
        return 0

def horizontal(spielfeld, checker):
    for i in range(3):
        counter = 0
        for e in range(3):
            if spielfeld[i][e] == checker:
                counter += 1
            if counter == 3:
                return 1

def vertikal(spielfeld, checker):
    for i in range(3):
        counter = 0
        for e in range(3):
            if spielfeld[e][i] == checker:
                counter += 1
            if counter == 3:
                return 1

#links oben rechs unten
def quer1(spielfeld, checker):
    counter = 0
    e = 0
    for i in range(3):
        if spielfeld[i][e] == checker:
            counter += 1
        e += 1
        if counter == 3:
            return 1

#links unten rechts oben
def quer2(spielfeld, checker):
    counter = 0
    e = 2
    for i in range(3):
        if spielfeld[e][i] == checker:
            counter += 1
        e -= 1
        if counter == 3:
            return 1

spieler = 0
while abruch != 0:
    spieler += 1
    liste = conversion(spieler)
    eingabe(spielfeld, liste, spieler)
    abruch = abruchbedingung1(spielfeld, spieler)

