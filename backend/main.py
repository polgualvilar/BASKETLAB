
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
