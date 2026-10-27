import json

def cargar_jugadores(ruta="data/jugadores.json"):
    with open(ruta, "r", encoding="utf-8") as archivo:
        jugadores = json.load(archivo)

    return jugadores

def guardar_jugadores(jugadores, ruta="data/jugadores.json"):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(jugadores, archivo, indent=4, ensure_ascii=False)