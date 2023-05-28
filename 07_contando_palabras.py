'''/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */'''
 
def contar_palabras(texto):
    # Limpiar el texto y dividirlo en palabras
    palabras = texto.lower().split()

    # Diccionario para almacenar el recuento de cada palabra
    recuento = {}

    # Iterar sobre las palabras y actualizar el recuento
    for palabra in palabras:
        # Eliminar signos de puntuación al comienzo y final de la palabra
        palabra = palabra.strip(".,?!-")

        # Si la palabra ya está en el diccionario, aumentar el recuento
        if palabra in recuento:
            recuento[palabra] += 1
        else:
            recuento[palabra] = 1

    return recuento

# Texto de ejemplo
texto_ejemplo = "Este es un ejemplo. Un ejemplo de texto para contar palabras."

# Obtener el recuento de palabras
recuento_palabras = contar_palabras(texto_ejemplo)

# Imprimir el recuento final de palabras
print("Recuento de palabras:")
for palabra, recuento in recuento_palabras.items():
    print(f"{palabra}: {recuento}")

    
    