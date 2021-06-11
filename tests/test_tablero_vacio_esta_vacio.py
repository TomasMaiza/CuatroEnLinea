from src.CuatroEnLinea import tableroVacio

def tets_tablero_vacio_esta_vacio():
    tablero = tableroVacio()
    for i in range(6):
        assert tablero[i] == [0, 0, 0, 0, 0, 0, 0]