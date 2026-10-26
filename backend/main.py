
# ==================================================
# BASKETLAB - GESTIÓN DE EQUIPOS DE BALONCESTO
# ==================================================

# ==================================================
# 1. IMPORTACIONES
# ==================================================

from almacenamiento import cargar_jugadores, guardar_jugadores
from consultas import buscar_jugador
from jugadores import agregar_jugador, modificar_jugador, eliminar_jugador
from config import posiciones
# ==================================================
# 2. CONFIGURACIÓN Y DATOS DEL EQUIPO
# ==================================================

# Información del equipo
equipo = "Divieto Basket"


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


# ==================================================
# 4. FUNCIONES DE ALMACENAMIENTO
# ==================================================



# ==========================================
# FUNCIONES AUXILIARES Y VALIDACIONES
# ==========================================



# ==================================================
# 5. FUNCIONES DE GESTIÓN
# ==================================================





    

# 3. Eliminar un jugador de la plantilla

         

                    







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
                modificar_jugador(jugadores, posiciones)
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

