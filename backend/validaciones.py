from consultas import buscar_jugador

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

            return comprobar_dorsal(dorsal, jugadores, jugador_actual)

        except ValueError as error:
            print(f"Error: {error}")

def solicitar_posicion(posiciones):
    while True:
        posicion = input("Introduce posición: ").strip().capitalize()

        if posicion not in posiciones:
            print("Error: posición no válida.")
        else:
            return posicion

def comprobar_nombre(nombre):
    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío.")
    
    return nombre.strip()

def comprobar_dorsal(dorsal, jugadores, jugador_actual=None):
    if not isinstance(dorsal, int):
        raise ValueError("El dorsal debe ser un número entero.")

    if dorsal < 0:
        raise ValueError("El dorsal no puede ser negativo.")

    jugador_existente = buscar_jugador(jugadores, dorsal)
    if jugador_existente is not None and jugador_existente is not jugador_actual:
        raise ValueError("Este dorsal pertenece a otro jugador.")
    
    return dorsal

def comprobar_posicion(posicion, posiciones):
    posicion = posicion.strip().capitalize()
    
    if not isinstance(posicion, str):
        raise ValueError("La posición debe ser una cadena de texto.")
    
    if posicion not in posiciones:
        raise ValueError("Posición no válida.")
    
    return posicion