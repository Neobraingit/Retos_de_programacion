'''/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */'''

def son_anagramas(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return False

    caracteres1 = list(palabra1)
    caracteres2 = list(palabra2)

    for caracter in caracteres1:
        if caracter in caracteres2:
            caracteres2.remove(caracter)
        else:
            return False

    return len(caracteres2) == 0

# Ejemplo de uso:
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if son_anagramas(palabra1, palabra2):
    print("Las palabras son anagramas.")
else:
    print("Las palabras no son anagramas.")
