from validaciones import solicitar_nombre, solicitar_dorsal, solicitar_posicion, comprobar_nombre, comprobar_dorsal, comprobar_posicion
from consultas import buscar_jugador
from config import posiciones


def agregar_jugador(jugadores, posiciones):

    nombre = solicitar_nombre()

    dorsal = solicitar_dorsal(jugadores)

    posicion = solicitar_posicion(posiciones)

    crear_jugador(jugadores, nombre, dorsal, posicion)

    print("Jugador añadido correctamente.")


def crear_jugador(jugadores, nombre, dorsal, posicion):
    nombre = comprobar_nombre(nombre)
    dorsal = comprobar_dorsal(dorsal, jugadores)
    posicion = comprobar_posicion(posicion, posiciones)

    nuevo_jugador = {
        "nombre": nombre,
        "dorsal": dorsal,
        "posicion": posicion
    }

    jugadores.append(nuevo_jugador)

    return nuevo_jugador

def modificar_jugador(jugadores, posiciones):

    # 1. BUSCAR JUGADOR

    while True:
        try:
            dorsal = int(input("Introduce dorsal: "))

            resultado = buscar_jugador(jugadores, dorsal)

            if resultado is not None:
                print("\n--- JUGADOR ENCONTRADO ---")
                print(f"Nombre: {resultado['nombre']}")
                print(f"Dorsal: {resultado['dorsal']}")
                print(f"Posición: {resultado['posicion']}")
                break
            else:
                print("Jugador no encontrado")   

        except ValueError:
                print("Error: debes introducir un número válido.")
    
    # 2. MENÚ DE MODIFICACIÓN

    while True:
        print("\n=== MODIFICAR JUGADOR ===")
        print("1. Modificar nombre")
        print("2. Modificar dorsal")
        print("3. Modificar posición")
        print("4. Modificar todos los datos")
        print("5. Volver al menú principal")
        print("")

        try:
            opcion_modificar = int(input("Selecciona una opción: "))

            if opcion_modificar == 1:
                modificar_nombre = solicitar_nombre()
                actualizar_jugador(resultado, nombre=modificar_nombre)
            elif opcion_modificar == 2:
                modificar_dorsal = solicitar_dorsal(jugadores, resultado)
                actualizar_jugador(resultado, dorsal=modificar_dorsal)

            elif opcion_modificar == 3:
                modificar_posicion = solicitar_posicion(posiciones)
                actualizar_jugador(resultado, posicion=modificar_posicion)

            elif opcion_modificar == 4:

                modificar_nombre = solicitar_nombre()
        
                modificar_dorsal = solicitar_dorsal(jugadores, resultado)
                
                modificar_posicion = solicitar_posicion(posiciones)

                actualizar_jugador(resultado, nombre=modificar_nombre, dorsal=modificar_dorsal, posicion=modificar_posicion)

                print("Jugador modificado correctamente.")
            elif opcion_modificar == 5:
                break
            else:
                print("Opción no valida.")
        except ValueError:
            print("Error: debes introducir un número válido.")

def actualizar_jugador(jugador, jugadores, nombre=None, dorsal=None, posicion=None):

    if nombre is not None:
        nombre = comprobar_nombre(nombre)

    if dorsal is not None:
        dorsal = comprobar_dorsal(dorsal, jugadores, jugador)

    if posicion is not None:
        posicion = comprobar_posicion(posicion, posiciones)

    if nombre is not None:
        jugador["nombre"] = nombre

    if dorsal is not None:
        jugador["dorsal"] = dorsal

    if posicion is not None:
        jugador["posicion"] = posicion

    return jugador

def borrar_jugador(jugadores, jugador):
    jugadores.remove(jugador)
    return jugador
    

def eliminar_jugador(jugadores):
    while True:
        try:
            dorsal = int(input("Introduce dorsal: "))

            resultado = buscar_jugador(jugadores, dorsal)

            if resultado is not None:
                print("\n--- JUGADOR ENCONTRADO ---")
                print(f"Nombre: {resultado['nombre']}")
                print(f"Dorsal: {resultado['dorsal']}")
                print(f"Posición: {resultado['posicion']}")
                break
            else:
                print("Jugador no encontrado")   

        except ValueError:
                print("Error: debes introducir un número válido.")
    
    while True:
        print("Estas seguro de eliminar el jugador de la plantilla?")
        print("1. Si")
        print("2. No")
        try:
            opcion_eliminar = int(input("Selecciona una opción: "))
    
            if opcion_eliminar == 1:
                borrar_jugador(jugadores, resultado)
                print("Jugador eliminado correctamente")
                break

            elif opcion_eliminar == 2:
                print("Eliminacion cancelada.")
                break

            else:
                print("Opción no valida")
        except ValueError:
            print("Error: debes introducir un número válido.")