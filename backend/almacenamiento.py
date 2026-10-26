def cargar_jugadores():
    with open("data/jugadores.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return datos

def guardar_jugadores(jugadores):
    with open("data/jugadores.json", "w", encoding="utf-8") as archivo:
        json.dump(jugadores, archivo, indent=4, ensure_ascii=False)