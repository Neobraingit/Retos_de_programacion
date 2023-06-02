'''/*
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
 */'''
 
def convertir_a_milisegundos(dias, horas, minutos, segundos):
        total_segundos = segundos + minutos * 60 + horas * 3600 + dias * 86400
        milisegundos = total_segundos * 1000
        return milisegundos

# Ejemplo de uso
d = 2  # días
h = 4  # horas
m = 30  # minutos
s = 45  # segundos

resultado = convertir_a_milisegundos(d, h, m, s)
print(resultado)  # Output: 185085000
