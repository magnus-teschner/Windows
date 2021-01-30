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
    if spieler %2:
    # horizontal
        for i in range(3):
            counter = 0
            for e in range(3):
                if spielfeld[i][e] == "X":
                    counter += 1
            if counter == 3:
                ausgabe_feld(spielfeld)
                print("Spieler 1 hat gewonnen")
                return 0
                break

        e = 0
        counter = 0
        for i in range(3):
            if spielfeld[i][e] == "X":
                counter += 1
            e += 1
            if counter == 3:
                ausgabe_feld(spielfeld)
                print("Spieler 1 hat gewonnen")
                return 0
                break

        e = 0
        counter = 0
        for i in range(2, -1, -1):
            if spielfeld[i][e] == "X":
                counter += 1
            e += 1
            if counter == 3:
                ausgabe_feld(spielfeld)
                print("Spieler 1 hat gewonnen")
                return 0
                break
        if counter != 3 and spieler == 9:
            print("Unentschieden")


    else:
        # horizontal
        for i in range(3):
            counter = 0
            for e in range(3):
                if spielfeld[i][e] == "O":
                    counter += 1
            if counter == 3:
                ausgabe_feld(spielfeld)
                print("Spieler 2 hat gewonnen")
                return 0
                break

        e = 0
        counter = 0
        for i in range(3):
            if spielfeld[i][e] == "O":
                counter += 1
            e += 1
            if counter == 3:
                ausgabe_feld(spielfeld)
                print("Spieler 2 hat gewonnen")
                return 0
                break

        e = 0
        counter = 0
        for i in range(2, -1, -1):
            if spielfeld[i][e] == "O":
                counter += 1
            e += 1
            if counter == 3:
                ausgabe_feld(spielfeld)
                print("Spieler 2 hat gewonnen")
                return 0
                break

        if counter != 3 and spieler == 9:
            print("Unentschieden")




spieler = 0
while abruch != 0:
    spieler += 1
    liste = conversion(spieler)
    eingabe(spielfeld, liste, spieler)
    abruch = abruchbedingung1(spielfeld, spieler)

