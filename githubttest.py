spielfeld = [[1,2,3],
             [4,5,6],
             [7,8,9]]

for i in range(3):
    print(spielfeld[i])

print("")
print("Es beginnt Spieler 1: \n")



def conversion(eingabe):
    if eingabe == 1:
        row = 0
        column = 0
    elif eingabe == 2:
        row = 0
        column == 1
    elif eingabe == 3:
        row = 0
        column == 2
    elif eingabe == 4:
        row = 1
        column == 0
    elif eingabe == 5:
        row = 1
        column == 2
    elif eingabe == 6:
        row = 1
        column == 1
    elif eingabe == 7:
        row = 2
        column == 0
    elif eingabe == 8:
        row = 2
        column == 1
    elif eingabe == 9:
        row = 2
        column == 2

    return [row, column]


def eingabe(i, liste):
    #wenn True -> Spieler 1 ist am Zug
    #bei 1 beginnend
    if i % 2:
        spielfeld[liste[0]][liste[1]] = "X"
    else:
        spielfeld[liste[0]][liste[1]] = "O"


