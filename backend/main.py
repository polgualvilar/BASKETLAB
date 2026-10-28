from almacenamiento import cargar_jugadores, guardar_jugadores, cargar_partidos, guardar_partidos
from consultas import buscar_jugador
from jugadores import agregar_jugador, modificar_jugador, eliminar_jugador
from config import posiciones
from partidos import agregar_partido


# ==========================================
# 1. CONFIGURACIÓN
# ==========================================

equipo = "Divieto Basket"


# ==========================================
# 2. FUNCIONES DE CONSULTA
# ==========================================

def mostrar_bienvenida(equipo):
    print(f"\nBienvenido a BasketLab - {equipo}")


def mostrar_plantilla(jugadores):
    print("\n--- PLANTILLA ---")

    if not jugadores:
        print("No hay jugadores registrados.")
        return

    for jugador in jugadores:
        print(f"Nombre: {jugador['nombre']}")
        print(f"Dorsal: {jugador['dorsal']}")
        print(f"Posición: {jugador['posicion']}")
        print("----------------")


def mostrar_partidos(partidos):
    print("\n--- PARTIDOS ---")

    if not partidos:
        print("No hay partidos registrados.")
        return

    for partido in partidos:
        print(f"ID: {partido['id']}")
        print(f"Rival: {partido['rival']}")
        print(f"Fecha: {partido['fecha']}")
        print(f"Lugar: {partido['lugar']}")
        print(
            f"Resultado: {partido['puntos_favor']} - "
            f"{partido['puntos_contra']}"
        )
        print("----------------")


def contar_jugadores(jugadores):
    return len(jugadores)


# ==========================================
# 3. MENÚ DE PLANTILLA
# ==========================================

def menu_plantilla(jugadores, posiciones):

    while True:
        print("\n=== GESTIÓN DE PLANTILLA ===")
        print("1. Mostrar plantilla")
        print("2. Buscar jugador")
        print("3. Añadir jugador")
        print("4. Modificar jugador")
        print("5. Eliminar jugador")
        print("6. Volver al menú principal")

        try:
            opcion = int(input("\nSelecciona una opción: "))

            if opcion == 1:
                mostrar_plantilla(jugadores)

            elif opcion == 2:
                dorsal = int(input("Introduce dorsal: "))
                resultado = buscar_jugador(jugadores, dorsal)

                if resultado is not None:
                    print("\n--- JUGADOR ENCONTRADO ---")
                    print(f"Nombre: {resultado['nombre']}")
                    print(f"Dorsal: {resultado['dorsal']}")
                    print(f"Posición: {resultado['posicion']}")
                else:
                    print("Jugador no encontrado.")

            elif opcion == 3:
                agregar_jugador(jugadores, posiciones)
                guardar_jugadores(jugadores)
                mostrar_plantilla(jugadores)

            elif opcion == 4:
                modificar_jugador(jugadores, posiciones)
                guardar_jugadores(jugadores)

            elif opcion == 5:
                eliminar_jugador(jugadores)
                guardar_jugadores(jugadores)

            elif opcion == 6:
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Error: debes introducir un número válido.")


# ==========================================
# 4. MENÚ DE PARTIDOS
# ==========================================

def menu_partidos(partidos):

    while True:
        print("\n=== GESTIÓN DE PARTIDOS ===")
        print("1. Mostrar partidos")
        print("2. Registrar partido")
        print("3. Volver al menú principal")

        try:
            opcion = int(input("\nSelecciona una opción: "))

            if opcion == 1:
                mostrar_partidos(partidos)

            elif opcion ==2:
                agregar_partido(partidos)
                guardar_partidos(partidos)

            elif opcion == 3:
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Error: debes introducir un número válido.")


# ==========================================
# 5. MENÚ PRINCIPAL
# ==========================================

def menu_principal(equipo, jugadores, posiciones, partidos):

    mostrar_bienvenida(equipo)

    while True:
        print("\n=== BASKETLAB ===")
        print("1. Plantilla")
        print("2. Partidos")
        print("3. Salir")

        try:
            opcion = int(input("\nSelecciona una opción: "))

            if opcion == 1:
                menu_plantilla(jugadores, posiciones)

            elif opcion == 2:
                menu_partidos(partidos)

            elif opcion == 3:
                print("Cerrando BasketLab...")
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Error: debes introducir un número válido.")


# ==========================================
# 6. INICIO DEL PROGRAMA
# ==========================================

if __name__ == "__main__":
    jugadores = cargar_jugadores()
    partidos = cargar_partidos()

    menu_principal(equipo, jugadores, posiciones, partidos)
