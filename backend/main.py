
equipo = "Divieto Basket"

jugadores = [
    {
        "nombre": "Victor",
        "dorsal": 30,
        "posicion": "Exterior"
    },
    {
        "nombre": "Pol",
        "dorsal": 15,
        "posicion": "Exterior"
    },
    {
        "nombre": "Pedro",
        "dorsal": 7,
        "posicion": "Exterior"
    },
    {
        "nombre": "Ivan",
        "dorsal": 5,
        "posicion": "Exterior"
    },
    {
        "nombre": "Eloi",
        "dorsal": 22,
        "posicion": "Exterior"
    },
    {
        "nombre": "Pelayo",
        "dorsal": 12,
        "posicion": "Exterior"
    },
    {
        "nombre": "Migue",
        "dorsal": 9,
        "posicion": "Interior"
    },
    {
        "nombre": "Kevin",
        "dorsal": 24,
        "posicion": "Interior"
    },
    {
        "nombre": "Jeff",
        "dorsal": 11,
        "posicion": "Interior"
    }
]

print("Bienvenido a Divieto by BasketLab")
print("Equipo:", equipo)
print("Número de jugadores:", len(jugadores))

print("--- PLANTILLA ---")

for jugador in jugadores:
    print(f"Nombre: {jugador['nombre']}")
    print(f"Dorsal: {jugador['dorsal']}")
    print(f"Posición: {jugador['posicion']}")
    print("---------------")

try:
    dorsal = int(input("Introduce el dorsal del jugador: "))

    for jugador in jugadores:
        if jugador["dorsal"] == dorsal:
            print(f"Nombre: {jugador['nombre']}")
            print(f"Dorsal: {jugador['dorsal']}")
            print(f"Posición: {jugador['posicion']}")
            break
    else:
        print("No se encontró ningún jugador con ese dorsal.")

except ValueError:
    print("Error: debes introducir un número válido.")

def mostrar_bienvenida(equipo):
    print("Bienvenido a BasketLab")
    print("Equipo:", equipo)
    print("Número de jugadores:", len(jugadores))

mostrar_bienvenida("RCDE")

def mostrar_plantillas(jugadores):
    for jugador in jugadores:
        print(f"Nombre: {jugador['nombre']}")
        print(f"Dorsal: {jugador['dorsal']}")
        print(f"Posición: {jugador['posicion']}")
        print("---------------")

mostrar_plantillas(jugadores)

def contar_jugadores(jugadores):
    return len(jugadores)

resultado = contar_jugadores(jugadores)
print("Número de jugadores de Divieto Basket:", resultado)

def buscar_jugador(jugadores, dorsal):
    for jugador in jugadores:
        if jugador['dorsal'] == dorsal:
            return jugador
    return None
    
        
resultado = buscar_jugador(jugadores, 15)

if resultado is not None:
    print("---JUGADOR ENCONTRADO---")
    print(f"Nombre: {resultado['nombre']}")
    print(f"Dorsal: {resultado['dorsal']}")
    print(f"Posición: {resultado['posicion']}")
else:
    print("Jugador no encontrado")