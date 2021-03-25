from os import system

def tableroVacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

def ingresarSecuencia(secuencia):
    if len(secuencia) % 2 == 0:
        turno = "Jugador 1 debe ingresar una columna: "
    else:
        turno = "Jugador 2 debe ingresar una columna: "
    columna = int(input(turno))
    secuencia.append(columna)

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila-1][columna-1] == 0:
            tablero[fila-1][columna-1] = ficha
            return

def completarTableroEnOrden(secuencia, tablero):
    l = len(secuencia)
    if l % 2 == 0:
        ficha = 2
    else:
        ficha = 1
    columna = secuencia[l-1]
    soltarFichaEnColumna(ficha, columna, tablero)


def dibujarTablero(tablero):
    for i in range(6):
        for j in range(7):
            print("{0} ".format(tablero[i][j]), end = "")
        print("")

secuencia = []
tablero = tableroVacio()
system("cls")
print("4 EN LINEA")
system("pause")
system("cls")
while len(secuencia) < (7*6):
    dibujarTablero(tablero)
    print("\n\n")
    ingresarSecuencia(secuencia)
    system("cls")
    completarTableroEnOrden(secuencia, tablero)
    print("")
    system("cls")
dibujarTablero(tablero)
print("\n\n")
print("Fin del juego")