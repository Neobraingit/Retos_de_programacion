'''/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */'''
 
def verificar_equilibrio(expresion):
        pila = []
delimitadores = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

for caracter in expresion:
        if caracter in delimitadores.keys():
            pila.append(caracter)
        elif caracter in delimitadores.values():
            if len(pila) == 0 or caracter != delimitadores[pila.pop()]:
                return False

    return len(pila) == 0

# Ejemplos
expresion_balanceada = "{[a * (c + d)] - 5}"
expresion_no_balanceada = "{a * (c + d)] - 5}"

if verificar_equilibrio(expresion_balanceada):
    print("La expresión está balanceada.")
else:
    print("La expresión no está balanceada.")

if verificar_equilibrio(expresion_no_balanceada):
    print("La expresión está balanceada.")
else:
    print("La expresión no está balanceada.")
