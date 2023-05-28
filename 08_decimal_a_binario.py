'''/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */'''
 
numero_decimal = int(input("Ingrese un número decimal: "))

# Verificar si el número es cero
if numero_decimal == 0:
    binario = '0'
else:
    binario = ''

    # Realizar la conversión
    while numero_decimal > 0:
        residuo = numero_decimal % 2
        binario = str(residuo) + binario
        numero_decimal = numero_decimal // 2

print("El número binario correspondiente es:", binario)

    