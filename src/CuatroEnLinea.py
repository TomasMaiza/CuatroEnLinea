from os import system
import colorsys

def tableroVacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

def columnaValida(columna):
    if columna > 7 or columna < 1:
        return -1
    else:
        return 1

'''def ingresarSecuencia(secuencia):
    if len(secuencia) % 2 == 0:
        turno = "Jugador 1 debe ingresar una columna: "
    else:
        turno = "Jugador 2 debe ingresar una columna: "
    columna = int(input(turno))
    if (columnaValida(columna) == -1):
        return -1
    else:
        secuencia.append(columna)
        return 1'''
        

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila-1][columna-1] == 0:
            tablero[fila-1][columna-1] = ficha
            return

def completarTableroEnOrden(secuencia, tablero, turno):
    l = len(secuencia)
    '''if l % 2 == 0:
        ficha = 2
    else:
        ficha = 1'''
    if (turno % 2 == 0):
        ficha = 1
    else:
        ficha = 2
    columna = secuencia[l-1]
    soltarFichaEnColumna(ficha, columna, tablero)

def dibujarTablero(tablero):
    print("+- - - - - - - -+")
    for i in range(6):
        print("| ", end = "")
        for j in range(7):
           print("{0} ".format(tablero[i][j]), end = "")
        print("|")
    print("+---------------+")

def contenidoColumna(nro_columna, tablero):
    columna = []
    for fila in tablero:
        celda = fila[nro_columna-1]
        columna.append(celda)
    return columna

def contenidoFila(nro_fila, tablero):
    fila = tablero[nro_fila-1]
    return fila

def todasLasColumnas(tablero):
    columnas = [None] * 7
    for i in range(7):
        columnas[i] = contenidoColumna((i+1), tablero)
    return columnas

def todasLasFilas(tablero):
    filas = [None] * 6
    for i in range(6):
        filas[i] = contenidoFila((i+1), tablero)
    return filas

tablero = tableroVacio()
secuencia = [1, 4, 2, 3, 1, 1, 2]
i = 0
while (i < len(secuencia)):
    if(columnaValida(secuencia[i]) == (-1)):
        print("Secuencia invalida")
        break
    else:
        i += 1
i = 0
while (i < len(secuencia)):
    completarTableroEnOrden([secuencia[i]], tablero, i)
    i += 1
'''system("cls")
print("4 EN LINEA")
system("pause")
system("cls")
while len(secuencia) < (7*6):
    dibujarTablero(tablero)
    print("\n\n")
    sec = ingresarSecuencia(secuencia)
    if sec < 0:
        print("\nNumero de columna inv??lida. Por favor, ingresar un n??mero entre 1 y 7.\n")
        system("pause")
    else:
        system("cls")
        completarTableroEnOrden(secuencia, tablero)
        print("")'''
    #system("cls")
dibujarTablero(tablero)
#print("\n\nFin del juego")