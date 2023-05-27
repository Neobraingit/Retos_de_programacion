'''/*
 Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13. *..
 */'''
 
 # Función para generar la sucesión de Fibonacci
def fibonacci(n):
    # Inicializar los primeros dos números
    fib = [0, 1]
    
    # Generar la sucesión
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

# Imprimir los primeros 50 números de Fibonacci
fibonacci_sequence = fibonacci(50)
for num in fibonacci_sequence:
    print(num)
