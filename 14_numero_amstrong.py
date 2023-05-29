
'''/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información 
 * al respecto.
 */'''
 
def es_numero_armstrong(numero):
        # Convierte el número en una cadena de caracteres
    numero_str = str(numero)
    # Calcula la longitud del número
    n = len(numero_str)
    # Inicializa la suma
    suma = 0
    
    # Recorre cada dígito
    for digito in numero_str:
        # Convierte el dígito a un número entero y calcula la potencia
        suma += int(digito) ** n
    
    # Compara si la suma es igual al número original
    if suma == numero:
        return True
    else:
        return False

# Ejemplos de uso
print(es_numero_armstrong(153))  # True
print(es_numero_armstrong(370))  # True
print(es_numero_armstrong(9474)) # True
print(es_numero_armstrong(123))  # False
