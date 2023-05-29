'''/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */'''
 
from datetime import datetime

def calcular_diferencia_en_dias(fecha1, fecha2):
    try:
        # Convierte las cadenas de texto en fechas
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Las cadenas de texto no representan fechas correctas.")

    # Calcula la diferencia absoluta en días
    diferencia = abs(fecha1_obj - fecha2_obj)

    # Retorna la diferencia en días como un entero
    return diferencia.days

# Ejemplo de uso
fecha1 = "01/05/2023"
fecha2 = "15/05/2023"
diferencia = calcular_diferencia_en_dias(fecha1, fecha2)
print(diferencia)  # Output: 14
