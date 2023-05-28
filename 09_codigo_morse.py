'''/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */'''
 
 # Diccionario para convertir texto a código Morse
texto_a_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': ' '
}

# Diccionario para convertir código Morse a texto
morse_a_texto = {value: key for key, value in texto_a_morse.items()}

def convertir_texto_a_morse(texto):
    morse = ''
    for char in texto:
        if char.upper() in texto_a_morse:
            morse += texto_a_morse[char.upper()] + ' '
    return morse.strip()

def convertir_morse_a_texto(morse):
    texto = ''
    palabras = morse.split('  ')
    for palabra in palabras:
        letras = palabra.split(' ')
        for letra in letras:
            if letra in morse_a_texto:
                texto += morse_a_texto[letra]
        texto += ' '
    return texto.strip()

def detectar_tipo(texto):
    if any(char in '.-' for char in texto):
        return 'morse'
    else:
        return 'texto'

def main():
    entrada = input("Ingrese el texto o código Morse a convertir: ")
    tipo = detectar_tipo(entrada)

    if tipo == 'texto':
        morse = convertir_texto_a_morse(entrada)
        print("El código Morse correspondiente es:", morse)
    else:
        texto = convertir_morse_a_texto(entrada)
        print("El texto correspondiente es:", texto)

if __name__ == '__main__':
    main()
