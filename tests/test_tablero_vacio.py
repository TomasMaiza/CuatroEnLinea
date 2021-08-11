from src.CuatroEnLinea import tableroVacio

def test_tablero_vacio_tiene_6_filas():
    tablero = tableroVacio()
    assert len(tablero) == 6

def test_tablero_vacio_tiene_7_columnas():
    tablero = tableroVacio()
    assert len(tablero[0]) == 7

def test_tablero_vacio_esta_vacio():
    tablero = tableroVacio()
    for i in range(6):
        assert tablero[i] == [0, 0, 0, 0, 0, 0, 0]