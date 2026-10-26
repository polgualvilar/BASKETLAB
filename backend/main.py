
# ==================================================
# BASKETLAB - GESTIÓN DE EQUIPOS DE BALONCESTO
# ==================================================

# ==================================================
# 1. IMPORTACIONES
# ==================================================

import json

# ==================================================
# 2. CONFIGURACIÓN Y DATOS DEL EQUIPO
# ==================================================

# Información del equipo
equipo = "Divieto Basket"

# Posiciones disponibles
posiciones = ["Interior", "Exterior"]

# Plantilla del equipo
"""jugadores = [
    {"nombre": "Victor", "dorsal": 30, "posicion": "Exterior"},
    {"nombre": "Pol", "dorsal": 15, "posicion": "Exterior"},
    {"nombre": "Pedro", "dorsal": 7, "posicion": "Exterior"},
    {"nombre": "Ivan", "dorsal": 5, "posicion": "Exterior"},
    {"nombre": "Eloi", "dorsal": 22, "posicion": "Exterior"},
    {"nombre": "Pelayo", "dorsal": 12, "posicion": "Exterior"},
    {"nombre": "Migue", "dorsal": 9, "posicion": "Interior"},
    {"nombre": "Kevin", "dorsal": 24, "posicion": "Interior"},
    {"nombre": "Jeff", "dorsal": 11, "posicion": "Interior"}
]
"""

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

def cargar_jugadores():
    with open("data/jugadores.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return datos

def guardar_jugadores(jugadores):
    with open("data/jugadores.json", "w", encoding="utf-8") as archivo:
        json.dump(jugadores, archivo, indent=4, ensure_ascii=False)


# ==================================================
# 5. FUNCIONES DE GESTIÓN
# ==================================================

# Añadir un jugador a la plantilla

def agregar_jugador(jugadores, posiciones):

    # Validación del nombre
    while True:
        nombre = input("Introduce nombre: ").strip()

        if nombre == "":
            print("Introduce un nombre válido.")
        else:
            break

    # Validación del dorsal
    while True:
        try:
            dorsal = int(input("Introduce dorsal: "))

            if buscar_jugador(jugadores, dorsal) is not None:
                print("Error: este dorsal ya está ocupado")
            else:
                break

        except ValueError:
            print("Error: debes introducir un número válido.")

    while True:
        posicion = input("Introduce posición: ").strip().capitalize()

        if posicion not in posiciones:
            print ("Posición no valida")
        else:
            break

    jugador = {
        "nombre": nombre,
        "dorsal": dorsal,
        "posicion": posicion
    }

    jugadores.append(jugador)

    print("Jugador añadido correctamente.")


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
        print("4. Salir")
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

            # OPCIÓN 4 - SALIR
            elif opcion == 4:
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

