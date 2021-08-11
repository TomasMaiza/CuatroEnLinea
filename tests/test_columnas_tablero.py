from src.CuatroEnLinea import contenidoColumna, columnaValida, todasLasColumnas

def test_contenido_columna():
    tablero = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 2],
        [0, 0, 1, 2, 0, 2, 1]
    ]
    assert [0, 0, 0, 1, 2, 1] == contenidoColumna(3, tablero)

def test_todas_las_columnas():
    tablero = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 2],
        [0, 0, 1, 2, 0, 2, 1]
    ]
    assert todasLasColumnas(tablero) == [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 2, 1], [0, 0, 0, 0, 1, 2], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 2, 1]]

def test_columna_valida():
    assert columnaValida(4) == 1

def test_columna_invalida():
    assert columnaValida(9) == -1