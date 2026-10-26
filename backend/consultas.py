def buscar_jugador(jugadores, dorsal):
    for jugador in jugadores:
        if jugador["dorsal"] == dorsal:
            return jugador

    return None