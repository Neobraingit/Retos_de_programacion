'''/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */'''
 
def caracteres_diferentes(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    out1 = ''.join(c for c in str1 if c not in set2)
    out2 = ''.join(c for c in str2 if c not in set1)

    return out1, out2

# Ejemplo de uso
str1 = "Hola mundo"
str2 = "Hola amigos"

resultado1, resultado2 = caracteres_diferentes(str1, str2)

print("out1:", resultado1)
print("out2:", resultado2)

 