from src.CuatroEnLinea import contenidoFila, todasLasFilas

def test_contenido_fila():
    tablero = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 2],
        [0, 0, 1, 2, 0, 2, 1]
    ]
    assert [0, 0, 1, 2, 0, 2, 1] == contenidoFila(0, tablero)


def test_todas_las_filas():
    tablero = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 2],
        [0, 0, 1, 2, 0, 2, 1]
    ]
    assert todasLasFilas(tablero) == [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 2, 1, 0, 0, 2], [0, 0, 1, 2, 0, 2, 1]]