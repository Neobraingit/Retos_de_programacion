'''/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */'''
 
 def calcular_area_poligono(poligono):
        tipo_poligono = poligono['tipo']
    if tipo_poligono == 'triangulo':
        base = poligono['base']
        altura = poligono['altura']
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    elif tipo_poligono == 'cuadrado':
        lado = poligono['lado']
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")
    elif tipo_poligono == 'rectangulo':
        base = poligono['base']
        altura = poligono['altura']
        area = base * altura
        print(f"El área del rectángulo es: {area}")
    else:
        print("Polígono no soportado")

# Ejemplos de uso:
triangulo = {'tipo': 'triangulo', 'base': 4, 'altura': 3}
cuadrado = {'tipo': 'cuadrado', 'lado': 5}
rectangulo = {'tipo': 'rectangulo', 'base': 6, 'altura': 8}

calcular_area_poligono(triangulo)
calcular_area_poligono(cuadrado)
calcular_area_poligono(rectangulo)
