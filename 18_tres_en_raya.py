'''/*
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
 */'''
 
def analizar_matriz(matriz):
        # Verificar si hay un número igual de "X" y "O"
    cantidad_x = sum(fila.count("X") for fila in matriz)
    cantidad_o = sum(fila.count("O") for fila in matriz)
    if cantidad_x != cantidad_o:
        return "Nulo"

    # Verificar si hay un ganador en filas
    for fila in matriz:
        if fila.count("X") == 3:
            return "X"
        elif fila.count("O") == 3:
            return "O"

    # Verificar si hay un ganador en columnas
    for i in range(3):
        columna = [fila[i] for fila in matriz]
        if columna.count("X") == 3:
            return "X"
        elif columna.count("O") == 3:
            return "O"

    # Verificar si hay un ganador en diagonales
    if matriz[0][0] == matriz[1][1] == matriz[2][2]:
        if matriz[0][0] == "X":
            return "X"
        elif matriz[0][0] == "O":
            return "O"
    if matriz[0][2] == matriz[1][1] == matriz[2][0]:
        if matriz[0][2] == "X":
            return "X"
        elif matriz[0][2] == "O":
            return "O"

    # Si no hay ganador, verificar si hay empate o matriz incompleta
    if cantidad_x + cantidad_o == 9:
        return "Empate"
    else:
        return "Nulo"

# Ejemplo de uso
matriz1 = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", ""]
]
resultado1 = analizar_matriz(matriz1)
print(resultado1)  # Output: "X"

matriz2 = [
    ["O", "X", "O"],
    ["X", "O", "X"],
    ["O", "X", "O"]
]
resultado2 = analizar_matriz(matriz2)
print(resultado2)  # Output: "Empate"
