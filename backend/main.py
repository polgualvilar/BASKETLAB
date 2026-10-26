
# ==================================================
# BASKETLAB - GESTIÓN DE EQUIPOS DE BALONCESTO
# ==================================================

# ==================================================
# 1. IMPORTACIONES
# ==================================================

import json

from validaciones import solicitar_nombre, solicitar_dorsal, solicitar_posicion

from almacenamiento import cargar_jugadores, guardar_jugadores

# ==================================================
# 2. CONFIGURACIÓN Y DATOS DEL EQUIPO
# ==================================================

# Información del equipo
equipo = "Divieto Basket"

# Posiciones disponibles
posiciones = ["Interior", "Exterior"]


# ==================================================
# 3. FUNCIONES DE CONSULTA
# ==================================================

# Mostrar información general del equipo
def mostrar_bienvenida(equipo):
    print("Bienvenido a BasketLab", equipo)



# Mostrar todos los jugadores del equipo
def mostrar_plantillas(jugadores):
    print("\n--- PLANTILLA ---")

    for jugador in jugadores:
        print(f"Nombre: {jugador['nombre']}")
        print(f"Dorsal: {jugador['dorsal']}")
        print(f"Posición: {jugador['posicion']}")
        print("----------------")


# Contar el número de jugadores
def contar_jugadores(jugadores):
    return len(jugadores)


# Buscar un jugador por su dorsal
def buscar_jugador(jugadores, dorsal):
    for jugador in jugadores:
        if jugador["dorsal"] == dorsal:
            return jugador

    return None

# ==================================================
# 4. FUNCIONES DE ALMACENAMIENTO
# ==================================================



# ==========================================
# FUNCIONES AUXILIARES Y VALIDACIONES
# ==========================================



# ==================================================
# 5. FUNCIONES DE GESTIÓN
# ==================================================

# Añadir un jugador a la plantilla

def agregar_jugador(jugadores, posiciones):

    # Validación del nombre
    nombre = solicitar_nombre()

    # Validación del dorsal
    dorsal = solicitar_dorsal(jugadores)


    posicion = solicitar_posicion(posiciones)

    jugador = {
        "nombre": nombre,
        "dorsal": dorsal,
        "posicion": posicion
    }

    jugadores.append(jugador)

    print("Jugador añadido correctamente.")


# Modificar un jugador a la plantilla

def modificiar_jugador(jugadores, posiciones):

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

                resultado["nombre"] = modificar_nombre
                print("Nombre modificado correctamente.")
                
            elif opcion_modificar == 2:
                modificar_dorsal = solicitar_dorsal(jugadores, resultado)

                resultado["dorsal"] = modificar_dorsal
                print("Dorsal modificado correctamente.")
                
            elif opcion_modificar == 3:
                modificar_posicion = solicitar_posicion(posiciones)

                resultado["posicion"] = modificar_posicion
                print("Posición modificada correctamente.")

            elif opcion_modificar == 4:

                modificar_nombre = solicitar_nombre()
        
                modificar_dorsal = solicitar_dorsal(jugadores, resultado)
                
                modificar_posicion = solicitar_posicion(posiciones)

                resultado["nombre"] = modificar_nombre
                resultado["dorsal"] = modificar_dorsal
                resultado["posicion"] = modificar_posicion

                print("Jugador modificado correctamente.")
            elif opcion_modificar == 5:
                break
            else:
                print("Opción no valida.")
        except ValueError:
            print("Error: debes introducir un número válido.")
    pass
    

# 3. Eliminar un jugador de la plantilla

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
                jugadores.remove(resultado)
                print("Jugador eliminado correctamente")
                break

            elif opcion_eliminar == 2:
                print("Eliminacion cancelada.")
                break

            else:
                print("Opción no valida")
        except ValueError:
            print("Error: debes introducir un número válido.")         

                    







# --------------------------------------------------
# FUTURAS FUNCIONES DE GESTIÓN
# --------------------------------------------------

# Aquí añadiremos:
# - Validar dorsales duplicados
# - Modificar datos de un jugador
# - Eliminar jugadores
# - Guardar y cargar datos


# ==================================================
# 6. MENÚ PRINCIPAL
# ==================================================

def menu_principal(equipo, jugadores, posiciones):

    mostrar_bienvenida(equipo)

    while True:
        print("\n=== BASKETLAB ===")
        print("1. Mostrar plantilla")
        print("2. Buscar jugador")
        print("3. Añadir jugador")
        print("4. Modificar jugador")
        print("5. Eliminar jugador")
        print("6. Salir")
        print("")

        try:
            opcion = int(input("Selecciona una opción: "))

            # OPCIÓN 1 - MOSTRAR PLANTILLA
            if opcion == 1:
                mostrar_plantillas(jugadores)

            # OPCIÓN 2 - BUSCAR JUGADOR
            elif opcion == 2:

                dorsal = int(input("Introduce dorsal: "))
                resultado = buscar_jugador(jugadores, dorsal)

                if resultado is not None:
                    print("\n--- JUGADOR ENCONTRADO ---")
                    print(f"Nombre: {resultado['nombre']}")
                    print(f"Dorsal: {resultado['dorsal']}")
                    print(f"Posición: {resultado['posicion']}")
                else:
                    print("Jugador no encontrado")

            # OPCIÓN 3 - AÑADIR JUGADOR
            elif opcion == 3:
                agregar_jugador(jugadores, posiciones)
                mostrar_plantillas(jugadores)
                guardar_jugadores(jugadores)

            # OPCIÓN 4 - MODIFICAR JUGADOR
            elif opcion == 4:
                modificiar_jugador(jugadores, posiciones)
                guardar_jugadores(jugadores)

            # OPCIÓN 5 - ELIMINAR JUGADOR    
            elif opcion == 5:
                eliminar_jugador(jugadores)
                guardar_jugadores(jugadores)
                

            # OPCIÓN 6 - SALIR
            elif opcion == 6:
                print("Cerrando BasketLab...")
                break
                            
            # OPCIÓN NO VÁLIDA
            else:
                print("Opción no válida")

        except ValueError:
            print("Error: debes introducir un número válido.")


# ==================================================
# 7. INICIO DEL PROGRAMA
# ==================================================

jugadores = cargar_jugadores()

menu_principal(equipo, jugadores, posiciones)

