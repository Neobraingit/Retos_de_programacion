'''/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */'''
 
def evaluar_carrera(atleta, pista):
        # Verificar que el atleta y la pista tengan la misma longitud
    if len(atleta) != len(pista):
        print("Error: la longitud del atleta y la pista no coincide.")
        return False

    for i in range(len(atleta)):
        if atleta[i] == "run" and pista[i] == "_":
            # Atleta corre en el suelo, no se modifica la pista
            pass
        elif atleta[i] == "jump" and pista[i] == "|":
            # Atleta salta una valla, no se modifica la pista
            pass
        elif atleta[i] == "run" and pista[i] == "|":
            # Atleta corre en una valla, se modifica la pista por "/"
            pista = pista[:i] + "/" + pista[i+1:]
        elif atleta[i] == "jump" and pista[i] == "_":
            # Atleta salta en el suelo, se modifica la pista por "x"
            pista = pista[:i] + "x" + pista[i+1:]
        else:
            # Opción incorrecta, el atleta no ha superado la carrera
            return False

    # Imprimir cómo ha finalizado la carrera
    print("Pista final:", pista)

    # Retornar True si el atleta ha superado correctamente la carrera
    return True

# Ejemplo de uso
atleta = ["run", "jump", "run", "run", "jump"]
pista = "__|_|_"
if evaluar_carrera(atleta, pista):
    print("El atleta ha superado correctamente la carrera.")
else:
    print("El atleta no ha superado la carrera.")
