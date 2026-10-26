def solicitar_nombre():
    while True:
        nombre = input("Introduce nombre: ").strip()

        if nombre == "":
            print("Introduce un nombre válido.")
        else:
            return nombre

def solicitar_dorsal(jugadores, jugador_actual=None):
    while True:
        try:
            dorsal = int(input("Introduce dorsal: "))
            jugador_existente = buscar_jugador(jugadores, dorsal)

            if jugador_existente is not None and jugador_existente is not jugador_actual:
                print("Error: este dorsal pertenece a otro jugador")
            else:
                return dorsal
        except ValueError:
            print("Error: debes introducir un número válido.")

def solicitar_posicion(posiciones):
    while True:
        posicion = input("Introduce posición: ").strip().capitalize()

        if posicion not in posiciones:
            print("Error: posición no válida.")
        else:
            return posicion