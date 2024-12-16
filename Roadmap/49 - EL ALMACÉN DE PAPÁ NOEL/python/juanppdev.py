"""
 * EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 * 
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 * 
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y 
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 * 
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
"""

import random

def generar_codigo_secreto():
    """Genera un código secreto aleatorio de 4 caracteres únicos (letras A-C, números 1-3)."""
    caracteres = list("ABC123")
    return ''.join(random.sample(caracteres, 4))

def evaluar_intento(codigo_secreto, intento):
    """Evalúa el intento del usuario y retorna una lista con resultados por carácter."""
    resultado = []
    for i, char in enumerate(intento):
        if char == codigo_secreto[i]:
            resultado.append("Correcto")
        elif char in codigo_secreto:
            resultado.append("Presente")
        else:
            resultado.append("Incorrecto")
    return resultado

def validar_intento(intento):
    """Valida que el intento tenga la longitud adecuada y contenga caracteres permitidos."""
    if len(intento) != 4:
        return False, "El intento debe tener 4 caracteres."
    caracteres_validos = set("ABC123")
    if not all(char in caracteres_validos for char in intento):
        return False, "El intento contiene caracteres no permitidos."
    return True, ""

def main():
    print("\u2728\u2728 BIENVENIDO AL JUEGO DE PAPÁ NOEL \u2728\u2728")
    print("\nTienes que adivinar el código secreto del almacén.\n")

    codigo_secreto = generar_codigo_secreto()
    intentos_restantes = 10

    while intentos_restantes > 0:
        print(f"Intentos restantes: {intentos_restantes}")
        intento = input("Introduce un código de 4 caracteres (A-C, 1-3): ").upper()

        valido, mensaje = validar_intento(intento)
        if not valido:
            print(mensaje)
            continue

        resultado = evaluar_intento(codigo_secreto, intento)
        print("Resultado del intento: ", resultado)

        if intento == codigo_secreto:
            print("\n\u2728\u2728 \u2728\u2728 ¡FELICIDADES! Has adivinado el código secreto. Papá Noel podrá repartir los regalos. \u2728\u2728 \u2728\u2728")
            input("Presiona Enter para salir...")
            break

        intentos_restantes -= 1

    if intentos_restantes == 0:
        print(f"\nLo siento, has agotado tus intentos. El código secreto era: {codigo_secreto}.")
        print("Papá Noel no podrá repartir los regalos este año...")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()
