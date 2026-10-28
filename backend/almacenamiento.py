import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def cargar_jugadores(ruta=BASE_DIR / "data/jugadores.json"):
    with open(ruta, "r", encoding="utf-8") as archivo:
        jugadores = json.load(archivo)

    return jugadores

def guardar_jugadores(jugadores, ruta=BASE_DIR / "data/jugadores.json"):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(jugadores, archivo, indent=4, ensure_ascii=False)

def cargar_partidos(ruta=BASE_DIR / "data/partidos.json"):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
                partidos = json.load(archivo)

        return partidos
    except FileNotFoundError:
        return []

def guardar_partidos(partidos, ruta=BASE_DIR / "data/partidos.json"):
     with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(partidos, archivo, indent=4, ensure_ascii=False)