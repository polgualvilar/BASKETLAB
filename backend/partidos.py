import json

from validaciones import comprobar_rival, comprobar_id_partido

def crear_partido(id, rival, fecha, lugar, puntos_favor, puntos_contra):
    id = comprobar_id_partido(id)
    rival = comprobar_rival(rival)
    partido = {
        "id": id,
        "rival": rival,
        "fecha": fecha,
        "lugar": lugar,
        "puntos_favor": puntos_favor,
        "puntos_contra": puntos_contra
    }

    return partido

def registrar_partido(partidos, partido):

    for existente in partidos:
        if existente["id"] == partido["id"]:
            raise ValueError("Ya existe un partido con este ID.")
    
    partidos.append(partido)
    return partido